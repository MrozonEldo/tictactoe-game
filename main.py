def rysujMape(tablica):
    print(str(tablica[0]) + str(tablica[1]) + str(tablica[2]))
    print(str(tablica[3]) + str(tablica[4]) + str(tablica[5]))
    print(str(tablica[6]) + str(tablica[7]) + str(tablica[8]))

def isPlayer1Win(t):
    if t[0]==krzyzyk and t[4]==krzyzyk and t[8]==krzyzyk:
        return True
    elif t[2]==krzyzyk and t[4]==krzyzyk and t[6]==krzyzyk:
        return True
    elif t[0] == krzyzyk and t[1] == krzyzyk and t[2] == krzyzyk:
        return True
    elif t[3] == krzyzyk and t[4] == krzyzyk and t[5] == krzyzyk:
        return True
    elif t[6] == krzyzyk and t[7] == krzyzyk and t[8] == krzyzyk:
        return True
    elif t[0] == krzyzyk and t[3] == krzyzyk and t[6] == krzyzyk:
        return True
    elif t[1] == krzyzyk and t[4] == krzyzyk and t[7] == krzyzyk:
        return True
    elif t[2] == krzyzyk and t[5] == krzyzyk and t[8] == krzyzyk:
        return True
    else:
        return False
def isPlayer2Win(t):
    if t[0] == kolko and t[4] == kolko and t[8] == kolko:
        return True
    elif t[2] == kolko and t[4] == kolko and t[6] == kolko:
        return True
    elif t[0] == kolko and t[1] == kolko and t[2] == kolko:
        return True
    elif t[3] == kolko and t[4] == kolko and t[5] == kolko:
        return True
    elif t[6] == kolko and t[7] == kolko and t[8] == kolko:
        return True
    elif t[0] == kolko and t[3] == kolko and t[6] == kolko:
        return True
    elif t[1] == kolko and t[4] == kolko and t[7] == kolko:
        return True
    elif t[2] == kolko and t[5] == kolko and t[8] == kolko:
        return True
    else:
        return False
def isDraw(t):
    empty_fields=0
    for index in t:
        if not(index==krzyzyk) and not(index==kolko):
            empty_fields+=1
    if empty_fields>0:
        return False
    else:
        return True
def isTaken(t,p):
    if t[p]==krzyzyk or t[p]==kolko:
        return True
    else:
        return False
print("Witaj w grze kółko i krzyżyk")
tablica=[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]]
kolko="['0']"
krzyzyk="['X']"
round_nr=1

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