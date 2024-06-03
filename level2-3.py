input_string = input("Enter a list of integers separated by spaces: ")
my_list = [int(x) for x in input_string.split()]
k = int(input("Enter the k value: "))
freq = {}
c = 0
    
for num in my_list:
        x = k - num
        if x in freq:
            c += freq[x]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
print(c)