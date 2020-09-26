
list=[0,1]
a=list[0] # assigning a value of list item with index 0
a_i=list.index(0) #a_i assigned value 0
b=list[1]# assigning b value of list item with index 1
b_i=list.index(1)#b_i assigned value 1
for x in range(11):
    list.append(a+b) #for each iteration a+b is added to list
    a_i+=1 #a_i is incremented
    a=list[a_i] # a now assigned the list item with new index incremented by 1
    b_i+=1 #b_i is incremented
    b=list[b_i] # b now assigned the list item with new index incremented by 1


print(*list[0:],sep=",", end=",.......")   #list items are printed separated with comma 

