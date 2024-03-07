import random

original_prices = [random.randint(-14, 10) for _ in range(10)]

new_prices = [0 if original_prices[i_price] < 0 else original_prices[i_price] for i_price in
              range(len(original_prices))]

print(original_prices)
print(new_prices)
print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))
