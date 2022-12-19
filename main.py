from turtle import Screen
from pylab import *
from enum import Enum#test
import random
import numpy as np
from itertools import combinations_with_replacement
import sys
import copy
import pygame
from pygame.locals import *
import os

absolute_path = os.path.dirname(__file__)
relative_path = "images"
full_path = os.path.join(absolute_path, relative_path)
sys.setrecursionlimit(10000) 
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


stateSteps=[]
#fantomele o sa se miste random
#pacmanul isi va alege pozitia dupa algoritmul min-max alpha beta pruning

matrix=[[1,1,1,1,1,1,1,1,1,1,1,1],
        [1,2,2,2,1,2,2,2,1,1,2,1],
        [1,2,1,2,2,2,1,2,2,2,2,1],
        [1,2,1,1,1,1,1,1,2,1,2,1],
        [1,2,1,2,2,2,1,2,2,2,2,1],
        [1,2,2,2,1,1,1,2,1,2,1,1],
        [1,2,1,2,2,1,2,2,1,2,2,1],
        [1,2,1,1,2,1,2,1,1,1,2,1],
        [1,2,2,2,2,2,2,2,1,2,2,1],
        [1,2,2,1,1,1,2,2,1,2,1,1],
        [1,2,2,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]]
minMatrix=[[1,1,1,1,1],
            [1,2,2,2,1],
            [1,2,2,2,1],
            [1,2,2,2,1],
            [1,1,1,1,1]]
def do_move(move,matrix): # mananca bomboana de pe move
    if move['x'] < 0 or move['x'] >= N or move['y'] < 0 or move['y'] >= N:
        return False
 
    if matrix[move['x']][move['y']] == BOMBOANA:
        matrix[move['x']][move['y']] = GOL
        return True
    
    return False
def undo_move(CH,move,matrix): #dam undo la mutare. punem pe move CH( bomboana sau gol)
    if move['x'] < 0 or move['x'] >= N or move['y'] < 0 or move['y'] >= N:
        return False
 
    matrix[move['x']][move['y']] = CH
    return True
titleSize=48
tile_dict = {0: pygame.image.load(full_path+"\gray.png"),    1: pygame.image.load(full_path+"\\brick.png"), 
    2: pygame.image.load(full_path+"\\bomboana.png"), 3: pygame.image.load(full_path+"\\fantoma.png"),
    4: pygame.image.load(full_path+"\pacman.png")}
for x in range(5):
    tile_dict[x]=pygame.transform.scale(tile_dict[x],(titleSize,titleSize))
def printGraphic(matrix):
    tileX = 0
    tileY = 0
   
    screen = pygame.display.set_mode((600,600))
    for x in matrix:
        tileX = 0
        for x in x:
            if x == 0:
                screen.blit(tile_dict[0], (tileX, tileY))
                tileX = tileX+titleSize
            if x == 1:
                screen.blit(tile_dict[1], (tileX, tileY))
                tileX = tileX+titleSize
            if x== 2:
                screen.blit(tile_dict[0], (tileX, tileY))
                screen.blit(tile_dict[2], (tileX, tileY))
                tileX = tileX+titleSize
            if x==3:
                screen.blit(tile_dict[0], (tileX, tileY))
                screen.blit(tile_dict[3], (tileX, tileY))
                tileX = tileX+titleSize
            if x==4:
                screen.blit(tile_dict[0], (tileX, tileY))
                screen.blit(tile_dict[4], (tileX, tileY))
                tileX = tileX+titleSize
            
        tileY += titleSize
    pygame.time.wait(100)
def print_Matrix(matrix): #afisam matricea in interfata sau normal

    newMatrix=copy.deepcopy(matrix)
    newMatrix[pacman_pos['x']][pacman_pos['y']]=PACMAN
    for i in range(ghost_number):
         newMatrix[ghost_pos[i]['x']][ghost_pos[i]['y']]=FANTOMA
    for i in range(N):
        print(newMatrix[i])
    print(pacman_pos)
    print(ghost_pos)
    printGraphic(newMatrix)
    print("\n\n")
def is_ghost_move_valid(ghostPosition,actualGhost,newMove):
    for i in range(ghost_number):
        if(i!=actualGhost):
            if(newMove['x']==ghostPosition[i]['x'] and newMove['y']==ghostPosition[i]['y']):
                return False
    return True
