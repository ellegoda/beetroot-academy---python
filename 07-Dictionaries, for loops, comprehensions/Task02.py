stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_stock_price(stock, prices):
    total_stock_price = 0
    for item in stock:
        stock_count = stock.get(item)
        item_price = prices.get(item)
        total_stock_price += stock_count * item_price
    return total_stock_price

print("Total Stock Prices : ", total_stock_price(stock, prices))
