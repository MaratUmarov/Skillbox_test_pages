left_border=int(input('Левая граница: '))
right_border=int(input('Правая граница: '))
cubes_list=[x**3 for x in range(left_border,right_border+1)]
squares_list=[x**2 for x in range(left_border,right_border+1)]
print(f'Список кубов чисел в диапазоне от {left_border} до {right_border}: {cubes_list}')
print(f'Список квадратов чисел в диапазоне от {left_border} до {right_border}: {squares_list}')
