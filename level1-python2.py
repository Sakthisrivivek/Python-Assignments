input_string = input("Enter a string: ")
alphabets = 0
digits = 0

for char in input_string:
 if char.isalpha():
   alphabets += 1
 elif char.isdigit():
    digits += 1
            
print(f"Alphabets: {alphabets} & Number: {digits}")