def sum_of_digits(num):
    total = sum(int(digit) for digit in str(num))
    return total
num = int(input("Enter the number:"))
while num >= 10:
    num = sum_of_digits(num)
print("Final Output:", num)