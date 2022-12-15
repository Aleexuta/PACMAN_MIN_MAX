from enum import Enum#test
import numpy as np
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

matrix=[[1,1,1,1,1,1,1,1,1,1,1,1]
        [1,2,2,2,1,2,2,2,1,1,2,1],
        [1,2,1,2,2,2,1,2,2,1,2,1],
        [1,2,1,1,1,1,1,1,2,1,2,1],
        [1,2,1,2,2,2,1,2,2,2,2,1],
        [1,2,2,2,1,1,1,2,1,2,1,1],
        [1,2,1,2,2,1,2,2,1,2,2,1],
        [1,2,1,1,2,1,2,1,1,1,2,1],
        [1,2,2,2,2,2,2,2,1,2,2,1],
        [1,1,1,1,1,1,2,1,1,2,1,1],
        [1,2,2,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]]

def do_move(move,matrix): # mananca bomboana de pe move
    #move e de forma (i,j)
    return True 
def undo_move(CH,move,matrix): #dam undo la mutare. punem pe move CH( bomboana sau gol)
    return True
def print_Matrix(matrix): #afisam matricea in interfata sau normal
    return True

def move_ghost(matrix,ghostPositions): #mutam random fantomele
    return True

def check_win(matrix,ghostPositions, pacmanPosition): # verificam daca s-a terminat jocul, nr de bomboane==0, sau pacman este mancat 
    return False
def possible_moves(CH,matrix): # ia toate posibilele mutari ale lui pacman(4) sau ale fantomelor(toate)
    #posibile adica sa nu aiba ziduri si chestii
    #pacman sa nu intre in fantoma
    #returnam o lista cu elem de forma (i,j) de la personajul resp
    return True

#este recursiva, face overthinking
def evaluate_move(matrix,pacmacPosition, ghostPositions, candyConsumed=0,depth=0,isMaximizingPlayer=True): #calculeaza costul mutarii ( arborele) si returneaza cea mai buna alegere 
    #functia de min/max
    #verificam sa nu fie la final ( game over /castig )
    final,player=check_win(matrix,ghostPositions=ghostPositions,pacmanPosition=pacmacPosition)
    if final==1:
        if player==FANTOMA:
            return 1000-depth
        elif player==PACMAN:
            return depth-1000
    #aici, la frunze e cel mai ciudatel
        # -1000 + depth pierde pacman
        # 1000 - depth + candyConsumed pana aici

    evals=[]
    #if daca e isMax=True   ->pacman
    if isMaximizingPlayer==True:
        #reapelam functia cu isMax=false
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
        moves=possible_moves(PACMAN,matrix,ghost_pos,pacmacPosition)
        for move in moves:
        #salvam ce se afla pe viitoarea pozitie
            old_ch=matrix[move.x][move.y]
        #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
            do_move(move,matrix)
        #evaluam noua posibila mutare, adaugam +1 la candyConsumed daca pe viitoarea este bomboana
            if(old_ch==BOMBOANA):
                 candy=candyConsumed+1
            else:
                 candy=candyConsumed
            evals.append(evaluate_move(matrix,move,ghostPositions,candy,depth+1,False))
        #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
            undo_move(old_ch)
        bestMove=max(evals)
        #calculam max din valorile
    #else    ->fantoma
    else:

        #reapelam functia cu isMax=True
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari fantomelor
        moves=possible_moves(FANTOMA,matrix,ghost_pos,pacmacPosition)
        #evaluam noua posibila mutare, matricea nu se schimba 
        evals.append(evaluate_move(matrix,pacmacPosition,ghostPositions,candyConsumed,depth+1,True))
        #calculam min din valori
        bestMove=min(evals)
    #returnam valoarea cea mai buna
    return bestMove
def move_pacman(matrix,pacmanPosition, ghostPositions):
    
    #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
    #salvam ce se afla pe viitoarea pozitie
    #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
    #evaluam noua posibila mutare
    #candy consumed va fi 0  de la pozitia asta
    #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
    evals=[]
    moves=possible_moves(PACMAN,matrix,ghost_pos,pacmanPosition)
    for move in moves:
    #salvam ce se afla pe viitoarea pozitie
        old_ch=matrix[move.x][move.y]
    #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
        do_move(move,matrix)
    #evaluam noua posibila mutare, adaugam +1 la candyConsumed daca pe viitoarea este bomboana
        if(old_ch==BOMBOANA):
                candy=1
        else:
                candy=0
        evals.append(evaluate_move(matrix,move,ghostPositions,candy,0,False))
    #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
        undo_move(old_ch)
    best_move=moves[np.argmax(evals)]
    do_move(best_move,matrix)
    #calculam cea mai buna valoare dintre valorile de la posibilele mutari
    #facem cea mai buna mutare pe tabla noastra (mancam bomboana si pacmanul)
    return False


game_over=False
pacman_pos={'x':1,'y':1}
ghost_pos=[{'x':1,'y':11},{'x':11,'y':1}]
N=10
matrix[pacman_pos[0]][pacman_pos[1]]=0

while not game_over:
    #o sa dam impresia ca pacman si fantoma se misca in acelasi timp pt ca le mutam pe ambele in aceasi iteratie

    #mutam fantoma
    
    #mutam pacman
    #verificam sa nu se fi terminat jocul

    #afisam matricea
