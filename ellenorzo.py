# CHATGPT: A programod nem fog működni, mivel az int() függvénnyel egész számmá alakítod a bemenetet, és a numerikus
# típusokon nem lehet indexelni (tehát nem kérheted le a TAJ-szám utolsó számjegyét úgy, ahogy egy string esetén tennéd).
taj_szam = (input("Kérem a TAJ-számot: "))

utolso_szamjegy = taj_szam[-1]
#012345678
print(f"Az ellenőrzőszámjegy: {utolso_szamjegy}  ")
