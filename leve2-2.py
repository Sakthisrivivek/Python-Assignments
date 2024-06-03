input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]
res=list(set(my_list))
print(res)