def move_ghost(matrix,ghostPositions): #mutam random fantomele
    # facem random pe pozitii. 0 pt sus, 1 pt dreapta, 2 pt jos, 3 pt stanga
    for nr_gh in range(ghost_number):
        moved = False
        i=ghostPositions[nr_gh]['x']
        j=ghostPositions[nr_gh]['y']
        invalid_pos=0
        while not moved:
            pozitie_random = random.randint(0, 100)
            pozitie_random=pozitie_random%4
            if pozitie_random == 0:
                if (i-1)>=0 and matrix[i-1][j] != PERETE:
                    if(is_ghost_move_valid(ghostPositions,nr_gh,{'x':i-1,'y':j})):
                        ghostPositions[nr_gh]={'x':i-1,'y':j}
                        moved=True
                    else: invalid_pos+=1
            if pozitie_random == 1:
                if (j+1)<=N and matrix[i][j+1] != PERETE:
                    if(is_ghost_move_valid(ghostPositions,nr_gh,{'x':i,'y':j+1})):
                        ghostPositions[nr_gh]={'x':i,'y':j+1}
                        moved = True
                    else: invalid_pos+=1
            if pozitie_random == 2:
                if (i+1)<=N and matrix[i+1][j] != PERETE:
                    if(is_ghost_move_valid(ghostPositions,nr_gh,{'x':i+1,'y':j})):
                        ghostPositions[nr_gh]={'x':i+1,'y':j}
                        moved=True
                    else: invalid_pos+=1
            if pozitie_random == 3:
                if (j-1)>=0 and matrix[i][j-1] != PERETE:
                    if(is_ghost_move_valid(ghostPositions,nr_gh,{'x':i,'y':j-1})):
                        ghostPositions[nr_gh]={'x':i,'y':j-1}
                        moved = True
                    else: invalid_pos+=1
            if( invalid_pos==4):
                moved=True
    return ghostPositions
def check_win(matrix,ghostPositions, pacmanPosition,inEvaluate=True): # verificam daca s-a terminat jocul, nr de bomboane==0, sau pacman este mancat 

   
    
    k=pacmanPosition['x']
    l=pacmanPosition['y']
    for nr_gh in range(ghost_number):
        i=ghostPositions[nr_gh]['x']
        j=ghostPositions[nr_gh]['y']

        if(j==l and i==k):
            return (True,FANTOMA)
    nr_bomboane=0
    for i in range(N):
        for j in range(N):
            if(matrix[i][j]==BOMBOANA):
                nr_bomboane+=1
    
    if nr_bomboane==0:
        return (True,PACMAN)
    return (False,-1)
    
    

def all_ghost_moves():

    moves=combinations_with_replacement([0,1,2,3],ghost_number)

    #posible_moves()
    return moves
def isInList(move):
    for mv in stateSteps:
        if mv['x']==move['x'] and mv['y']==move['y']:
            return True
    return False
def possible_moves(CH,matrix,ghost_pos,pacman_pos): # ia toate posibilele mutari ale lui pacman(4) sau ale fantomelor(toate)
    moves=[]

    x=pacman_pos['x']
    y=pacman_pos['y']
            
    if CH==PACMAN :
        if matrix[x+1][y]!=PERETE :                       #jos
            moves.append({'x':x+1,'y':y})
        if matrix[x-1][y]!=PERETE :                      #sus
           moves.append({'x':x-1,'y':y})
        if matrix[x][y-1]!=PERETE :                      #stanga
            moves.append({'x':x,'y':y-1})
        if matrix[x][y+1]!=PERETE :                      #dreapta
            moves.append({'x':x,'y':y+1})
        return moves
    if CH==FANTOMA :
        combinations=all_ghost_moves()
        moves_ghost_position=[]
        for i in range(ghost_number):
           
            x_ghs=ghost_pos[i]['x']
            y_ghs=ghost_pos[i]['y']
            moves=[]

            if matrix[x_ghs+1][y_ghs]!=1 :                       #dreapta
               moves.append({'x':x_ghs+1,'y':y_ghs})
            if matrix[x_ghs-1][y_ghs]!=1 :                      #stanga
               moves.append({'x':x_ghs-1,'y':y_ghs})
            if matrix[x_ghs][y_ghs-1]!=1 :                      #jos
               moves.append({'x':x_ghs,'y':y_ghs-1})
            if matrix[x_ghs][y_ghs+1]!=1 :                      #sus
               moves.append({'x':x_ghs,'y':y_ghs+1})
            moves_ghost_position.append(moves)        
        all_moves=[]
        for comb in list(combinations):
            state=[]
            isok=True
            for gh in range(ghost_number):
                if(comb[gh]>=len(moves_ghost_position[gh])):
                    isok=False
            if(isok):
                for gh in range(ghost_number):
                    state.append(moves_ghost_position[gh][comb[gh]])
                all_moves.append(state)
        return all_moves

