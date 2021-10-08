# In de code MOET je gebruik maken van loops, functies en arrays 
# (lists/tuples/sets/dictionaries). De game is een oneindige loop 
# totdat de speler het spel wint of verliest OF het spel handmatig 
# afsluit middels een commando.

# DE GAME MOET ALS VOLGT WERKEN:

# De speler moet aan het begin van het spel gegroet worden gevolgd door een uitleg van het spel.
# De speler moet het spel zelf kunnen afsluiten door een commando in te typen.
# Het spel kiest willekeurig een woord uit een woordenlijst aan het begin van het spel.
# De speler moet een aantal levens hebben. Als een letter niet in het woord zit wordt er een leven afgetrokken. Als de speler 0 levens heeft, hangt de speler.
# De geraden letters van het woord mogen alleen zichtbaar zijn.
# De speler mag maar één letter per input geven. Vang dit af met een boodschap aan de speler als de speler zich hier niet aan houdt. (Met uitzondering van het afsluit commando.)
# De speler moet zien welke letters al genoemd zijn.
# Dezelfde letter mag niet nog een keer geraden worden. Vertel de speler dat de letter al geraden is en laat de speler een nieuwe poging doen.
# Aan het einde van het spel, zowel bij winnen als verliezen, wordt het volledige woord onthuld. Het spel sluit vervolgens automatisch af met een gepaste boodschap.

import random
import time
import os

# Runs clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

clearConsole()

def choose_word():
    with open('word_list.txt', 'r') as whole_list:
        list_full = [line.strip() for line in whole_list]
    random_word = random.choice(list_full)
    print(random_word)

def scramble_word():
    len_word = len(choose_word)
    print(len_word)

def gameStart():
    print("[C] is the computer")
    print("[Y] is you")
    print("\n")
    print("[C] Hello", name, ", you start with 7 lifes")
    print("[C] The word is, ", choose_word())

    

# runDemo()
def runDemo():

    # 1st Instance
    print("[C] is the computer")
    print("[Y] is you")
    time.sleep(3)
    clearConsole()
    print("[C] Hello", name, ", you start with 7 lifes")
    time.sleep(3)
    print("[C] The word is _______")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: E")
    
    time.sleep(2)
    clearConsole()

    # 2nd Instance
    print("[C] That is correct", name, ", you have 7 lifes left")
    time.sleep(3)
    print("[C] The word is E_____E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: C")
    time.sleep(2)
    clearConsole()

    # 3rd Instance
    print("[C] That is incorrect", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is E_____E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: X")

    time.sleep(2)
    clearConsole()

    # 4th Instance
    print("[C] That is correct", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is EX____E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: M")
    time.sleep(2)
    clearConsole()

    # 5th Instance
    print("[C] That is correct", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is EX_M__E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: C")
    time.sleep(2)
    clearConsole()

    # 6th Instance
    print("[C] That is correct", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is EX_M__E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: A")
    time.sleep(2)
    clearConsole()

    # 7th Instance
    print("[C] That is correct", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is EXAM__E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: P")
    time.sleep(2)
    clearConsole()

    # 8th Instance
    print("[C] That is correct", name, ", you have 6 lifes left")
    time.sleep(3)
    print("[C] The word is EXAMP_E")
    time.sleep(3)
    print("[C] Guess a letter: ")
    time.sleep(3)
    print("[Y] Letter: L")
    time.sleep(2)
    clearConsole()

    # 8th Instance
    print("[C] Great job ", name, ", you won!")
    time.sleep(3)
    print("[C] The word was 'EXAMPLE'")
    time.sleep(3)
    print("[C] You won with 6 lifes left!")
    time.sleep(3)
    clearConsole()

    # Ending demo
    print("Now it's your turn to play!")
    gameStart()

# Welcomes the user
print("Welcome to hangman")
name = input("Please enter your name: ")
print("\n")

# Rules list
def rules():
    clearConsole()

    # Rule 1
    print("Very well, these are the rules:")
    print("\n")
    print("Rule 1:")
    print("We will choose a random word from the English")
    print("dictionairy, this is a list of 370,000+ words.")

    # Rule 2
    time.sleep(3)
    print("\n")
    print("Rule 2:")
    print("A hidden word will appear like the following:")
    print("_______ you can enter letters to guess the word,")
    print("if a letter is in the word it will be replaced")
    print("like this: e_____e")
    print("if the guess is wrong, you will lose a life.")

    # Rule 3
    time.sleep(12)
    print("\n")
    print("Rule 3:")
    print("You will have 7 lives, every wrong guess you make")
    print("you will lose a life, once you lose all your")
    print("lifes, you lose the game.")

    # Have fun!
    time.sleep(4)
    print("\n")
    print("Have fun!")
    time.sleep(2)

    # Rules run
    print("Have you read the rules:")
    rules_read = input("Y/N: ")
    if rules_read == "Y" or rules_read == "y":
        # runDemo y/n
        print("Do you want to run a demo?")
        demo_YN = input("Y/N: ")

        # Run Demo = Yes
        if demo_YN == "Y" or demo_YN == "y":
            print("Starting demo...")
            time.sleep(1)
            clearConsole()
            runDemo()

        # Run Demo = No
        elif demo_YN == "N" or demo_YN == "n":
            print("Okay, i'll give you some time!")
            time.sleep(7)
            print("That should be enough time!")
            print("Starting the demo!")
            runDemo()

        # Run demo else
        else:
            print("That is not an option,")
            print("please use Y or N")

    elif rules_read == "N" or rules_read == "n":
        print("Okay, i'll give you some time!")
    else:
        print("That is not an option,")
        print("please use Y or N")
    # Run Demo:
    clearConsole()


# Explain rules Y/N
clearConsole()
print("Welcome to hangman", name) 
print("\n")
print("Do you want me to explain")
print("the rules to you?")
rules_YN = input("Y/N: ")

if rules_YN == "Y" or rules_YN == "y":
    rules()
elif rules_YN == "N" or rules_YN == "n":
# runDemo y/n
    print("Do you want to run a demo?")
    demo_YN = input("Y/N: ")

    # Run Demo = Yes
    if demo_YN == "Y" or demo_YN == "y":
        print("Starting demo...")
        time.sleep(1)
        clearConsole()
        runDemo()
    
else:
    print("That is not an option,")
    print("please use Y or N")

print("")