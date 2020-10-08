low=900
up=1000
print("Prime numbers between ",low," and ",up,"are :") 
for n in range(low,up+1):
      for i in range(2,n):
        if n%i==0:
            break
      else:
        print(n)
