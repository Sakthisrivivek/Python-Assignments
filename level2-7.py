input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]

list_length = len(my_list)
sum_median = 0
my_list.sort()
if list_length % 2 == 0:
    sum_median = (my_list[list_length // 2] + my_list[list_length // 2 - 1]) / 2
else:
    sum_median = my_list[list_length // 2]

print("Median:", sum_median)