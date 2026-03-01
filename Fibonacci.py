list=[]
for i in range(0,10):
    if(i>2):
        k=list[i-1]+list[i-2]
    else:
        k=i
    list.append(k)

print(list)
