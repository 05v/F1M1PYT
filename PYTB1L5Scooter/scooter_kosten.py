
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
bereken_maandkosten(km_per_maand)

invoer = input("Hoeveel km per maand: ")

while invoer != float:
    try:
        invoer = float(invoer)
        print("Ja, de invoer ", str(invoer), " is een getal, want ik kan het omzetten naar een float")
        break

    except ValueError:
        print(invoer, " is geen getal...")
        break