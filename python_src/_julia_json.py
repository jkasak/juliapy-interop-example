import json


def average_furniture_price(json_str: str) -> float:
    products = json.loads(json_str)
    furniture_products = [product for product in products if product["category"] == "Furniture"]
    average_price = sum(product["price"] for product in furniture_products) / len(furniture_products)
    return average_price