#este recursiva, face overthinking
def evaluate_move(matrix, pacmacPosition, ghostPositions, alpha, beta,candyConsumed=0,depth=0,isMaximizingPlayer=True): #calculeaza costul mutarii ( arborele) si returneaza cea mai buna alegere 
    #functia de min/max
    #verificam sa nu fie la final ( game over /castig )
    final,player=check_win(matrix,ghostPositions=ghostPositions,pacmanPosition=pacmacPosition)
    if final==1:
        if player==FANTOMA:
            return -100+depth
        elif player==PACMAN:
            return -depth+100+2*candyConsumed
        else:
            return -depth+2*candyConsumed
    if depth >8:
        return depth+2*candyConsumed
    #aici, la frunze e cel mai ciudatel
        # -1000 + depth pierde pacman
        # 1000 - depth + candyConsumed pana aici

    evals=[]
    #if daca e isMax=True   ->pacman
    if isMaximizingPlayer==True:
        maxEval=-10000
        #reapelam functia cu isMax=false
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
        moves=possible_moves(PACMAN,matrix,ghostPositions,pacmacPosition)
        for move in moves:
        #salvam ce se afla pe viitoarea pozitie
            old_ch=matrix[move['x']][move['y']]
        #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
            do_move(move,matrix)
        #evaluam noua posibila mutare, adaugam +1 la candyConsumed daca pe viitoarea este bomboana
            if(old_ch==BOMBOANA):
                 candy=candyConsumed+1
            else:
                 candy=candyConsumed
            eval=evaluate_move(matrix,move,ghostPositions,alpha,beta,candy,depth+1,False)
        #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
            undo_move(old_ch,move,matrix)
            maxEval=max(maxEval,eval)
            alpha=max(alpha,eval)
            if(beta <= alpha):
                break
        bestMove= maxEval
        #calculam max din valorile
    #else    ->fantoma
    else:
        minEval=10000
        #reapelam functia cu isMax=True
        #merge pe acelasi principiu ca la move.
        #luam toate posibilele mutari fantomelor
        moves=possible_moves(FANTOMA,matrix,ghostPositions,pacmacPosition)
        for move in moves:
        #evaluam noua posibila mutare, matricea nu se schimba 
            eval=evaluate_move(matrix, pacmacPosition, move, alpha, beta, candyConsumed, depth+1, True)
        #calculam min din valori
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if(beta<=alpha):
                break
        bestMove=minEval
    #returnam valoarea cea mai buna
    return bestMove
def move_pacman(matrix,pacmanPosition, ghostPositions,alpha,beta):
    
    #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
    #salvam ce se afla pe viitoarea pozitie
    #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
    #evaluam noua posibila mutare
    #candy consumed va fi 0  de la pozitia asta
    #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
    
    maxEval=-10000
    evals=[]
    #reapelam functia cu isMax=false
    #merge pe acelasi principiu ca la move.
    #luam toate posibilele mutari pacman ( lista cu pozitile de la pacman )
    moves=possible_moves(PACMAN,matrix,ghost_pos,pacmanPosition)
    for move in moves:
    #salvam ce se afla pe viitoarea pozitie
        old_ch=matrix[move['x']][move['y']]
    #facem mutare, punem pe noua pozitia a pacmanului, ca e GOL
        do_move(move,matrix)
    #evaluam noua posibila mutare, adaugam +1 la candyConsumed daca pe viitoarea este bomboana
        if(old_ch==BOMBOANA):
                candy=1
        else:
                candy=0
        eval=evaluate_move(matrix,move,ghostPositions,alpha,beta,candy,0,False)
        evals.append(eval)
    #undo la mutare ( adaugam in matrice daca era bomboana sau nu)
        undo_move(old_ch,move,matrix)
        maxEval=max(maxEval,eval)
        alpha=max(alpha,eval)
        if(beta <= alpha):
            break
    #random.shuffle(moves)

    print(str(pacman_pos)+' -> '+ str(evals)+' // ' +str(stateSteps))
    best_move=moves[np.argmax(evals)]
    while isInList(best_move) and len(moves)>1:
        o=np.argmax(evals)
        only_pos = [num for num in evals if num >= 1]
        pos_count = len(only_pos)
        if(pos_count<=1):
            break
        del moves[o]
        del evals[o]
        print(str(pacman_pos)+' -> '+ str(evals))
        best_move=moves[np.argmax(evals)]
    do_move(best_move,matrix)
    #calculam cea mai buna valoare dintre valorile de la posibilele mutari
    #facem cea mai buna mutare pe tabla noastra (mancam bomboana si pacmanul)

    return best_move
#TODO
def PointsForPacman(matrix):
    return 0
game_over=False

pacman_pos={'x':1,'y':1}
ghost_pos=[{'x':10,'y':1},{'x':10,'y':3},{'x':5,'y':5}]
#ghost_pos[1].x
N=12
ghost_number=2
matrix[pacman_pos['x']][pacman_pos['y']]=0
TotalStates=[]
print_Matrix(matrix)
while not game_over:
    
    pygame.display.flip()
    #o sa dam impresia ca pacman si fantoma se misca in acelasi timp pt ca le mutam pe ambele in aceasi iteratie
    ghost_pos=move_ghost(matrix, ghost_pos)
    
    game_over, cast=check_win(matrix,ghost_pos,pacman_pos,False)
    #mutam fantoma
    if not game_over:
        pacman_pos=move_pacman(matrix,pacman_pos,ghost_pos,-10000,10000)
        stateSteps.append(pacman_pos)
        #mutam pacman
        #verificam sa nu se fi terminat jocul
        game_over, cast= check_win(matrix,ghost_pos,pacman_pos,False)

    #afisam matricea
    print_Matrix(matrix)
    if len(stateSteps) >10:
        stateSteps.pop(0)
if(cast==3):
    print("Game Over")
else: 
    print("Winner")
print(PointsForPacman(matrix))