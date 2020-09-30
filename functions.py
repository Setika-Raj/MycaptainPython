string=input("PLEASE ENTER A STRING: ")
output={}
for i in string:
        if i in output:
            output[i]+=1
        else:
            output[i]=1


print(*[f'{key} {val}' for (key,val) in sorted(output.items(),key=lambda item: item[1],reverse=True)],sep='\n')    
        
