# wordle bot

## Overview
The `main.py` script is a Python program designed for filtering words in wordle based on various constraints. It allows users to input a word and specify whether the letters are "bad," "wrong," or "good." Based on this input, the program intelligently determines the possible valid words that align with the provided constraints.

The script primarily filters words from a file called `words.txt`.

## Features
- **Interactive Word Input**: Prompts users to input a word and classify each letter as one of the following:
  - **B (Bad)**: The letter is not in the word.
  - **W (Wrong)**: The letter is in the word but not in the correct position.
  - **G (Good)**: The letter is in the word and in the correct position.
- **Invalid Position and Wrong Letters**: Keeps track of letters that are in the word but positioned incorrectly.
- **File Input**: Reads a list of possible words from the `words.txt` file.
- **Smart Filtering**: Compares the user input against the list of words and outputs only those that match the given constraints.

## How to Use
### 1. Ensure File Presence
Place a file named `words.txt` in the same directory as the `main.py` script. This file should contain the words that the program will filter from, with each word on a new line.

### 2. Run the Script
Execute the script using Python:
```sh
python main.py
```

### 3. Interactive Prompts
- **Enter a word** when prompted:
  ```
  Enter world word: snake
  ```
- **Specify the status of each letter** using `B/W/G`:
  ```
  Enter word order B/W/G: WBGBB
  ```

### 4. View Outputs
The script will output all valid words matching the constraints provided.

#### Example
**Input:**
```sh
Enter world word: snake
Enter word order B/W/G: WBGBB
```

**Output:**
```sh
stake
spake
scale
...
```

## Requirements
- Python 3.9 or newer.

## Key Variables and Logic
### Variables:
- `current_word`: Tracks the known positions of correct letters.
- `letters`: Contains all available letters.
- `invalid_positions`: Tracks positions where letters cannot appear.
- `wrong_letters`: Letters that are in the word but misplaced.
- `bad_letters`: Letters not present in the word.

### Processing Logic:
- If a letter is marked **B (Bad)**, it is added to `bad_letters` and removed from the set of available letters.
- If a letter is marked **W (Wrong)**, its position is added to `invalid_positions`, and it’s added to `wrong_letters`.
- If a letter is marked **G (Good)**, its position is set in `current_word`.

### Filtering Words:
Words are filtered based on constraints stored in `current_word`, `invalid_positions`, `wrong_letters`, and `bad_letters`.

## Customization
To modify or expand the script:
- Adjust or add logic for different word constraints.
- Change the input file `words.txt` to include a different list of words.
- Customize prompts if additional input fields are necessary.

---

