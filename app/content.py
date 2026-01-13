from typing import List
import json

class Content:
    def __init__(self, fuel_price: float, customers: List[dict], shops: List[dict]) -> None:
        self.fuel_price = fuel_price
        self.customers = customers
        self.shops = shops


    @staticmethod
    def load_content(file: str) -> "Content":
        with open(file, "r") as f:
            content = json.load(f)

        return Content(
            content["FUEL_PRICE"],
            content["customers"],
            content["shops"])