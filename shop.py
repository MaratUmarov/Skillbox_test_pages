original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [0 if original_prices[i_price] < 0 else original_prices[i_price] for i_price in
              range(len(original_prices))]
print(new_prices)
