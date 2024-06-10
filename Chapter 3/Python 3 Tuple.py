tup = (2,5,6,7)
print(tup[1:3])
print(type(tup))

#Returns index of first occurrance
tup = (6,7,8,9)
print(tup.index(8))

#Counts total occurrance
tup = (2,2,3,2,1)
print(tup.count(2))

#practice question
#To ask the user to enter names of their 3 favourite movies & store them in a list
'''movies =[]
movies.append(input("Enter first movie name: "))
movies.append(input("Enter Second movie name: "))
movies.append(input("Enter third movie name: "))

print(movies)
'''
Movies =[]
mov1 = input("Enter first name")
mov2 = input("Enter the second name")
mov3 = input("Enter the third name")

Movies.append(mov1)
Movies.append(mov2)
Movies.append(mov3)

print(Movies)

#To check if a list contains a palindrome of elements. 

list1 = [1,2,3,2,1]


copyl1 = list1.copy()
copyl1.reverse()

if copyl1 == list1:
    print("List is Palindrome")
else:
    print("Not Palindrome")    

#Write a  program of students with the "A"grade in the following tuple.
               #"C","D","A","A","B","B","A"
Grades = ("C","D","A","A","B","B","A")
print(Grades.count("A"))                   

#Store the above valus in a list & sort them from "A" to "D".
grade = ["C","A","B","D","F","B"]
grade.sort()
print(grade)