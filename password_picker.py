#import modules

import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat',
              'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white',
              'fluffy', 'proud', 'brave']

nouns = ['apple', 'hammer', 'ball', 'toaster',
         'goat', 'dragon', 'dinosaur', 'duck', 'panda']

print('Welcome to password Picker!')


#unlimited number of runs
while True:

    #for limited number of runs
    #indentation makes it a subblock of returning 3 passwords at a time
    for num in range(3):
        
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) +special_char

        # %s substitute the value after next %
        print('Your new password is: %s' %password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break

