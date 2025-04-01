current_word = ["-", "-", "-", "-", "-"]
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
invalid_positions = {letter: set() for letter in letters}
wrong_letters = set()
bad_letters = set()

def main():

    inputed = input("Enter world word: ")
    inputed = inputed.lower()
    badwronggood = input("Enter word order B/W/G: ")
    badwronggood = badwronggood.lower()
    with open('words.txt', 'r') as file:
        words = file.readlines()
    for i in range(len(inputed)):
        if badwronggood[i] == 'b':
            if inputed[i] not in wrong_letters and inputed[i] not in current_word:
                letters.discard(inputed[i])
                bad_letters.add(inputed[i])
        elif badwronggood[i] == 'w':
            invalid_positions[inputed[i]].add(i)
            wrong_letters.add(inputed[i])
        elif badwronggood[i] == 'g':
            current_word[i] = inputed[i]
            wrong_letters.discard(inputed[i])

    # print(f"Current word: {current_word}")
    # print(f"Bad letters: {bad_letters}")
    # print(f"Wrong letters: {wrong_letters}")
    # print(f"Invalid positions: {invalid_positions}")

    if wrong_letters:
        for word in words:
            word = word.strip().lower()
            if all(cw == '-' or cw == w for cw, w in zip(current_word, word)) and all(i not in invalid_positions[word[i]] for i in range(len(word))):
                if all(word.count(letter) >= inputed.count(letter) and word.index(letter) not in invalid_positions[letter] for letter in wrong_letters) and not any(letter in word for letter in bad_letters):
                    print(word)
    else:
        for word in words:
            word = word.strip().lower()
            if all(cw == '-' or cw == w for cw, w in zip(current_word, word)) and not any(letter in word for letter in bad_letters):
                print(word)


    print(current_word)
    main()
if __name__ == '__main__':
    main()