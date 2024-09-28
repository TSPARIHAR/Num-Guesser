import random
randomNumber=random.randint(1,100)
        
guess=None
guesses=0
while(True):
    print("press e to exit") 
    guess=input("Enter your guess:")
   
    
    if guess.lower()=="e":
        print("Exit")
        break
    try:
        guess = int(guess)
    except Exception:
        print("ivalid input")
        continue
    
    guesses +=1    
    
    if (guess<randomNumber):
        print("higher")
    elif(guess>randomNumber):
        print("lower")
    else:
        print("You guessed it")
        print(f"You took {guesses} guesses")
        guesses = 0
        randomNumber = random.randint(1,100)  # Generate new random number
        print("New number generated. Guess again!")
