#Nesting
age = 94
if age >= 18:
    if age >= 80:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")
 
    #practice questions
# to check a number entrerd by the user is odd and even.
num= int(input("Enter a number"))
rem = num%2 
if rem ==0:
   print("Number is Even")
else:
   print("Number is Odd")

# to find a greatest of 3 numbers entered by the user.
a = int(input("enter first number: "))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
d = int(input("Enter fourth number"))
if a >= b and a >= c and a >= d:
   print("First is the greatest number",a)
elif b >= a and b >= c and b >= d:
   print("Second is the greatest number",b)
elif c >= a and c >= b and c >=d:
   print("Third is the greatest number",c)
else:
   print("Fourth is the greatest number",d)   

#to check if a number is a multiple of 7 or not
num = int(input("enter a number"))
rem = num%7
if rem==0:
   print(num,"is the multiple of seven")
else:
   print("It is not a multiple of 7")   
   


