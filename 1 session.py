print(123)
print("123")
print (1+2)
print (1,"+",2)
print ("rafay")
rafay=1 #ye variable hai
print (rafay)
print (rafay+2)
print (rafay,"+",2)
num1=1
num2=2
print("addition",num1+num2)
print("subtraction",num1-num2)
print("multiplication",num1/num2)
print("division",num1*num2)
print("addition",num1+num2,"\nSubtraction",num1-num2) #"\n" = escape sequence
num1=22
num2=33
Addition=num1+num2
Subtraction=num1-num2
Division=num1/num2
Multiplication=num1*num2
print(Addition,Subtraction,Division,Multiplication)
# input () to input data
# by default input consider value as a string so we have to typecast
# =2, -> "2"
# for whole num = int()
# for decimal = float()
num1=int(input("enter your number 1:"))
num2=int(input("enter your number 2:"))
# ; is used to break line
addition=num1+num2;subtraction=num1-num2
print("this is addition:",addition,"\nthis is subtraction:",subtraction)

print("******MATRIC RESULTS SUMMARY******")


name=input("what is your name:")
DOB=input("what is your date of birth:")
English=int(input("your marks in english subject:"))
Maths=int(input("your marks in maths subject:"))
Urdu=int(input("your marks in urdu:"))
Science=int(input("your marks in Science:"))
physics=int(input("your marks in physics:"))

Addition=English+Maths+Urdu+Science+physics;per=(Addition/500)*100

if per>=80:
    Grade="A+"
elif per>=70:
    Grade="A"
elif per>=60:
    Grade="B"
elif per>=50:
    Grade="C"
else:
    Grade="fail"

print("your name is:",name,"\ndate of birth:",DOB,"\nObtained marks:",Addition,"\ntotal marks: 500","\nyour percentage is:",per,"\nyour grade is:",Grade)
# github.com?youexcellabs/python1
