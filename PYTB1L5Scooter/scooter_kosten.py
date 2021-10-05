
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

def bereken_maandkosten():
    return (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand

script = True
while script:
    try:
        km_per_maand = float(input("Hoeveel kilometer rijd je per maand: "))
        value = bereken_maandkosten()
        print("Jij betaald $"+ str(value) +" per maand aan ")

        break
    except:
        print("Dat is geen float")
        break