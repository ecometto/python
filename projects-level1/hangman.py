import getpass, random

# VARIABLES:
maxAttempts = 5
attempts = 0
modes = ["1", "2"]
end = False
progress = ""


# FUNCTIONS
def inputVacio(prompt):
    return getpass.getpass(prompt=prompt)


def validateProgress(letters, secretWord):
    progress = ""
    for eachLetter in secretWord:
        if eachLetter in letters:
            progress += eachLetter
        else:
            progress += "-"
    return progress


def playAlone():
    words = ["ven","lin"]
    end = False
    letters = []
    secretWord = random.choice(words)

    while end == False:
        letter = input("Type a letter: ")
        while letter in letters:
            print(f"You have already used the letter {letter}")
            letter = input("Type a diferent letter: ")

        letters.append(letter)

        progressStr = validateProgress(letters, secretWord)
        print(progressStr)

        if progressStr == secretWord:
            end = True
            print("Youn have won !!! Congratulations")
            exit = input("Do you want to play Again? (1=Yes or 2= No (exit))")
            if exit == "2":
                return True
            else:
                letters = []
                return False


def playWithAFriend():    
    
    end = False
    letters = []
    
    print("FRIEND N°1 turn...")
    secretWord = inputVacio("Type a secret word to guess: ")
    # print("FRIEND N°2 turn...")

    while end == False:
        letter = input("\nFRIEND N°2 turn..\nType a letter: ")
        while letter in letters:
            print(f"You have already used the letter {letter}")
            letter = input("Type a diferent letter: ")

        letters.append(letter)

        progressStr = validateProgress(letters, secretWord)
        print(progressStr)

        if progressStr == secretWord:
            end = True
            print("Youn have won !!! Congratulations")
            exit = input("Do you want to play Again? (1=Yes or 2= No (exit))")
            if exit == "2":
                return True
            else:
                letters = []
                return False

    pass
    # letters = []
    
    # print("FRIEND N°1 turn...")
    # secretWord = inputVacio("Type a secret word to guess: ")
    # print("FRIEND N°2 turn...")

    # # while end == False:
    # letter = input("Type a letter: ")
            
    # while letter in letters:
    #     print(f"You have already used the letter {letter}")
    #     letter = input("Type a diferent letter: ")

    # letters.append(letter)

    # progress = validateProgress(letters, letter, secretWord)
    # print(progress)

    # if progress == secretWord:
    #     print("Youn have won !!! Congratulations")
    #     exit = input("Do you want to play Again? (1=Yes or 2= No (exit))")
    #     if exit == "2":
    #         return True
    #     else:
    #         return False



def run():

    # INITIALIZING THE GAME
    print(
        f"""
-------------------------------------------------------------------------------------
WELCOME =) ..! 
In this game, you have to guess a secret word. 
You have {maxAttempts} attempts to achieve it.
Good luck !!!!

There are 2 modes to play it ('Alone' or 'with a friend'). 
"""
    )

    # VALIDATING THE INPUT
    mode = input("Select the mode you want to play: \n1- Alone \n2- With a friend\n")
    while True:
        if mode not in modes:
            mode = input(
                "You have to choise a valid mode (1=alone o 2=With a friend)\n"
            )
        else:
            break

    # RUNNING THE GAME IN SELECTED MODE
    status = False
    while not status:
        if mode == "1":
            print("You have choised play ALONE.")
            status = playAlone()
            
        elif mode == "2":
            print("You have choised play with a FRIEND.")
            status = playWithAFriend()


run()
