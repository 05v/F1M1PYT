# Als ik honger heb en ik geen zin heb om te koken dan bestel ik pizza tenzij 
# er nog een kliekje in de koelkast ligt. Dan eet ik die op. 
# Als ik geen geld heb ga ik toch koken.

Hunger = True
Cooking = False
Fridge = False
Money = True

if Hunger == True and Cooking == False and Fridge == False and Money == True:
    print("[x] You ordered pizza.")
elif Hunger == True and Cooking == False and Fridge == True:
    print("[x] Er ligt nog een kiekje in de koelkast.")
elif Hunger == False:
    print("[x] You're not hungry.")
else:
    print("[x] You're broke, go cook food")