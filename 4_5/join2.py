while True:
    greets_templ = input('Введите шаблон поздравления,'
                         'в шаблоне нужно использовать конструкцию '
                         '{name} и {age}: ')

    if '{name}' in greets_templ and '{age}' in greets_templ:
        break
    print(' Ошибка: отсутствует одна или две конструкции .')

print('Введите список имён (зааканчивается на end): ')

names_list = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')
ages = [int(i_num) for i_num in ages_str.split()]


for i_name in names_list:
    print(greets_templ.format(name=names_list[i_name], age=ages[i_name]))

people=[
    ' '.join([names_list[i_name], str(ages[i_name ])])
    for i_name in range(len(names_list))
]

people_str = ', '.join(people)
print('\nИменниники:', people_str)
