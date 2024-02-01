import python_src
from pathlib import Path

price = python_src.average_furniture_price(Path("./demo_data.json"))

print(f"The average price of furniture is {price}€.")
