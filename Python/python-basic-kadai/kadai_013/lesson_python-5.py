def total_price(price, tax):
  tax_amount = price*(tax / 100)
  total = price + tax_amount
  
  print(f"{total}円")
  
total_price(1200, 10)