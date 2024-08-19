# CHATGPT: 1. Egész számként tárolod, majd mod operátorral lekéred az utolsó számjegyet: Ebben az esetben nem indexelni
# fogod a számot, hanem matematikai úton, a maradékos osztás (%) operátorral kérheted le az utolsó számjegyet.
taj_szam = int(input("Kérem a TAJ-számot: "))

# Az utolsó számjegy kiszámítása
utolso_szamjegy = taj_szam % 10

# Az utolsó számjegy kiíratása
print(f"Az ellenőrzőszámjegy: {utolso_szamjegy} ")

# CHATGPT: Szövegként tárolod a TAJ-számot, majd visszaalakítod számokká:
# Ez az első megoldásodhoz hasonló, ahol a TAJ-számot stringként kezeled, és amikor szükséged van rá, számként használod:

# Bekérjük a TAJ-számot szövegként
taj_szam = input("Kérem a TAJ-számot: ")

# Az utolsó számjegy kivétele és átalakítása számmá
utolso_szamjegy = int(taj_szam[-1])

# Az utolsó számjegy kiíratása
print(f"Az ellenőrzőszámjegy: {utolso_szamjegy}")

"""
tajszam = 673457015
for szam in taj_szam[:8]: # nyolcadikig -> 0.-tól a 7.-ig, miután indexelünk, ezért a 0-tól számítva a 8.-ig megyünk, tehát a hetedikig.

67345701
"""
