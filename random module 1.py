import random
n=random.randint(1,6)
guess=int(input("guess a number between 1 to 6"))

if n==guess:
  print("congrats you won the lottery")

else:
    print("sorry try again ---- the lucky number was",n)

          
          
