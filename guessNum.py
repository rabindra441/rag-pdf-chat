# This is a guess the number game
import random
print('Whats Your Name?')
name = input()
print('Hello, ' + name + ', I am thinking a number between 1 to 20')
secretNumber = random.randint(1, 20)
for guessNumber in range(1, 7): 
        print('Guess your number')
        guess = int(input())

        if guess < secretNumber:
                print('Your guess number is too low')
        elif guess > secretNumber:
                print('Your guess number is too high')
        else:
                print('Congratulations, '+name+' !You guessed it!')
                break


if guess == secretNumber:
        print('Good job ' + name + ', You guessed my number after ' + str(guessNumber) + ' tries.')
else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

        

