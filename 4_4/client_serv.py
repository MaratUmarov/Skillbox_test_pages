nums = [x for x in range(1, 101) if x % 10 == 0]
new_nums = nums[:]
new_nums[3] = 0

print(new_nums[2:8])
