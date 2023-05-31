def shopping_list(budget, **dicts):
    if budget < 100:
        return f'You do not have enough budget.'
    basket = []
    return_list = []
    for product in dicts.keys():
        current_price = dicts[product][0]
        quantity = dicts[product][1]
        current_total_price = current_price * quantity
        if budget - current_total_price >= 0:
            budget -= current_total_price
            basket.append(product)
            return_list.append(f'You bought {product} for {current_total_price:.2f} leva.')
        if len(return_list) == 5:
            return "\n".join(return_list)
    return "\n".join(return_list)
