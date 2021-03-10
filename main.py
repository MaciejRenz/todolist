def wyswietl():
    suma = len(a)
    print(a)
    print("Zadan na liscie:", suma)


def dodaj(nazwa):
    a.append(nazwa)


def usun(indeks):
    suma = len(a)
    if suma == 0:
        print("Lista nie ma zadan..")
        input("Enter aby kontynuowac...")
    elif indeks < 0 or indeks > (suma - 1):
        print("Nie istnieje zadanie o takim numerze!")
        input("Enter aby kontynuowac...")
    else:
        del a[indeks]


def edytuj(nazwa1, indeks1):
    suma = len(a)
    if suma == 0:
        print("Lista nie ma zadan..")
        input("Enter aby kontynuowac...")
    elif indeks1 < 0 or indeks1 > (suma - 1):
        print("Nie istnieje zadanie o takim numerze!")
        input("Enter aby kontynuowac...")
    else:
        a[indeks1] = nazwa1


def menu():
    print("---------------------------")
    print("|1.Wyswietl liste zadan   |")
    print("|2.Dodaj zadanie do listy |")
    print("|3.Usun zadanie z listy   |")
    print("|4.Edytuj zadanie z listy |")
    print("|5.Koniec                 |")
    print("---------------------------")
    x = input("Wybierz opcje:")
    if x == '1':
        wyswietl()
        input("Enter aby kontynuowac...")
        menu()
    elif x == '2':
        nazwa = input("Nazwa zadania:")
        dodaj(nazwa)
        menu()
    elif x == "3":
        indeks = int(input("Numer zadania:"))
        usun(indeks)
        menu()
    elif x == '4':
        indeks1 = int(input("Numer zadania:"))
        nazwa1 = input("Nowa nazwa zadania:")
        edytuj(nazwa1, indeks1)
        menu()
    elif x == '5':
        exit()
    else:
        print("Nie ma takiej opcji")
        input("Enter aby kontynuowac...")
        menu()


a = []
menu()
