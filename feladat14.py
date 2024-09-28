def kocka():

    # 14. feladat – Kocka
    # A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza. A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra! Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kocka élének hossza nem pozitív!"!

    el = int(input("Kérem, adjon meg egy él értéket!"))

    if el > 0:
        felszin = 6*el**2
        terfogat = pow(el, 3)
        print("A kocka felszíne:", str(felszin))
        print("A kocka térfogata:", str(terfogat))
    else:
        print("Hiba: a kocka élének hossza nem pozitív!")