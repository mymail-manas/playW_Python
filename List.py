Cars=["Maruti","TATA","Mahindra"]
print(Cars[0])
Cars.append("Hyndai")
print(Cars)

Numbers=[1,2,3,4,5,6]
print(Numbers[1:4])

Numbers.reverse()
print(Numbers)
Numbers.sort()
print(Numbers)
Squares=[x**2 for x in range(4)]

print("Square numbers are:",Squares)


Cars.append("KA058899")
print("The stae of registration:", Cars[4][0])


print("the smalles numnber is",Numbers[0])
print("the largest number is:",Numbers[-1])

sum=0
for i in Numbers:
    sum+=i

print("Sum is:",sum)
size=len(Numbers)
avg=sum/size
print("Average is", avg)


numToCheck=0
# for i in Numbers:
      #occurance=0
#     for j in(i,):
#         if(Numbers[i]==Numbers[j]):
#             occurance+=1
#     #print("the number" + Numbers[i]+ "occured", occurance)


NewList=[1,2,4,5,2,1,"TEST","PY","TEST"]
occurance=NewList.count("TEST")
print(occurance)

    

CombinesLIst=Numbers+NewList
print(CombinesLIst)
Copy=CombinesLIst
print(Copy)