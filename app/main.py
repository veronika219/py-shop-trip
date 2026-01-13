from shop import Shop
from customer import Customer
from content import Content


def shop_trip():
    content = Content.load_content("config.json")

    fuel_price = content.fuel_price
    shops = Shop.load_shops(content.shops)
    customers = Customer.load_customers(content.customers)

    ride_cost = Customer.cost_to_shop(customers, shops, fuel_price)
    Customer.price_for_road_and_products(customers, shops, ride_cost)

shop_trip()

