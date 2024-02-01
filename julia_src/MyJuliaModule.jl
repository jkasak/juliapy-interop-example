module MyJuliaModule

using JSON


function average_furniture_price(json_path::String)::Float64
    data = JSON.parsefile(json_path)

    furniture_products = filter(product -> product["category"] == "Furniture", data)
    total_price = sum(product["price"] for product in furniture_products)

    return total_price / length(furniture_products)
end

end