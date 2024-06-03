input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]
input_string1 = input("Enter another list of integers separated by spaces: ")
my_list1 = [int(x) for x in input_string1.split()]
res = [value for value in my_list if value in my_list1]
print("Common elements:", res)