import math

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

gcd = math.gcd(x, y)
lcm = (x * y) // gcd

print(f"LCM of {x} and {y} is: {lcm}")