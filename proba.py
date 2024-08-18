# CHATGPT: 1. Egész számként tárolod, majd mod operátorral lekéred az utolsó számjegyet: Ebben az esetben nem indexelni
# fogod a számot, hanem matematikai úton, a maradékos osztás (%) operátorral kérheted le az utolsó számjegyet.
taj_szam = int(input("Kérem a TAJ-számot: "))

# Az utolsó számjegy kiszámítása
utolso_szamjegy = taj_szam % 10

# Az utolsó számjegy kiíratása
print(f"Az ellenőrzőszámjegy: {utolso_szamjegy}")