input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]
sum=0
for i in my_list[:]:
    sum+=i
average=sum/len(my_list)
my_list.sort()
max=my_list[len(my_list)-1]
min=my_list[0]
print(f"Average:{average}")
print(f"Maximum:{max}")
print(f"Minimum:{min}")