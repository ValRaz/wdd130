import random

play_again = True
name = input('What is your name?\n')

while play_again:

    word_list =['ATE','HOG','PAT','FOUR','THIN','REND','HELLO','CRATE','GOURD','PURPLE','KNIGHT','TUESDAY','MUSEUM','GAFFERS', 'UMPIRES' ]
    #creates a list to pull the secret word for the game from

    secret_word = random.choice(word_list)
    #chooses a secret word for the game randomly from the stored list

    tries = 0
    #sets up an attempt counter variable

    print('\n Your hint is:', end='')
    for character in secret_word:
        print('_', end='')
    #loops through the secret word to provide the initial hint

    word_guess = input(f'\n\nWhat is your guess?\n')
    #requests first guess from end user

    if len(word_guess) != len(secret_word):
        print(f'\nThe word is not the right length!')
    else:
        exit
    #checks that the end user's input is the correct length for the word being guessed.
    
    while word_guess.upper() != secret_word:

        print(f'\nYou\'re hint is:', end='')

        for word, secret in zip(word_guess, secret_word):
            if word.upper() == secret:
                print(word.upper(), end='')
            elif word.upper() in secret_word:
                print(word.lower(), end='')
            else:
                print('_', end='')
        word_guess = input(f'\n What is your guess?\n')
        tries += 1
    #checks input guess against secret word and loops for incorrect guesses
    # iterates a hint with _ for incorrect letters, upercase for correct letter
    # in correct place and lowercase for correct letter in incorrect place.  
    #increases value of tries per guess.
    
    print(f'Congratulations you\'ve guessed it!\n It took you {tries + 1} tries.')

    play_again = input(f'Would you like to play again (yes/no)?\n')
    if play_again == 'no':
        play_again = False

print(f'Thank you for playing. Have a great day {name}!')
exit
#Displays the number of tries taken to get the correct word, and allows the end user
# to choose if they want to play again, and responds accordingly.