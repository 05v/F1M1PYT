
import time

print("")

question = input("[?] Do you want a BURGER or CAKE: ")
if question == 'BURGER':
    print("You received a delicious juicy burger...")
elif question == 'CAKE':
    print("You received a plain cake which smells horrible...")
else:
    print(question, " that's not an option! Choose BURGER or CAKE")

print("")

question2 = input("[?] Go to HOME or STORE: ")
if question2 == 'HOME':
    print("You are waiting on the bus to go home...")
elif question2 == 'STORE':
    print("Uppon arriving at the store, you see it's closed, you decide to take the bus home...")
else:
    print(question2, " that's not an option! Choose HOME or STORE")

print("")

question3 = input("[?] The bus is 10 minutes late, WAIT or WALK: ")
if question3 == 'WAIT':
    print("The bus arrived, its completely full and uncomfortable...")
elif question3 == 'WALK':
    print("You decide to walk home, on your way you found a $20 bill...")
else:
    print(question3, " that's not an option! Choose WAIT or WALK")

print("")

question4 = input("[?] You arrive home it is now 10:00pm, GAME or SLEEP: ")
if question4 == 'GAME':
    print("You play videogames for an hour then fall asleep...")
elif question4 == 'SLEEP':
    print("You decide to sleep, it was an exhausting day...")
else:
    print(question4, " that's not an option! Choose GAME or SLEEP")

print("")

question5 = input("[?] You wake up, you don't have work today, go back to SLEEP or GETUP: ")
if question5 == 'SLEEP':
    print("You went back to sleep, you choked in your sleep.")
elif question5 == 'GETUP':
    print("You decide to get out of back, you trip and fall out of your window.")
else:
    print(question5, " that's not an option! Choose SLEEP or GETUP")

print("")
time.sleep(3)
print("[!] Thanks for playing!")
print("")