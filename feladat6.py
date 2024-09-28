def szog():

# 6. feladat – Szögtípus
# A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!

    szam1 = float(input("Adj meg egy valós számot!"))

    if (szam1 >= 0) and (szam1 <= 360):
        if szam1 == 0:
            print(str(szam1)+" -> nullszög")
        elif szam1 < 90:
            print(str(szam1)+" -> hegyesszög")
        elif szam1 == 90:
            print(str(szam1)+" -> derékszög")
        elif (szam1 > 90) and (szam1 < 180):
            print(str(szam1)+" -> tompaszög")
        elif szam1 == 180:
            print(str(szam1)+" -> egyenesszög")
        elif (szam1 > 180) and (szam1 < 360):
            print(str(szam1)+" -> homorúszög")
        elif szam1 == 360:
            print(str(szam1)+" -> teljesszög")
    else:
        print("Hibás szög érték!")