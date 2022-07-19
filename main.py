from functions import *

print("Witaj w grze kółko i krzyżyk")
while(True):
    rysujMape(tablica)
    if(round_nr%2==1):
        pole=int(input(print("Gracz numer 1 podaje nr pola:")))
        if isTaken(tablica,pole):
            print("Hej, to pole jest zajęte! Zaznacz inne pole.")
            continue
        else:
            tablica[pole]=krzyzyk
    else:
        pole=int(input(print("Gracz numer 2 podaje nr pola:")))
        if isTaken(tablica, pole):
            print("Hej, to pole jest zajęte! Zaznacz inne pole.")
            continue
        else:
            tablica[pole] = kolko
    round_nr+=1
    if isPlayer1Win(tablica)==True:

        print("Gratulacje dla gracza nr 1 !!!")
        break
    elif isDraw(tablica)==True:
        rysujMape(tablica)
        print("REMIS! Spróbujcie jeszcze raz !!!")
        break
    elif isPlayer2Win(tablica)==True:
        rysujMape(tablica)
        print("Gratulacje dla gracza nr 2 !!!")
        break