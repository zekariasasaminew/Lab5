'''
Name(s): Zekarias Asaminew 
CSC 201
Lab 5

This program plays the game of "Bagels" where the user tries to guess a number.
After each guess the user is given clues:
    "fermi" for correct digit in the correct position
    "pico" for correct digit is the wrong position
    "bagels" when every digit is incorrect
When the user guesses the number, the user is asked whether they want to play again.

Did you complete this lab file during the class period (yes or no)? No

I completed bagels_game.py without my partner from class.

Document any assistance you get if you complete the lab after the class period: I neither gave nor recieved
any assistance from anyone

'''
import random
NUM_DIGITS = 4    # number of digits in the number to be guessed

def intro():
    '''
    Introduces the game and explains the clues
    '''
    print('Welcome to Bagels!')
    print()
    print(f"I'm thinking of a {NUM_DIGITS} digit number. Each digit is between")
    print("1 and 9. Try to guess my number.")
    print()
    print("I'll say \"fermi\" for each correct digit in the correct position.")
    print("I'll say \"pico\" for each correct digit in the wrong position.")
    print("I'll say \"bagels\" if all of the digits are wrong.")
  
  
def get_clues(secret_string, guess_string):
    """
    Creates the clues for the user depending on how of the user's guess match
    the secret number to be guessed.
    
    Params:
    secret_string: The number to be guessed as a string
    guess_string: The number guessed by the user as a string
    
    Returns:
    a string of clues
    """
    # make copies so the parameter lists are not altered
    secret_list = list(secret_string)
    guess_list = list(guess_string)
    clues = ''
    
    # check for any correct digits in the correct position
    for index in range(NUM_DIGITS):
        if guess_list[index] == secret_list[index]:
            clues = clues + 'fermi '
            guess_list[index] = 'X'
            secret_list[index] = 'Y'
    
    # check for any correct digits in the wrong position
    for index in range(NUM_DIGITS):
        for index2 in range(NUM_DIGITS):
            if secret_list[index] == guess_list[index2]:
                clues = clues + 'pico '
                secret_list[index] = 'Y'
                guess_list[index2] = 'X'
   
    # if clues is '' then there were no correct digits
    if clues == '':
        clues = 'bagels'
        
    return clues


def get_secret_number():
    '''
    Randomly generates the number the user will guess stored as a string
    Each digit must be 1-9 inclusive
    
    Returns:
    the secret number as a string of digits each digit 1-9
    '''
    number = ''
    for num in range(NUM_DIGITS):
        number = number + str(random.randrange(1, 9))
        
    return number


def is_guess_valid(guess):
    """
    Determines if the guess is valid. To be valid, it must have NUM_DIGIT characters,
    each character must be a digit, and none of the characters can be a '0'.
    
    Param:
    guess (str): the guess made by the user
    Returns:
    True if the guess is valid; False otherwise
    """
    if '0' not in guess and guess.isdigit() and len(guess) == NUM_DIGITS:
        return True
    else:
        return False
    
    

def get_user_guess():
    '''
    This function repeatedly asks the user to make a guess until the guess is valid.
    
    Returns:
    The valid guess entered by the user as a string
    '''
    guess_user = input('Your guess? ')
    
    while not is_guess_valid(guess_user):
        print(f'You must enter {NUM_DIGITS} digits with no zeros. Try again.')
        guess_user = input('Your guess? ')
        
    return guess_user
    
    


def play_one_round():
    """
    Plays one round from generating the number to be guessed until the user guesses the number.
    When the user guesses the number, the number of guesses it took is displayed.
    """
    count = 1
    
    secret_number = get_secret_number()
    guess_user = get_user_guess()
    while guess_user != secret_number:
        print(get_clues(secret_number, guess_user))
        guess_user = get_user_guess()
        count += 1
    if count == 1:
        print(f'You got it in {count} guess.')
    else:
        print(f'You got it in {count} guesses.')

        
        
 
 
def play_again():
    """
    The function asks the user if they want to play again until
    the user answers 'y' or 'n', upper or lower case.
    
    Returns:
    the lowercase version of the user's y/n response lower case
    """
    que = input('Do you want to play again (y/n)? ')
    que = que.lower()
    
    while que != 'y' and que != 'n':
        print('You must answer y or n. Try again.')
        que = input('Do you want to play again (y/n)? ')
        que = que.lower()
    if que == 'y':
        play_one_round()
    elif que == 'n':
        return que
        
    
   
def main():
    intro()  
    response = 'y'
    while response =='y':
        print()
        play_one_round()
        print()
        response = play_again()
           
main()     
    
    
    
    
    
    