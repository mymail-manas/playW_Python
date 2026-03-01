
#WAP to check the eligibility criteria for voting

age=int(input("Enter age"))

# if age>=18:
#     print("Eligible for voting")

# else:
#     print("Not eligible")

 #WAP to check the eliginility crteria to participate in election

# if age>=21:
#     print("Eligible for election")
# else:
#     print("Not eligible for election")

if age>=21 and age >=18:
    print("Eligible for both election and voting")
elif age>=18 and age<21:
    print("Eligible for voting but not for election")
else:
    print("Not eligible for both")
19