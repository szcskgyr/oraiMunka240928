def honap():

# 5. feladat – HónapNév
# A program olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!

    szam1 = int(input("Kérem, adjon meg egy hónap sorszámot!"))

    if (szam1 >= 1) and (szam1 <= 12):
        if szam1 == 1:
            print("január")
        elif szam1 == 2:
            print("február")
        elif szam1 == 3:
            print("március")
        elif szam1 == 4:
            print("április")
        elif szam1 == 5:
            print("május")
        elif szam1 == 6:
            print("június")
        elif szam1 == 7:
            print("július")
        elif szam1 == 8:
            print("augusztus")
        elif szam1 == 9:
            print("szeptember")
        elif szam1 == 10:
            print("október")
        elif szam1 == 11:
            print("november")
        elif szam1 == 12:
            print("december")
    else:
        print("érvénytelen hónap!")
