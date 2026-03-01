Employee={"Name":"Alice",
          "EmployeeID":234,
          "Department":"Engg"
          }

print(Employee["Name"])
print(Employee["Department"])


#WAP for list to dictionary
names=["Alice","Bob","Charlie"]
ages=[30,30,40]

age_dict={name:age for name,age in zip(names,ages)}
print(age_dict)

#Clear dictionary

#Employee.clear
print(Employee)

##Merge two dict itoone

merge_dict=Employee|age_dict
print(merge_dict)

#Count Char
print(names.count("Bob"))


