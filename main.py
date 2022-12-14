from enum import Enum#test
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

def all_ghost_moves():
    #moves=[]

    #posible_moves()
    return True

def possible_moves(CH,matrix,ghost_pos,pacman_pos): # ia toate posibilele mutari ale lui pacman(4) sau ale fantomelor(toate)
    moves=[]



    moves_finalGh=[]
    x=pacman_pos.x
    y=pacman_pos.y
    
            
    if CH==PACMAN :
        if matrix[x+1][y]!=1 :                       #dreapta
            moves.append({'x':x+1,'y':y})
        if matrix[x-1][y]!=1 :                      #stanga
           moves.append({'x':x-1,'y':y})
        if matrix[x][y-1]!=1 :                      #jos
            moves.append({'x':x,'y':y-1})
        if matrix[x][y+1]!=1 :                      #sus
            moves.append({'x':x,'y':y+1})
        return moves

    



    if CH==FANTOMA :
        for i in ghost_number:
            moves_ghost=[{}]
            x_ghs=ghost_pos[i].x
            y_ghs=ghost_pos[i].y
            moves=[]

        # facem combiari 4 cate nr de fantome 

            if matrix[x_ghs+1][y_ghs]!=1 :                       #dreapta
               moves.append({'x':x_ghs+1,'y':y_ghs})
            if matrix[x_ghs-1][y_ghs]!=1 :                      #stanga
               moves.append({'x':x_ghs-1,'y':y_ghs})
            if matrix[x_ghs][y_ghs-1]!=1 :                      #jos
               moves.append({'x':x_ghs,'y':y_ghs-1})
            if matrix[x_ghs][y_ghs+1]!=1 :                      #sus
               moves.append({'x':x_ghs,'y':y_ghs+1})
            moves_ghost.append(moves)        
    


    return moves_ghost



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

pacman_pos={'x':1,'y':1}
ghost_pos=[{'x':1,'y':11},{'x':11,'y':1}]
#ghost_pos[1].x

N=10
ghost_number=2
matrix[pacman_pos[0]][pacman_pos[1]]=0

while not game_over:
    #o sa dam impresia ca pacman si fantoma se misca in acelasi timp pt ca le mutam pe ambele in aceasi iteratie

    #mutam fantoma
    
    #mutam pacman
    #verificam sa nu se fi terminat jocul

    #afisam matricea
