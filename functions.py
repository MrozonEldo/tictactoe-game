tablica=[["[ ]" for i in range(3)] for j in range(3)]
kolko="[0]"
krzyzyk="[X]"
round_nr=1
def rysujMape(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            print(str(tablica[i][j]),end=' ')
        print()


def isPlayer1Win(tablica):
    xcol=0
    xrow=0
    for i in range(len(tablica)):
        if i == 0:
            if tablica[i][0] == krzyzyk and tablica[1][1] == krzyzyk and tablica[2][2] == krzyzyk:
                return True
            elif tablica[2][0] == krzyzyk and tablica[1][1] == krzyzyk and tablica[0][2] == krzyzyk:
                return True
        for j in range(len(tablica[i])):
            if tablica[i][j]==krzyzyk:
                xrow+=1
            if tablica[j][i]==krzyzyk:
                xcol+=1
        if xrow == 3:
            return True
        if xcol == 3:
            return True
        xrow=0
        xcol=0
    return False

def isPlayer2Win(tablica):
    orow = 0
    ocol = 0
    for i in range(len(tablica)):
        if i == 0:
            if tablica[i][0] == kolko and tablica[1][1] == kolko and tablica[2][2] == kolko:
                return True
            elif tablica[2][0] == kolko and tablica[1][1] == kolko and tablica[0][2] == kolko:
                return True
        for j in range(len(tablica[i])):
            if tablica[i][j] == kolko:
                orow += 1
            if tablica[j][i] == kolko:
                ocol+=1
        if orow == 3:
            return True
        if ocol == 3:
            return True
        orow = 0
        ocol = 0
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