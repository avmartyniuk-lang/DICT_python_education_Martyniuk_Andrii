import random

print("HANGMAN")

while True:
    choice = input('Type "play" to play the game, "exit" to quit: > ')

    if choice == "exit":
        break
    elif choice == "play":
        possible_words = ["python", "java", "javascript", "php"]
        right_answer = possible_words[random.randint(0, 3)]

        hidden = ["-"] * len(right_answer)
        tried = []
        attempts = 8

        while attempts > 0:
            print()
            print("".join(hidden))
            letter = input("Input a letter: > ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            elif letter in tried:
                print("You've already guessed this letter")
            else:
                tried.append(letter)
                if letter in right_answer:
                    for i in range(len(right_answer)):
                        if right_answer[i] == letter:
                            hidden[i] = letter
                else:
                    print("That letter doesn't appear in the word")
                    attempts -= 1

            if "-" not in hidden:
                print("You guessed the word " + right_answer + "!")
                print("You survived!")
                break

        if "-" in hidden:
            print("You lost!")
