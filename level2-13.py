input_string = input("Enter a string: ")
input_char = input("Enter a character: ")
res = lambda s, c: s.startswith(c)
result=res(input_string,input_char)
print(result)


