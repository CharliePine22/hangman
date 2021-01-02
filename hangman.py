import random
import sys

game_words = ['pear', 'RJCT', 'Ryan', 'Superman', 'Cake', 'Hangman', 'Batman', 'magic']

game_word = random.randint(0, len(game_words) - 1)
secret_word = game_words[game_word].lower()


def start_game():
    """
    HANG
    ____
    MAN
    """

    print('Welcome to Hangman!\n')

    print(' O ')
    print('\|/')
    print(' |')
    print(" /\\\n")

    game_active = True

    while game_active:
        print('To start type "p" or "play" or to quit type "q" or "quit"')
        player_choice = input('What would you like to do? ').lower()

        if player_choice == 'p' or player_choice == 'play':
            print('Play!!\n\n')
            game_logic()
            break

        elif player_choice == 'q' or player_choice == 'quit':
            print('See ya later!')
            sys.quit()

        else:
            print('Please type either start or quit!')
            continue


def game_logic():
    """Create the logic to make the game playable"""

    print('You have 6 guesses to guess the secret word!\n')

    used_letters = []
    correct_letters = []
    attempted_word = []
    result = []
    guesses = 6

    for i in secret_word:
        attempted_word.append('X')

    print(attempted_word)
    print('\n')

    # Print length of word to player
    print(f'The secret word has {len(secret_word)} letters!')

    while guesses > 0:
        print('\n')
        print(f"SECRET WORD: {attempted_word}")
        print(f'INCORRECT GUESSES: {used_letters}')
        guess = input('Guess a letter! ')
        print('\n')

        # quit the game
        if guess == 'quit':
            break

        # check to see if its one letter
        if len(guess) > 1:
            print('Please choose only one letter!')
            continue
        elif (len(guess) > 1) and (guess != secret_word) and (len(guess == len(secret_word))):
            print('Good try! Incorrect!')
            guesses -= 1
            continue

        # If the user has made a correct guess
        if guess in used_letters:
            print("\nYou've already guessed that letter! Guess again!")
            print(used_letters)
            print(f'You have {guesses} guesses left!\n')
            continue
        # If the user has made an incorrect guess
        elif guess not in used_letters:
            if guess in secret_word:
                print('Correct!')
                result.append(guess)
                correct_letters.append(guess)
                attempted_word[secret_word.index(guess)] = guess

            # Win check
            if result == attempted_word:
                print('YOU WIN!!!')
                print(f'The secret word was: {secret_word}!')
                replay = True
                while replay:
                    play_again = input('Would you like to play again? ').lower()
                    if play_again == 'yes':
                        print("Let's play!")
                        game_logic()
                    elif play_again == 'no':
                        print('Thanks for playing!')
                        sys.quit()
                    else:
                        print('Please choose "yes" or "no"!')

                # Try to check for words with more than one occurence of a letter
                for i in secret_word:
                    if secret_word.count(guess) > 1:
                        attempted_word[secret_word.index(guess)] = guess
                print(f'You have {guesses} guesses left!')
                continue
            else:
                print('Incorrect!')
                used_letters.append(guess)
                guesses -= 1
                print(f'\nYou have {guesses} guesses left!')
                continue


start_game()