#check if the player's guess is correct. This piece of code is
#before the input function because it needs to return right direction
#right after what user inputs there

def check_guess(guess, answer):
    #global variable ensures changes to the variable can be seen
    #throughout the whole program
    
    global score

    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again. ')
            attempt += 1
        if attempt == 3:
            print('The correct answer is ' + answer)

score = 0
print('Guess the animal!')
guess1 = input('Which bear lives at the North Pole? ')
#call the check_guess function to check if answer equals to guess
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal? ')
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))
