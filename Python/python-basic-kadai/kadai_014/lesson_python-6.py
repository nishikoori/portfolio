price1 = 10050
price2 = 20050

def total():
    tax = 1.1
    return price1 + price2 * tax

amount = round(total())

print (f"{amount}円")
