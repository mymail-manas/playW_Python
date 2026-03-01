my_tuple=(1,2,3,"Apple",True)
print(my_tuple)
not_a_tuple=(5) #not a tuple
print(type(my_tuple))
print(type(not_a_tuple))

#Access nested tuple

print(my_tuple[3][0])

#Tuple with single item 50

tuple1=(50,)
#Swap tuple
tupleA=("ABC",False)
tupleB=(1.5,True)
tupleA,tupleB=tupleB,tupleA

print(tupleA)
print(tupleB)

#Copy specific elements
copyTuple=tupleA[1]
print(copyTuple)

#Slicing tuple
Sliced=my_tuple[1:3]
print(Sliced)

#Reverse print a tuple
print(my_tuple[::-1])

#Unpack
a,b,c,d,e=my_tuple
print(a,b,c,d)

mylist=[2,4,6,8]
mytuple=tuple(mylist)
print(my_tuple)


