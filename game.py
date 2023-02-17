# this program demonstrates a guessing game
# 1 get user name and input
# using while loop get user number
# 2 generate random number
# 3 using while loop(check if user number=random number)

import random

name=input("enter name: ")
print("hello "+ name +"!")
random_number=random.randint(1,10)
counter=0
while counter<5:
   choice=input("try your luck??(y/n): ")
   if choice.casefold()=="n":
    break
      
   else:
    number=eval(input("enter number: "))

    counter+=1

    if number<random_number:
        print("guess is too low")
    elif number>random_number:
        print("guess is high")
    elif number==random_number:
        print("you won"+"!")    
        break

   