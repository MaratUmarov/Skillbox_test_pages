import random

left_border = int(input('Левая граница: '))
right_border = int(input('Правая граница: '))
rand_num = [random.randint(left_border, right_border) for _ in range(left_border, right_border)]
even_num_list = [rand_num[i_num] for i_num in range(len(rand_num)) if rand_num[i_num] % 2 ==0  ]
print(rand_num)
print(even_num_list)
