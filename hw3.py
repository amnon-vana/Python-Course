matrix = [[5,5,5],[1,-9,44],[-20,10,5]]
sum = 0
for num in matrix[0]:
  sum += num
min_sum_num = sum
min_sum_list = matrix[0]

for mylist in matrix[1:]:
  sum = 0
  for num in mylist:
    sum += num
  if sum < min_sum_num:
    min_sum_num = sum
    min_sum_list = mylist
print("Min sum is: {} of list {}".format(min_sum_num,min_sum_list))
