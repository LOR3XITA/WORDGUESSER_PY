import random
import os
import json
import sys
import colorama

colorama.init()

def compare(word_list: list, guess_list: list):
    if len(word_list) != len(guess_list):
         print(f"YOUR WORD HAS {len(guess_list)} LETTERS INSTEAD OF {word_list}! TRY AGAIN!")
         tries += 1
    word_w_colors = []
    for i, letter in enumerate(guess_list):
        if letter == word_list[i]:
            word_w_colors.append(f"\x1b[42m{letter}\x1b[0m")
        elif letter in word_list:
            word_w_colors.append(f"\x1b[43m{letter}\x1b[0m")
        else:
            word_w_colors.append(f"\x1b[41m{letter}\x1b[0m")
    
    return "".join(word_w_colors)

def load_vocabulary():
    with open("language.json", "r") as file:
        vocabulary = json.load(file)
        language = vocabulary["language"] + ".txt"
    if os.path.exists(language):
        with open(language, "r") as file:
            return file.read().splitlines()
    else:
        print("ERROR! FILE DOESN'T EXIST!")



while True:
    tries = 5
    
    gamestart = input("WELCOME TO WORDGUESSER_PY! PRESS S TO START OR E TO EXIT: ").upper()
    if gamestart == "S" or gamestart == "DEBUG":
        
                content = load_vocabulary()
                word = list(random.choice(content))
                if gamestart == "DEBUG": print(f"DEBUG: {word}")
                guess = list("")
                while guess != word and tries >0:
                    guess = list(input(f"TRY TO GUESS THE WORD ({len(word)} LETTERS, {tries} TRIES): "))
                    if guess == ["!"]: sys.exit()
                    print(compare(word, guess))
                    tries -= 1
                
                if guess == word:
                     print("CORRECT! YOU WON!")
                
                if tries <0:
                     print(f"YOU LOST! THE WORD WAS {guess}")
        
    elif gamestart == "E":
        sys.exit()
    else:
        continue
