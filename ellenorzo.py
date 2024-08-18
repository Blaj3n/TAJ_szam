# CHATGPT: A programod nem fog működni, mivel az int() függvénnyel egész számmá alakítod a bemenetet, és a numerikus
# típusokon nem lehet indexelni, tehát nem kérheted le a TAJ-szám utolsó számjegyét úgy, ahogy egy string esetén tennéd
taj_szam = input("Kérem a TAJ-számot: ")

ellenorzoszam = int(taj_szam[-1])  # A TAJ-szám utolsó karakterét egész számmá alakítom, hogy megtudjam,
# mi az utolsó számjegy (ellenőrzőszám).
#123456789
print(f"Az ellenőrzőszámjegy: {ellenorzoszam}  ")

osszeg = 0
pozicio = 1  # Létrehozunk egy pozicio változót, ami az aktuális karakter pozícióját fogja tárolni. Kezdéskor ez 1 lesz,
# mert a feladatban az első pozícióra hivatkozunk (nem 0-ra, mint az indexelésnél).
# A pozicio változót minden iteráció végén növeljük 1-gyel.

for szam in taj_szam[:8]:  # Az első nyolc számjegyen végigmegyünk
    szam = int(szam)  # A számjegyet egész számmá alakítjuk
    if pozicio % 2 == 1:
        osszeg += szam * 3
    else:
        osszeg += szam * 7
    pozicio += 1

print(f"A szorzatok összege: {osszeg} ")

if osszeg % 10 == ellenorzoszam:
    print("Helyes a szám!")
else:
    print("Hibás a szám!")
