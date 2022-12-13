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

matrix=[[],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []]

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


while not game_over:
    #o sa dam impresia ca pacman si fantoma se misca in acelasi timp pt ca le mutam pe ambele in aceasi iteratie

    #mutam fantoma
    
    #mutam pacman
    #verificam sa nu se fi terminat jocul

    #afisam matricea
