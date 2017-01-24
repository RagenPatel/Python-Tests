import random

numGuess = 0

number = random.randint(1,100)
print("Guess a number between 1 and 100")

while numGuess < 10:
    guess = int(input("Take a guess: "))

    numGuess+=1

    if(guess<number):
        a = number-guess
        if(a<5):
            print("Almost there! your guess is very close! too low")
        else:
            print("Number too low. Try again")

    if(guess>number):
        b = guess-number
        if(b<5):
            print("Almost there! your guess is very close! too high")
        else:
            print("Number too high. Try again")
    if(guess==number):
        print("You found the number "+{0}+"! You guessed my number in" +{1}+ "guesses!").format(name,numGuess)
        break
    
print("ur bad EleGiggle the number I had was"+ {0}).format(number)

    
