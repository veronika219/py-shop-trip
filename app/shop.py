from typing import List


class Shop:
    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def load_shops(shops: list) -> List["Shop"]:

        list_shop_instance = []

        for shop in shops:
            list_shop_instance.append(Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            ))

        return list_shop_instance

# print(Shop.shop_instance("config.json"))