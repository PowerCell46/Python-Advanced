def shopping_cart(*tuples):
    dict = {"Soup": [], "Pizza": [], "Dessert": []}

    for tuple in tuples:
        if tuple == "Stop":
            break
        meal = tuple[0]
        product = tuple[1]
        if meal == "Soup":
            if product not in dict["Soup"] and len(dict["Soup"]) < 3:
                dict["Soup"].append(product)
        elif meal == "Pizza":
            if product not in dict["Pizza"] and len(dict["Pizza"]) < 4:
                dict["Pizza"].append(product)
        elif meal == "Dessert":
            if product not in dict["Dessert"] and len(dict["Dessert"]) < 2:
                dict["Dessert"].append(product)
                
    if len(dict["Soup"]) == 0 and len(dict["Pizza"]) == 0 and len(dict["Dessert"]) == 0:
        return "No products in the cart!"
    
    dict = (sorted(dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    
    for tuple in dict:
        products = sorted(tuple[1], key=lambda x: x)
        result.append(f'{tuple[0]}:')
        for product in products:
            result.append(f' - {product}')
            
    return "\n".join(result)
