def is_palidrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [1, 2, 3, 4, 5]
answer = []

for i_nums in range(0, len(nums)):
    if is_palidrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break
print("исходный список :", nums)
print('Нужно чисел для палиндрома: ', len(answer))
print('Спсок этих чисел: ', answer)
