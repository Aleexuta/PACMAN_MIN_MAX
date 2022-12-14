from enum import Enum#test
import random
#0-gol
#1-perete
#2-bomboana
#3-fantome
#4-pacman


#folosim astea pt clean code
GOL=0
PERETE=1
BOMBOANA=2


FANTOMA=3
PACMAN=4


#fantomele o sa se miste random
#pacmanul isi va alege pozitia dupa algoritmul min-max alpha beta pruning

matrix=[[2,2,2,1,2,2,2,1,1,2],
        [2,1,2,2,2,1,2,2,1,2],
        [2,1,1,1,1,1,1,2,1,2],
        [2,1,2,2,2,1,2,2,2,2],
        [2,2,2,1,1,1,2,1,2,1],
        [2,1,2,2,1,2,2,1,2,2],
        [2,1,1,2,1,2,1,1,1,2],
        [2,2,2,2,2,2,2,1,2,2],
        [1,1,1,1,1,2,1,1,2,1],
        [2,2,2,2,2,2,2,2,2,2]]

def do_move(move,matrix): # mananca bomboana de pe move
    if move[0] < 0 or move[0] >= N or move[1] < 0 or move[1] >= N:
        return False
 
    if matrix[move[0]][move[1]] == BOMBOANA:
        matrix[move[0]][move[1]] = GOL
        return True
    
    return False
def undo_move(CH,move,matrix): #dam undo la mutare. punem pe move CH( bomboana sau gol)
    if move[0] < 0 or move[0] >= N or move[1] < 0 or move[1] >= N:
        return False
 
    matrix[move[0]][move[1]] = CH
    return True
def print_Matrix(matrix): #afisam matricea in interfata sau normal
    return True

def move_ghost(matrix,ghostPositions): #mutam random fantomele
    # facem random pe pozitii. 0 pt sus, 1 pt dreapta, 2 pt jos, 3 pt stanga
    moved = False
    i=ghostPositions[nr_gh].x
    j=ghostPositions[nr_gh].y
    while not moved:
        pozitie_random = random.randint(0, 3)
        if pozitie_random == 0:
            if (i-1)>=0 and matrix[i-1][j] != PERETE:
                ghostPositions[nr_gh]={'x':i-1,'y':j}
                moved=True
        if pozitie_random == 1:
            if (j+1)<=N and matrix[i][j+1] != PERETE:
                ghostPositions[nr_gh]={'x':i,'y':j+1}
                moved = True
        if pozitie_random == 0:
            if (i+1)<=N and matrix[i+1][j] != PERETE:
                ghostPositions[nr_gh]={'x':i+1,'y':j}
                moved=True
        if pozitie_random == 0:
            if (j-1)>=0 and matrix[i][j-1] != PERETE:
                ghostPositions[nr_gh]={'x':i,'y':j-1}
                moved = True

def check_win(matrix,ghostPositions, pacmanPosition): # verificam daca s-a terminat jocul, nr de bomboane==0, sau pacman este mancat 
    nr_bomboane=0
    for i in range(N):
        for j in range(N):
            if(matrix[i][j]==BOMBOANA):
                nr_bomboane+=1
    
    if nr_bomboane==0:
        return (True,PACMAN)
    
    k=pacmanPosition.x
    l=pacmanPosition.y
    for nr_gh in range(ghost_number):
        i=ghostPositions[nr_gh].x
        j=ghostPositions[nr_gh].y

        if(i==l and j==k):
            return (True,FANTOMA)

    return (False,-1)
    
    


def possible_moves(CH,matrix): # ia toate posibilele mutari ale lui pacman(4) sau ale fantomelor(toate)
    #posibile adica sa nu aiba ziduri si chestii
    #pacman sa nu intre in fantoma
    #returnam o lista cu elem de forma (i,j) de la personajul resp
    return True

#este recursiva, face overthinking
def evaluate_move(matrix,pacmacPosition, ghostPositions, candyConsumed=0,depth=0,isMaximizingPlayer=True): #calculeaza costul mutarii ( arborele) si returneaza cea mai buna alegere 
    #functia de min/max
    #verificam sa nu fie la final ( game over /castig )

    #aici, la frunze e cel mai ciudatel
        # -1000 + depth pierde pacman
        # 1000 - depth + candyConsumed pana aici


    #if daca e isMax=True   ->pacman
        #reapelam functia cu isMax=false
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
        #salvam ce se afla pe viitoarea pozitie
        #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
        #evaluam noua posibila mutare, adaugam +1 la candyConsumed daca pe viitoarea este bomboana
        #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
        #calculam max din valorile
    #else    ->fantoma
        #reapelam functia cu isMax=True
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari fantomelor
        #evaluam noua posibila mutare, matricea nu se schimba 
        #calculam min din valori
    #returnam valoarea cea mai buna
    return True
def move_pacman(matrix,pacmanPosition, ghostPositions):
    
    #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
    #salvam ce se afla pe viitoarea pozitie
    #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
    #evaluam noua posibila mutare
    #candy consumed va fi 0  de la pozitia asta
    #undo la mutare ( adaugam in matrice daca era bomboana sau nu)

    #calculam cea mai buna valoare dintre valorile de la posibilele mutari
    #facem cea mai buna mutare pe tabla noastra (mancam bomboana si pacmanul)
    return False


game_over=False
pacman_pos=(0,0)
ghost_pos=[(0,10),(10,0)]

matrix[pacman_pos[0]][pacman_pos[1]]=0

while not game_over:
    #o sa dam impresia ca pacman si fantoma se misca in acelasi timp pt ca le mutam pe ambele in aceasi iteratie
    move_ghost(matrix, ghost_pos)
    #mutam fantoma
    move_pacman(matrix,pacman_pos,ghost_pos)
    #mutam pacman
    #verificam sa nu se fi terminat jocul
    check_win(matrix,ghost_pos,pacman_pos)
    #afisam matricea
    print_Matrix(matrix)