def row():
    a=[]
    for i in range(0,50):
        a.append("   ")
    return a
global l
l=[]
for i in range(0,25):
    a=row()
    l.insert(0,a)
for i in range(0,25):
        l[i][0]="*"
        l[i][49]="*"
for i in range(0,50):
    l[0][i]="**"
    l[24][i]="**"
def box():
    global l
    print()
    for i in range(0,25):
        for j in range(0,50):
            print(l[i][j],end="")
        print()
#
def level1():
    #
    #    -----           ------                ------
    #   |        |          |          |            |           |
    #   |        |          |          |            |           |
    #   |        |          |          |            |           |
    #    -----            ------              ------
    #
    #    -----           ------              ------
    #   |        |          |          |            |           |
    #   |        |          |          |            |           |
    #   |        |          |          |            |           |
    #    -----            ------              ------
    #
    #
    #
    #
    #
    global l
    for i in range(3,7):
        l[i][2]="|"
        l[i][9]="|"
        l[i][11]="|"
        l[i][17]="|"
    for i in range(3,8):
        l[2][i]=" _"
        l[7][i]=" _"
        l[2][9+i]=" _"
        l[7][9+i]=" _"
level1()
box()








     
