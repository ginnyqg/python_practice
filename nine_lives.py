import random

word_bank = ['apple', 'pizza', 'plane', 'shirt', 'teeth']
secret_word = random.choice(word_bank)

clue = list('?????')
heart_symbol = u'\u2764'

lives = 9
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    i = 0
    while i < len(secret_word):
        if guessed_letter == secret_word[i]:
            clue[i] = guessed_letter
        i += 1


while lives > 0:
    print(clue)
    print('Lives Left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lost a life.')
        lives -= 1


if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lose! The secret word was ' + secret_word)

