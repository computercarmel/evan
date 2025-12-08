import random
L=[]
l=int(input('enter the lower limit'))

h=int(input('enter the higher limit'))
while(1):
    a=random.randrange(l,h+1)
    if(a%2==0):
        L.append(a)
    if(len(L)==5):
     break
print(L)
