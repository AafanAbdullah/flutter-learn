#Clever if / Ternary Operator it's also a conditional statements
#var>=(false_val, true_val)[<condition>]

age=int (input("Age : "))
vote= ("yes","No") [age<18]
print(vote)

sal=float(input("Salary : "))
tax=sal*(0.1,0.2) [sal<=50000]
print(tax)