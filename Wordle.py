# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:23:27 2022

@author: Jason Kim

Python Wordle
"""

"""
To-Do
 - repeating letters
 - better graphics
 - more common words
"""

import random

debug = False

if __name__ == "__main__":
    
    # alphabet
    unused_letters = set(open('alphabet.txt').read().split('\n'))
    used_letters = set()
    
    """
    # getting five-letter words from txt file (coutesey of https://github.com/charlesreid1/five-letter-words)
    file = open('words.txt')
    words = file.read().split('\n')
    """
    words = open('corncob_lowercase.txt').read().split('\n')
    to_remove = []
    for word in words:
        if len(word) != 5:
            to_remove.append(word)
    # removing
    for word in to_remove:
        words.remove(word)
    
    
    # choosing word
    the_word = words[int(random.random() * len(words))].upper()
    # debugging
    if debug == True:
        print("The Word: " + the_word)
    
    # game loop
    guesses = 0;
    past_guesses = '\n'
    win = False
    while win == False:
        
        # user guesses
        while True:
            guess = input('Guess #{}: '.format(guesses + 1)).lower()
            if not guess in words or len(guess) != 5:
                print('Invalid word. Please try again.')
                continue
            break
        guess = guess.upper()
        guesses += 1
        
        win = True
        # guess results
        guess_results = ''
        for i in range(5):
            letter = guess[i]
            if not letter in the_word: # letter is not in the word
                guess_results += letter + 'x '
                win = False
            else:
                if not letter == the_word[i]: # letter is in the word, but not in the right position
                    guess_results += letter + '? '
                    win = False
                else: # the letter is in the word, and at the right position
                    guess_results += letter + '! '
            # updating letter status
            unused_letters.discard(letter)
            used_letters.add(letter)
        guess_results += '\n'
        past_guesses += guess_results
        print(past_guesses)
        
        # letter status
        print('Unused Letters: ' + str(unused_letters))
        print('Used Letters: ' + str(used_letters))
        
        # game over
        if guesses >= 6 and win == False:
            print('\nThe word was: ' + the_word)
            break
    
    # win pog
    print('\nYou got the word "{}" in {} guesses!'.format(the_word, guesses))