input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]
d=int(input("enter the d value:"))
x=len(my_list)-d
slice1 = my_list[x:]
slice2 = my_list[:x]
res = slice1 + slice2
print(res)