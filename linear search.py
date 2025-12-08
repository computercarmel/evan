l1=eval(input("enter list elements"))
length=len(l1)
element=int(input("enter the element to be searched"))
for i in range(0,length,+1):
  if element ==l1[i]:
            print(element,'found at index',i)
            break
        
else:
    print(element,"not present in the given list")
            
