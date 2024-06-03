physics = int(input("Enter the marks: "))
chemistry = int(input("Enter the marks: "))
maths =int(input("Enter the marks: "))
biology =int(input("Enter the marks: "))
computer = int(input("Enter the marks: "))


total = physics+chemistry+maths+biology+computer
per=total/500*100

grade = ''
if per>=90:
  grade='A'
elif per>=80:
  grade='B'
elif per>=70:
  grade='C'
elif per>=60:
  grade='D'
elif per>=40:
  grade='E'
elif per<40:
  grade='F'
print(grade)