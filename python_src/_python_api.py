from ._julia_backend import julia_module


def average_furniture_price(json_path: str) -> float:
    return julia_module.average_furniture_price(json_path)
