Student ={
    "name" : "Aafan",
    "subject" : {
        "phy" : 78,
        " Chem" : 67,
        "CS" : 95,

    }
}

#Nested Dictionary
print(Student["subject"]["CS"])

                                               #Dictionary methods
#KEYS() RETURN ALL KEYS
print(list(Student.keys()))
print(len(Student))
print(len(list(Student.keys())))

#VALUES() RETURN ALL VALUES
print(Student.values())
print(list(Student.values()))

#ITEMS() RETURN ALL (KEY,VAL) PAIRS AS TUPLE

print(Student.items())
print(list(Student.items()))

pairs= list(Student.items())
print(pairs[0]) # USING TUPLE

#GET() RETURN THE KEY ACCORDING TO THE VALUE
#print(Student["name2"]) #error
#print(Student.get("name2")) #given null

#UPDATE() INSERT THE SPECIFIED ITEMS TO THE DICTIONARY
new_dict={"City" : "Karachi", "Age" : 20}
#Student.update({"City" : "Karachi"})
Student.update(new_dict)
print(Student)