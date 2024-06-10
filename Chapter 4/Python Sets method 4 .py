                                    # SET METHOD
# SETS ARE MUTABLE 
#THE ELEMENTS OF SET IS IMMUTABLE
# WE CAN PASS TUPLE IN IT BUT NOT DICTIONARY AND LIST


  #ADD() ADDS AN ELEMENT
collection = set()
collection.add(1)
collection.add(2)
collection.add("Apna College") #passing string
collection.add((1,2,3)) #passing tuple

collection.remove(1) #REMOVE() REMOVE THE ELEMENT

collection.clear() #CLEAR() EMPITIES THE SET
print(len(collection))
 
 #POP() POP A RANDOM VALUE.
collect = {"HELLO"," AAFAN ABDULLAH", "WORLD", "PYHTON","COLLEGE"} 
print(collect.pop())
print(collect.pop())


#UNION() COMBINE BOTH SET VALUES & RETURNS NOW
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1)
print(set2)

print(set1.intersection(set2))





                                    #PRACTICE QUESTIONS

 #STORE SOME WORDS EANINGS IN PYTHON DICTIONARY                                   
dictionary = {
  "Table" :["a piece of furniture","list of facts and figure"],
   "Cat"  :["A small Animal"],
}
print(dictionary)

#YOU'RE GIVEN A LIST OF SUBJECTS. ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT.
# HOW MANY CLASSROOMS ARE NEEDED BY ALL STUDENTS.

subject = {"python","Java","C++","python","Javascript","Java","python","Java","C++","C"}

print(len(subject))

#ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY.
#START WITH AN EMPTY DICTIONARY & ADD ONE BY ONE. USE SUBJECT NAME AS KEY & MARKS AS VALUE.

marks = {}

a =int(input("Enter phy : "))
b =int(input("Enter CS : "))
c =int(input("Enter Math"))
marks.update({"phy": a,"CS" : b ,"Math": c,})

print(marks)

#Figure out a way to store 9 & 9.0 as seperate values in the set.
#(You can take help of built-in data types)
