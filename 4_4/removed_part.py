import random

amount = int(input('кол-во чисел :'))
nums = [random.randint(1, 100) for _ in range(amount) ]
print(nums)
a_ind, b_ind = random.randint(1, amount), random.randint(1, amount)

if a_ind < b_ind:
    del nums[a_ind:b_ind]


print(f'a_ind{a_ind}')
print(f'b_ind{b_ind}')
print(nums)
