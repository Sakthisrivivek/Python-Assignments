input_string = input("Enter a string: ")
c = 0
for i in input_string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or \
       i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        c += 1

print(c)