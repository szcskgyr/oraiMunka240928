import math


def kor():

    # 13. feladat – Kör
    # A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    r = float(input("Kérem, adja meg a kör sugarát!"))

    if r > 0:
        print("A kör kerülete: ", str(r*2*math.pi))
        print("A kör területe: ", str(r**2*math.pi))
    else:
        print("Hiba: a kör sugara nem pozitív!")
