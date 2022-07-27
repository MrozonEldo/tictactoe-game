from functions import *

print("Witaj w grze kółko i krzyżyk")
while(True):
    rysujMape(tablica)
    if(round_nr%2==1):
        p1,p2=input(print("Gracz numer 1 podaje nr pola:")).split()
        if isTaken(tablica,p1,p2):
            print("Hej, to pole jest zajęte! Zaznacz inne pole.")
            continue
        tablica[int(p1)][int(p2)]=krzyzyk
    else:
        p1,p2=input(print("Gracz numer 2 podaje nr pola:")).split()
        if isTaken(tablica,p1,p2):
            print("Hej, to pole jest zajęte! Zaznacz inne pole.")
            continue
        tablica[int(p1)][int(p2)] = kolko
    round_nr+=1
    if isPlayerWin(tablica,krzyzyk):
        rysujMape(tablica)
        print("Gratulacje dla gracza nr 1 !!!")
        break
    elif isPlayerWin(tablica,kolko):
        rysujMape(tablica)
        print("Gratulacje dla gracza nr 2 !!!")
        break
    elif isDraw(tablica):
        rysujMape(tablica)
        print("REMIS! Spróbujcie jeszcze raz !!!")
        break