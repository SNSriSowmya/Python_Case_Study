#importing random module

from random import randint

"""Initializing two variables min_value and max_value with lowest and 
    highest number of dice i.e. 1 and 6"""

min_value=1
max_value=6

roll_again="yes"

while roll_again.lower()=="yes" or roll_again.lower()=="y":
   random_number=randint(min_value,max_value)
   print("The Random Number is:",random_number)

   #Asking the user if they want to roll the dice again?

   roll_again=input("Do you want to roll the dice again yes/no ?")

print("Thanks for playing!")