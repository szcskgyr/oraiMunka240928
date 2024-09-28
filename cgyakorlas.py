# 3. Írasd ki a számokat egyesével 0-tól 20-ig! (a 20-at is!)
def haromA():
    for i in range(21):
        print(i, end=" ")

def haromB():
    i = 0
    while i < 21:
        print(i, end=" ")
        i += 1

# 4. Írasd ki a számokat kettesével 20-tól 56-ig! (az 56-ot is!)
def negy():
    for i in range(20,57,2):
        print(i, end=" ")

# 5. Írasd ki a számokat 4-esével 77-től -77-ig!
def ot():
    for i in range(77,-77,-4):
        print(i, end=" ")

# 6. Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

def beolvas():
    szam = int(input("Kérem, adjon meg egy egész számot!"))
    return szam

def hat():
    szam1 = beolvas()
    szam2 = beolvas()

    # szam1 legyen mindig kisebb, mint szam2
    if szam2 < szam1:
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1,szam2+1,1):
        print(i, end=" ")

# 7. Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1*szam2

    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1, 1):
            print(i, end=" ")

# 8. Írd meg a fenti feladatot while és for ciklussal is!
def nyolc():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    i = 0

    if szorzat < 0:
        while i > szorzat-1:
            print(i, end=" ")
            i -= 1
    else:
        while i < szorzat+1:
            print(i, end=" ")
            i += 1

# 9. Írasd ki az első 7 pozitív egész számot vesszővel elválasztva!
# a. úgy, hogy a végén ne legyen vessző!
