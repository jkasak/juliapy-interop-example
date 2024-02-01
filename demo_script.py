import python_src

json_data = """
[
  {"name": "Laptop", "category": "Electronics", "price": 1200},
  {"name": "Desk", "category": "Furniture", "price": 450},
  {"name": "Chair", "category": "Furniture", "price": 150},
  {"name": "Smartphone", "category": "Electronics", "price": 800},
  {"name": "Table Lamp", "category": "Furniture", "price": 90}
]
"""

price = python_src.average_furniture_price(json_data)
print(f"The average price of furniture is {price}€.")
