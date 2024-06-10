#Conditional Statement

A= int(input("A= : "))
G= input("M/F : ")
if((A ==1 or A==2) and G =="M"):
    print("Fees is 100")
elif(A==3 or A==4 and G =="F"):
    print("Fees is 200")
elif(A==5 and G== "M"):
    print("Fees is 300")
else:
    print("NO fees")            
