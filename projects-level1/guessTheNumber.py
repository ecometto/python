import random

def run():
    numberFrom = 1
    numberTo = 99
    searchedNumber = random.randint(numberFrom,numberTo)
    attempts = 0
    maxAttempts = 10
    finish = False

    print(f'''
-------------------------------------------------------------------------------------
WELCOME =) ..! 
In this game, you have to guess a number between {numberFrom} and {numberTo}. 
You have {maxAttempts} attempts to achieve it.
Good luck !!!!
''')
    while finish != True:
        number = input(f"*** Insert a number, please (from {numberFrom} to {numberTo}): ")
        
        if not number.isdigit():
            print("ERROR. You have to write a valid number. ")
            continue
        else:
            number = int(number)
            if number > numberTo or number < numberFrom:
                print("ERROR. You have to write a valid number. ")
            else:        
                if number > searchedNumber:
                    attempts += 1
                    print(f"The inserted number is grater than the 'Unknow' one.  ")
                    print(f"The number of available attempts is: {maxAttempts - attempts}")
                elif number < searchedNumber:
                    attempts += 1
                    print(f"The inserted number is smaller than the 'Unknow' one.  ")
                    print(f"The number of available attempts is: {maxAttempts - attempts}")
                else:
                    print (f"\nYou have won.!!! \nThe number of attempst was {attempts}\n")
                    finish = True
            
        if attempts >= maxAttempts:
            print("\nSORRY... \nYou have already use all the attemps.\n")
            break
run()