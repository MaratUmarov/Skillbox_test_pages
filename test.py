def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


price_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

prices_first = [get_higher_price(first_percent, i_price) for i_price in price_now]
prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]

print(f'Сумма цен за каждый год: {round(sum(price_now),2), round(sum(prices_first),2),round(sum(prices_second),2)}')

