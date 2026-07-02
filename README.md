# WordGuesser_PY

A simple terminal-based word-guessing game (Wordle-style) written in Python. The game picks a random word from a vocabulary file and gives the player color-coded feedback on each guess.

## Features

- Random word selection from a customizable vocabulary file
- Color-coded letter feedback directly in the terminal:
  - 🟩 **Green**: correct letter in the correct position
  - 🟨 **Yellow**: correct letter in the wrong position
  - 🟥 **Red**: letter not in the word
- Configurable language/vocabulary via a JSON config file
- Limited number of tries (5 by default)
- Quick exit shortcut during a guessing round

## Requirements

- Python 3.6+
- No external dependencies Python standard library only (`random`, `os`, `json`, `sys`)

## Project Structure

```
.
├── wordguesser.py      # Main game script
├── language.json       # Config file specifying which word list to use
└── <language>.txt      # Word list file (e.g. ENG.txt), one word per line
```

## Setup

1. Open the language.json file and edit the language. It is set on english by default (the other option is ITA - italian):

   ```json
   {
     "language": "ENG"
   }
   ```

1.5 If you want to add your own vocabulary file it should be a .txt formatted like shown below. If you do so, put the name of your file (without the extension) in the language.json file.

   ```
   HOUSE
   TABLE
   RIVER
   ...
   ```

## Usage

Run start.bat

You'll be prompted with:

```
WELCOME TO WORDGUESSER_PY! PRESS S TO START OR E TO EXIT:
```

- Press **S** to start a new round.
- Press **E** to exit the program.

During a round, you'll be asked to guess the word letter by letter:

```
TRY TO GUESS THE WORD (5 LETTERS, 5 TRIES):
```

Type your guess and press Enter. The letters will be shown highlighted according to how close your guess is to the target word.

### Quitting mid-round

While guessing, entering `!` will immediately exit the program.

- If the guess length doesn't match the target word's length, the game currently prints a warning but does not correctly handle re-prompting the player (this is a known bug being worked on).
- The word list should contain only single words without leading/trailing whitespace for accurate guessing.

## License

This project is provided as-is for personal/educational use. Feel free to modify and extend it.
