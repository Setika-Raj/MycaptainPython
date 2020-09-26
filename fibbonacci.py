
list=[0,1]
a=list[0]
a_i=list.index(0)
b=list[1]
b_i=list.index(1)
for x in range(11):
    list.append(a+b)
    a_i+=1
    a=list[a_i]
    b_i+=1
    b=list[b_i]


print(*list[0:],sep=",", end=",.......")    

