def egeszBeolvas():
    szam = float(input("Kérem, adjon meg egy valós számot!"))
    return szam
def teglalap1():

    # 15. feladat – Téglalap1
    # A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"

    a = egeszBeolvas()
    b = egeszBeolvas()

    if (a > 0) and (b > 0):
        kerulet = round(2*(a+b), 2)
        terulet = round(a*b, 2)
        print("A téglalap kerülete:", str(kerulet))
        print("A téglalap területe:", str(terulet))
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")