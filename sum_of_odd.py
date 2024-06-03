num = int(input("Enter the number: "))
num1 = int(input("Enter the number: "))
sum=0
for i in range(num,num1):
    if i%2==1:
        sum+=i
print(sum)