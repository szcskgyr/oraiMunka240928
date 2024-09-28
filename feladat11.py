def husvet():

    # 11. feladat – Húsvét
    # A program kérjen be egy évszámot a felhasználótól! Ha ez 1900 és 2099 közé esik, akkor a program írja ki, hogy az adott évben melyik napra esik húsvét vasárnap! A kiszámítás algoritmusát megtalálja a Wikipedia-ban Gauss módszer néven.

    szam1 = int(input("Kérem, adjon meg egy évszámot 1900 és 2099 között!"))

    # Gergely-naptár szerinti értékek a számításhoz
    # forrás: https://hu.wikipedia.org/wiki/H%C3%BAsv%C3%A9tsz%C3%A1m%C3%ADt%C3%A1s#Gauss_m%C3%B3dszere
    M = 24
    N = 5


    if (szam1 >= 1900) and (szam1 <= 2099):
        a = szam1 % 19
        b = szam1 % 4
        c = szam1 % 7
        d = (19*a + M) % 30
        e = (2*b + 4*c + 6*d + N) % 7
        print("A húsvét dátuma: ", end="")
        if d+e < 10:
            nap = d + e + 22
            print("március", str(nap)+".")
        else:
            nap = d + e - 9
            if nap == 26:
                nap = 19
            elif (nap == 25) and (d == 28) and (e == 6) and (a > 10):
                nap = 18
            print("április", str(nap)+".")
    else:
        print("Hiba: az évszám a határértékeken kívül esik!")