dict1={"name":"Tejas",
       "Empid":234,
       "City":"Hyd"
       }
print(dict1)

dict2={"name":"Manash",
       "Empid":235,
       "City":"BLR"
       }
print(dict2)

Nesteddict={"Teja":dict1,
            "Manash":dict2
}

print(Nesteddict["Manash"]["City"])

#Modify nested dict
Nesteddict["Manash"]["City"]="Delhi"
print(Nesteddict["Manash"]["City"])

employees=["Teja","Manash"]
default={"designation":"Dev",
         "Salary":50000
         }
thisdict = dict.fromkeys(employees,default)
print(thisdict)

