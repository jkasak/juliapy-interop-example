import json
from pathlib import Path


def average_furniture_price(json_path: Path) -> float:
    products = json.loads(json_path.read_text())
    furniture_products = [product for product in products if product["category"] == "Furniture"]
    average_price = sum(product["price"] for product in furniture_products) / len(furniture_products)
    return average_price
