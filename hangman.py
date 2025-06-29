import random

def hangman(word):
    wrong = 0
    stages = ["",
              "____    ",
              "|   |   ",
              "|   |   ",
              "|   O   ",
              "|  /|\  ",
              "|   |   ",
              "|  / \  ",
              "|       "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hanging!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter letter: "
        char  = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]  = char
            rletters[cind]  ='$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You Win! The word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stage[0: wrong]))
        print("You lost! The word was: {}.".format(word))

words = ["кот", "живот", "бегемот"]
random_word = random.choice(words)
hangman(random_word)