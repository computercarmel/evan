fact=1
n=int(input("enter the number"))
print("the factorial of",n,"is")
for i in range(1,n+1):
    fact*=i
print(fact)
