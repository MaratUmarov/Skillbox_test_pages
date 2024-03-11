while True:
    greets_templ = input('Введите шаблон поздравления,'
                         'в шаблоне нужно использовать конструкцию {name}: ')

    if '{name}' in greets_templ:
        break
    print(' Ошибка: отсутствует конструкция {name}.')

print('Введите список имён (зааканчивается на end): ')
names_list = []
while True:
    name = input('Имя: ')
    if name != 'end':
        names_list.append(name)
    else:
        break
for i_name in names_list:
    print(greets_templ.format(name=i_name))
