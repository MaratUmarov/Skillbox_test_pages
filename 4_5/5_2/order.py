name = input('Имя: ')
order = int(input('Номер заказа: '))

order_print = 'Здравствуйте , {recipient}! Ваш номер заказа: {recip_order} Приятного дня!'.format(recipient=name,
                                                                                                  recip_order=order)
print(order_print)
