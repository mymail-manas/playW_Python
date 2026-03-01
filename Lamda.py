
from functools import reduce


Sum_lamda= lambda x,y:x+y
print(Sum_lamda(3,4))


Diff_lamda= lambda x,y:x-y
print(Diff_lamda(30,4))

Multi_lamda= lambda x,y:x*y
print(Multi_lamda(3,4))

Division_lamda= lambda x,y:x/y
print(Division_lamda(30,5))


#WAP to sort list of tuples using lamda

tuple1=[(1,4),(6,5),(3,4)]
tuple1.sort(key=lambda x:x[0])
print(tuple1)

#WAP to square and cube for every number in a given list

list2=[2,4,6,5,7]
Square_Lamda=list(map(lambda x:x**2,list2))
print(Square_Lamda)

Cube_Lamda=list(map(lambda x:x**3,list2))
print(Cube_Lamda)

#WAP to count then number of even and odd numbers in given array of integers

Even_Lamda=list(filter(lambda x:x%2==0,list2))
print(Even_Lamda)

Odd_Lamda=list(filter(lambda x:x%2!=0,list2))
print(Odd_Lamda)

#WAP to add two given list using map and lamda
list3=[100,200,300]
Combined_Lamda=lambda list2,list3: list2+list3
print(Combined_Lamda(list2,list3))

Map_combined_lambda=list(map(lambda a,b:a+b,list2,list3))
print(Map_combined_lambda)

#WAP using lamda function with reduce function
num=[1,3,4,5]
Result=reduce(lambda x,y:x*y,num)
print(Result)

#