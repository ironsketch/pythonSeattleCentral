from random import randint

def randNum():
    num = randint(1,128)
    return num

def main():
    print('Welcome to the number guessing game')
    print('Guess a natural number between 1 and 128.')
    print('Score starts at 100 and')
    print('decreases by 2 for every guess')
    print('Game is over when user guesses secret number')
    answer = randNum()
    guess = 129
    score = 100
    guessList = []
    while guess != answer:
        guess = eval(input('What is your guess? '))
        guessList.append(guess)
        if guess < answer:
            score -= 2
            print('Your guess is too low.')
        elif guess > answer:
            score -= 2
            print('Your guess is too high.')
    print()
    if len(guessList) == 1:
        print('MOTHER FUCKING YEAH ONE GUESS!')
    else:
        print('Try better asshole')
    print('Your score was,',score)
    print('The secret number was,', answer)
    print('You guessed,',len(guessList),'times.')

main()
