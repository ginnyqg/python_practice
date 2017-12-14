import random

word_bank = ['apple', 'pizza', 'plane', 'banana', 'teeth', 'glasses']
secret_word = random.choice(word_bank)

heart_symbol = u'\u2764'

guessed_word_correctly = False


clue = []
i = 0
while i < len(secret_word):
    clue.append('?')
    i += 1

unknown_letters = len(secret_word)

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    i = 0
    while i < len(secret_word):
        if guessed_letter == secret_word[i]:
            clue[i] = guessed_letter
            unknown_letters -= 1
        i += 1
    return unknown_letters


difficulty = input('Choose difficulty level (type 1, 2, or 3): \n 1 Easy \n 2 Normal \n 3 Hard \n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
if difficulty == 2:
    lives = 9
else:
    lives = 6

   
while lives > 0:
    print(clue)
    print('Lives Left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrect. You lost a life.')
        lives -= 1
        
    if unknown_letters == 0:
        guessed_word_correctly = True
        break


if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lose! The secret word was ' + secret_word)

