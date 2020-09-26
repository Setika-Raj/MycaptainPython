list1=[12,-7,5,64,-14]
output1=[] # creating an empty list
for number in list1:
    if number>0:
        output1.append(number) # for each iteration ,if the list item is a positive number ,its gets added to the output1 list
        
print(*output1,sep=",")# output1 list items are printed separated with comma

list2=[12,14,-95,3]
output2=[]# creating an empty list
for number in list2:
    if number>0:
        output2.append(number) # for each iteration ,if the list item is a positive number ,its gets added to the output2 list
        
print(output2)#output2 list is printed

