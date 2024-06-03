num = int(input("Enter the number: "))

sum=0
for i in range(1,num):
    if num%i==0:
     sum+=i

if sum==num:
    print("perfect number")
elif sum!=num:
    print("not a perfect number")