import sys

debug = False

# word lists
DATA_DIR = "data/"
word_lists = {'corncob_lowercase.txt': [], 'five_letter_words.txt': [], 'top20kwords.txt': []}

# exit keywords
exit = {'exit', 'quit', 'stop'};

# lists out top 5 possible words
def possible_words():
    print('\nPossible Words:')
    for filename in word_lists:
        print('\n{}: {}'.format(filename, len(word_lists[filename])))
        for word in word_lists[filename][0:5]:
            print(word)
        if len(word_lists[filename]) > 5:
            print('...')

if __name__ == "__main__":
    
    # loading word lists
    for filename in word_lists:
        print('Loading', filename, '...')
        word_lists[filename] = open(DATA_DIR + filename).read().split('\n')
        
    # word length
    length = int(input('\nWord Length: ')) # debug: 10
    
    # keeping words of specified length
    for filename in word_lists:
        to_remove = []
        for word in word_lists[filename]:
            if len(word) != length:
                to_remove.append(word)
        for word in to_remove:
            word_lists[filename].remove(word)
    
    # removing word lists with zero words
    to_remove = []
    for filename in word_lists:
        if len(word_lists[filename]) == 0:
            to_remove.append(filename)
    for filename in to_remove:
        word_lists.pop(filename)
    
    # guessing phase
    for i in range(6):
        print('\nGUESS #{}'.format(i+1))
        
        # green letters
        possible_words()
        green_letters = input('\nGreen Letters: ').lower()
        if green_letters in exit: # quit keyword detection
            sys.exit()
        elif not '_' in green_letters: # win pog
            print("\nYou won, congrats!")
            break
        
        # search
        for filename in word_lists:
            words = word_lists[filename]
            for i in range(len(green_letters)):
                # debugging
                if debug == True:
                    print('Debug: Letter', i)
                to_remove = []
                letter = green_letters[i] # current letter
                if letter == '_':
                    continue # skip (unknown)
                for word in words:
                    other_letter = word[i]
                    if letter != other_letter: # check if the letter is in the right position in the possible word
                        to_remove.append(word)
                # removing
                for word in to_remove:
                    words.remove(word)
        
        # yellow letters
        possible_words()
        yellow_letters = input('\nYellow Letters: ').lower()
        
        # search again
        for filename in word_lists:
            words = word_lists[filename]
            for i in range(len(yellow_letters)):
                to_remove = []
                letter = yellow_letters[i] # current letter
                if letter == '_':
                    continue # skip (unknown)
                for word in words:
                    other_letter = word[i]
                    if letter == other_letter: # yellow letter is in the wrong spot
                        to_remove.append(word)
                    elif not letter in word:
                        to_remove.append(word) # yellow letter is not in the word
                # removing
                for word in to_remove:
                    words.remove(word)
        
        # grey letters
        possible_words()
        grey_letters = input('\nGrey Letters: ').lower()
        
        # filtering
        for filename in word_lists:
            words = word_lists[filename]
            for letter in grey_letters:
                to_remove = []
                for word in words:
                    if letter in word:
                        to_remove.append(word)
                # removing
                for word in to_remove:
                    words.remove(word)