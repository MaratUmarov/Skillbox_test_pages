str = input('Введите строку: ')

additional_str = input('Введите дополнительный символ: ')
doubbled_str_list=[letter*2 for letter in str]
gluing_doubbled_str=[dub+additional_str for dub in doubbled_str_list ]

print(f'Список удвоенных символов: {doubbled_str_list}')
print(f'Склейка с дополнительным символом: {gluing_doubbled_str}')
