from typing import List
from car import Car
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from shop import Shop

class Customer:
    def __init__(self, name: str, product_cart: dict, location: list, money: Decimal, car: Car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


    @staticmethod
    def cost_to_shop(customers: list["Customer"], shops: list["Shop"], fuel_price: float) -> dict:
        ride_cost = {}
        for index, customer in enumerate(customers):
            key = f"customer{index + 1}"
            ride_cost[key] = []
    
            for shop in shops:
                distance = customer.distance_between_location(
                    customer.location, shop.location
                )

                cost = customer.calculate_cost_trip(
                    Decimal(str(distance)),
                    Decimal(str(customer.car.fuel_consumption)),
                    Decimal(str(fuel_price))
                ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
                ride_cost[key].append({shop.name: cost})
        return ride_cost


    @staticmethod
    def price_for_road_and_products(customers:  list["Customer"], shops:  list["Shop"], ride_cost: dict):
        for index, customer in enumerate(customers):
            print(f"{customer.name} has {customer.money} dollars")
            list_cost_one_person = []
            for y, shop in enumerate(shops):
                trip_cost = (ride_cost[f"customer{index + 1}"][y][shop.name] +
                             Decimal(str(
                                 customer.sum_for_products(
                                     customer.product_cart,
                                     shop.products))))
                list_cost_one_person.append((shop, trip_cost))

                print(f"{customer.name}'s trip to {shop.name} costs {trip_cost}")
            cheapest_shop, cheapest_price = min(list_cost_one_person, key=lambda x: x[1])


            if customer.money >= cheapest_price:
                print(f"{customer.name} rides to {cheapest_shop.name}")
                customer.receipt(customer.product_cart, cheapest_shop.products)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money - cheapest_price} dollars")
                print("\n")
            else:
                print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


    @staticmethod
    def distance_between_location(
            customer_location: List[int],
            shop_location: List[int]) -> float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


    @staticmethod
    def calculate_cost_trip(distance: Decimal, fuel_consumption: Decimal, fuel_price: Decimal) -> Decimal:
        liters = distance * fuel_consumption / 100
        return liters * fuel_price


    @staticmethod
    def sum_for_products(product_cart:dict, products_shop: dict) -> float:
        return sum(count * products_shop[product]
            for product, count in product_cart.items()
            if product in products_shop)


    def receipt(self, product_cart: dict, products_price: dict) -> None:
        print(f"\nDate: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Thanks, Bob, for your purchase!")
        print("You have bought:")
        for product, count in product_cart.items():
                if product in  products_price:
                    print(f"{count} {product} for {count * products_price[product]}")

        print(f"Total cost is {self.sum_for_products(product_cart,products_price )} dollars")
        print("See you again!\n")


    @staticmethod
    def load_customers(customers: list[dict]) -> List["Customer"]:
        list_instance_customer = []

        for customer in customers:
            person = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],customer["car"]["fuel_consumption"])
            )
            list_instance_customer.append(person)
        return list_instance_customer
