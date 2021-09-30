weekdag = False

print("Welke dag is het? Kies uit: maandag / dinsdag / woensdag / donderdag / vrijdag / zaterdag / zondag")
dagcheck = input("Welke dag is het: ")
if dagcheck == ("maandag") or dagcheck == ("dinsdag") or dagcheck == ("woensdag") or dagcheck == ("donderdag") or dagcheck == ("vrijdag"):
    weekdag = True
elif dagcheck == ("zaterdag") or dagcheck == ("zondag"):
    weekend = True
else: 
    print("Dat is geen optie, kies uit een van de dagen. (CAPS SENSITIVE)")

if weekdag:
    schooldag = True
elif weekend:
    schooldag = False

if schooldag == True:
  print("Pak je spullen en ga er heen!")
else:
  print("Lekker uitslapen!")