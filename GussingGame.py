import random 
number = random.randint(1,10)
  
guess = int (input("enter your guess"))

if (guess == number):
    print (" you guessed the number correctly")
else :
    print ("you guessed the number incorrecty")
    
print ("The random number was", number)



    
    
