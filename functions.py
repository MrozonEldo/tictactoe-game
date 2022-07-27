tablica=[["[ ]" for i in range(3)] for j in range(3)]
kolko="[0]"
krzyzyk="[X]"
round_nr=1
def rysujMape(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            print(str(tablica[i][j]),end=' ')
        print()

def isPlayerWin(tablica,sign):
    col=0
    row=0
    for i in range(len(tablica)):
        if i == 0:
            if tablica[i][0] == sign and tablica[1][1] == sign and tablica[2][2] == sign:
                return True
            elif tablica[2][0] == sign and tablica[1][1] == sign and tablica[0][2] == sign:
                return True
        for j in range(len(tablica[i])):
            if tablica[i][j]==krzyzyk:
                row+=1
            if tablica[j][i]==krzyzyk:
                col+=1
        if row == 3:
            return True
        if col == 3:
            return True
        row=0
        col=0
    return False

def isDraw(tablica):
    empty_fields=0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if not(tablica[i][j]==krzyzyk) and not(tablica[i][j]==kolko):
                empty_fields+=1
    if empty_fields>0:
        return False
    else:
        return True

def isTaken(tablica, p1, p2):
    if tablica[int(p1)][int(p2)]==krzyzyk or tablica[int(p1)][int(p2)]==kolko:
        return True
    else:
        return False