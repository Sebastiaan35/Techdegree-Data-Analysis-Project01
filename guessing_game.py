"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
Personal note: I'm always using the plural, even when refering to a singular
"""
import random
import statistics
import os
import time
MIN_GUESS = 0
MAX_GUESS = 100


def start_game():
    """
    This is the main game function from which different games can be launched
    """
    # clear screen
    os.system('cls')
    #   Welcome message
    print("Hi - Welcome to Sebastiaan's guessing game")
    high_score = 999
    play_again_bool = True
    number_of_guesses_all = []

    #   Game loop allowing for multiple games to be played
    while play_again_bool:
        #   The high score is shown before starting the game
        print_high_score(high_score)
        nr_of_guesses_game_instance = game_instance()
        #   Attempts are stored in a list.
        number_of_guesses_all.append(nr_of_guesses_game_instance)
        number_of_guesses_all.sort()
        high_score = min(number_of_guesses_all)
    #   Statistics feedback
        print('\n' + 22*'*' + ' Statistics ' + 22*'*' + '\n')
    #     a. Number of guesses to finish the latest game
        print(f'Wow, it only took you {nr_of_guesses_game_instance} guess(es) \
to figure out the right number!')
    #     b. The mean of attempts list
        print(f'On average it took you {statistics.mean(number_of_guesses_all)} try/tries \
to get the right number.')
    #     c. The median of attempts list
        print(f'The median of all games is {statistics.median(number_of_guesses_all)} try/tries.')
    #     d. The mode attempts list
        multimode = statistics.multimode(number_of_guesses_all)
        mode = multimode[0]
        print(f'The mode of all games is {mode} try/tries.')
        print(f'{mode} try/tries occured {number_of_guesses_all.count(mode)} time(s).')
        if len(multimode)>1:
            print(f'Btw, there are multiple modes: {multimode}')
        print('\n' + 55*'*' + '\n')
        play_again_bool = play_again()
    #    Goodbye message at end of game
    print(f'The fastest attempt of all games was only {high_score} try/tries. \n'
            'This game will now quit. Thank you for playing and goodbye.')


def game_instance():
    """
    This is a game instance function responsible for one single game
    """
    #   Random number between (and including) MIN_GUESS and MAX_GUESS to be guessed
    correct_answer = random.randint(MIN_GUESS, MAX_GUESS)
    number_of_guesses_instance = 0
    #   Loop until the guess matches the "correct_answer"
    while True:
        # Only include guesses that are integers within specified range
        user_guess = valid_user_guess()
        number_of_guesses_instance += 1
        if user_guess > correct_answer:
            print("It's lower")
        elif user_guess < correct_answer:
            print("It's higher")
        # A correct guess provides a message of congratulations and returns the number of guesses
        else:
            print("\033[92m✔\033[0m Well done! You got it! :)")
            return number_of_guesses_instance


def print_high_score(high_score):
    """
    This function provides feedback to the user about the high score 
    """
    if high_score == 999:
        print('The high score is still empty')
    elif high_score == 1:
        print('The record is guessing the number straight away. Can you do that again?')
    else:
        print(f'The fastest guess needed only {high_score} tries. Can you beat it?')


def play_again():
    """
    This function determines whether a player would like to play again
    """
    while True:
        answer = input('Would you like to play again? (y/n): ')
        if not answer:
            print('That was not a valid answer. Please type "Y" for yes or "N" for no.')
        elif not (answer.lower()[0] == 'y' or answer.lower()[0] == 'n'):
            print('That was not a valid answer. Please type "Y" for yes or "N" for no.')
        elif answer.lower()[0] == 'y':
            return True
        elif answer.lower()[0] == 'n':
            return False


def valid_user_guess():
    """
    This function is responsible for gathering one valid guess
    i.e. a whole number, within the specified range.
    """
    while True:
        try:
            user_guess = int(input(f"Please guess a whole number that is \
anywhere between and including {MIN_GUESS} to {MAX_GUESS}: "))
            if user_guess>MAX_GUESS or user_guess<MIN_GUESS:
                print('That number is not within the specified range. Please try again.')
            else:
                return user_guess
        except ValueError:
            print('❌ That was not a whole number. Please try again.')

# Game start
if MAX_GUESS <= MIN_GUESS:
    print("Adjust the boundaries of this game.")
else:
    start_game()
time.sleep(3)
