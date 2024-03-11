
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
flattened_list = [i_item for secondary_sub in [item for sublist in nice_list for item in sublist] for i_item in secondary_sub]
print(flattened_list)