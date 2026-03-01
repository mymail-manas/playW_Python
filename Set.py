setfruit={"apple","banana","mango","orange"}
setfruit.add("grape")
print(setfruit)
setfruit.remove("apple")
print(setfruit)
setfruit.discard("mango")
print(setfruit)

#Union of sets,intersection,diff

Set2fruit={"banana","mango","orange","Jackfruit"}

union_Set=setfruit|Set2fruit
print(union_Set)
intersection_Set= setfruit&Set2fruit
print(intersection_Set)
diffSet=setfruit-Set2fruit
print(diffSet)
#Add a list Set update diff
list=[1,2,3]
setfruit.update(list)
print(setfruit)

L1=[1,2]
S=set(L1)
print(S)

#symmetric diff
symmetricDiff=setfruit.symmetric_difference(Set2fruit)
print(symmetricDiff)

#Difference update
S1={1,2,3}
S2={2,3,4}
S1.difference_update(S2)
print(S1)
S1.difference_update({3})
print(S1)

#Subset check
subSet={10,20}
MainSet={10,20,30,40}
isSubset=subSet.issubset(MainSet)
print(isSubset)
#Superset
isSuperSet=MainSet.issuperset(subSet)
print(isSuperSet)