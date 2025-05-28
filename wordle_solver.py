import pandas as pd
import numpy as np

# read word list
language = input("Choose a language (1: German, 2: English): ")

while language not in ["1", "2"]:
    print("")
    print("Your input wasn't an option. Please retry!\n")
    language = input("Choose a language (1: German, 2: English): ")
    print("")
    
language = int(language)

if language == 1:
    df = pd.read_csv("wordle_deutsch_liste.txt", sep=",", header=None)
    word_list = np.array(df)
    word_list = word_list[0]
else:
    df = pd.read_csv("wordle_englisch_liste.txt", header=None)
    word_list = np.array(df).T
    word_list = word_list[0]
    word_list = [i.upper() for i in word_list]
    

block_letters = []
yellow_letters = {}
green_letters = {}


def set_grey_letters(in_str):
    for i in in_str.upper():
        if i in block_letters:
            print(f'{i} is already bloked.')
            continue
        else:
            block_letters.append(i)

    return None


def set_yellow_letters(in_str):
    for i in range(len(in_str) // 2):
        try: 
            if yellow_letters[in_str[2*i]] != None:
                yellow_letters[in_str[2*i]].append(int(in_str[2*i+1]))
            else:
                continue
        
        except KeyError:
            yellow_letters[in_str[2*i]] = []
            yellow_letters[in_str[2*i]].append(int(in_str[2*i+1]))

    print("The following yellow letters and positions are registered: ")
    print(yellow_letters)
    return None


def set_green_letters(in_str):
    for i in range(len(in_str) // 2):
        green_letters[int(in_str[2*i+1])] = in_str[2*i]

    print("The following green letters and positions are registered: ")
    print(green_letters)
    return None


def return_possible_words():
    list_possible_words = []

    for word in word_list:
        word_is_possible = True
        
        for i in range(len(word)):
            if word[i] in block_letters:
                word_is_possible = False
                break
        
            if word[i] in yellow_letters:
                if i + 1 in yellow_letters[word[i]]:
                    word_is_possible = False
                    break

            if i+1 in green_letters:
                if green_letters[i+1] != word[i]:
                    word_is_possible = False
                    break

        for j in yellow_letters:
            if j not in word:
                word_is_possible = False
                break

        if word_is_possible:
            list_possible_words.append(word)

    print("The following words are possible: ")
    print(list_possible_words)

    return None


def main():
    solved = False

    print("Welcome to the Wordle Solver! \n")

    while not solved:
        print("The following modi are available! ")
        print("1: Grey letters. Format: ABCDE...")
        print("2: Yellow letters. Format: A2B3C1")
        print("3: Green letters. Format: F1B3C5")
        print("4: Return possible words")
        print("5: End program.\n")

        modus = int(input("Please choose a modus: "))
        print('\n')

        if modus == 1:
            in_str = input("Enter grey letters: ")
            set_grey_letters(in_str)
        elif modus == 2:
            in_str = input("Enter yellow letters and their position: ")
            set_yellow_letters(in_str)
        elif modus == 3:
            in_str = input("Enter green letters and their position: ")
            set_green_letters(in_str)
        elif modus == 4:
            return_possible_words()
        elif modus == 5:
            solved = True
        else:
            print("Please retry, you haven't typed a valid option!")

        print("\n")


main()