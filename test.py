import random
squad_1=[random.randint(50,80) for _ in range(10)]
squad_2=[random.randint(30,60) for _ in range(10)]
squad_3=[('Погиб' if squad_1[i_damage]+squad_2[i_damage]>100 else 'Выжил') for i_damage in range(10)]

print(f'Урон первого отряда: {squad_1}')
print(f'Урон второго отряда: {squad_2}')
print(f'Состояние третьего отряда: {squad_3}')

