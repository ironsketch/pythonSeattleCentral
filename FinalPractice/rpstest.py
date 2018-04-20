def meatTurn():
    play = ''
    while play != 'paper' or play != 'rock' or play != 'scissors':
        play = input('Type rock paper or scissors ')
        play = play.lower()
    return play

print(meatTurn())
