# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    count = 0
    for i in secret_word:
        if i in letters_guessed:
        # if letters_guessed[count] == i:
            count+=1
        else:
            break

    if count == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    for i in secret_word:
        if i in letters_guessed:
            print (i)
        else:
            print("-")




def get_available_letters(letters_guessed):
    alphabet = string.ascii_lowercase
    guess_string=''
    for i in alphabet:
        if i not in letters_guessed:
            guess_string += i
    return guess_string
#

def hangman(secret_word):
    print(f'''
Welcome to the game Hangman!
I am thinking of a word that is {len(secret_word)} letters long.
You have 6 guesses in total
Available letters {string.ascii_lowercase}''')
    letters_guessed=[]
    guess=6
    warning=3
    i=0
    while guess > 0 and warning > 0 :
        letters_guessed+=input("please guess a letter\n")
        get_guessed_word(secret_word, letters_guessed)
        # print(f"You have {count} guesses in total")
        # print(f"available letters {get_available_letters(letters_guessed)}")

        if letters_guessed[i] in secret_word and not is_word_guessed(secret_word, letters_guessed) and letters_guessed[i].isalpha() :
            print(f"Great,You have {guess} guesses in left")
            print(f"available letters {get_available_letters(letters_guessed)}")
        elif not letters_guessed[i].isalpha():
            warning = warning - 1
            print(f"Oops! That is not a valid letter. You have {warning} warnings left")
        else:
            # print("wrong answer")
            # print(letters_guessed)
            # print("try again")
            guess = guess-1
            print(f"Oops, You have {guess} guesses left")
            print(f"available letters {get_available_letters(letters_guessed)}")
            # print(count)
        i+=1
        print("---------")
        if is_word_guessed(secret_word, letters_guessed):
            break
        else:
            continue
            print("sorry you didn't get the answer")

    if is_word_guessed(secret_word, letters_guessed):
        print("You won this round")
        print(f"The word was {secret_word}")
    else:
        print("sorry you didn't get the answer")
        print(f"The word was {secret_word}")

hangman(choose_word(wordlist))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
