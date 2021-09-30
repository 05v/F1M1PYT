from time import process_time


name = "erwin henraat"
job = "teacher"
moneyInAccount = 9000

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.

if name == "erwin henraat" and job != None or moneyInAccount > 10000:
    print("[x] Enjoy the new ride!")
    exit()
else:
    print("[x] You can't afford a motorcycle, you only have:", moneyInAccount)




#Maak nu voor jezelf ook een logische voorwaarde waarin je de operatoren 'and' en 'or' gebruikt.