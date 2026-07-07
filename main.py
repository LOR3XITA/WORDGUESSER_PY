import random
import json
import sys
import colorama
colorama.init()
from pathlib import Path
import requests

current_version = "1.1.0"


def check_updates() -> None:
    try:
        url = "https://github.com/LOR3XITA/WORDGUESSER_PY/releases/latest"
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        latest_version = response.json()["tag_name"].lstrip("v")
        if current_version != latest_version:
             print(f"VERSION {latest_version} OF WORDGUESSER_PY IS OUT! DOWNLOAD IT AT https://github.com/LOR3XITA/WORDGUESSER_PY/releases/latest")
        else:
             print("You're up-to-date!")
    except requests.RequestException:
         print("Couldnt connect to https://github.com/LOR3XITA/WORDGUESSER_PY/releases/latest to find updates")

check_updates()

def compare(word_list: list[str], guess_list: list[str]) -> str:
    if len(word_list) != len(guess_list):
         print(f"YOUR WORD HAS {len(guess_list)} LETTERS INSTEAD OF {word_list}! TRY AGAIN!")
         tries += 1
    
    word_w_colors = []
    RESET_COLOR = "\x1b[0m"
    RED_COLOR = "\x1b[41m"
    YELLOW_COLOR = "\x1b[43m"
    GREEN_COLOR = "\x1b[42m"

    for i, letter in enumerate(guess_list):
        if letter == word_list[i]:
            word_w_colors.append(f"{GREEN_COLOR}{letter}{RESET_COLOR}")
        elif letter in word_list:
            word_w_colors.append(f"{YELLOW_COLOR}{letter}{RESET_COLOR}")
        else:
            word_w_colors.append(f"{RED_COLOR}{letter}{RESET_COLOR}")
    
    return "".join(word_w_colors)

def load_vocabulary() -> list[str]:
    with open("language.json", "r") as file:
        vocabulary = json.load(file)
        language = Path(vocabulary["language"] + ".txt")
    if language.exists():
        with language.open() as file:
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
