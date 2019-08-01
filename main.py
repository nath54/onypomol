#coding:utf-8
import random,time,pygame
from pygame.locals import *

class Joueur:
    def __init__(self):
        self.pseudo="pseudo"
        self.argent=0
        self.cases_possedees=[]
        self.caseactu=0
        self.couleur=(250,250,250)

class Propriete:
    def __init__(self):
        self.nom=""
        self.prix=0
        self.prix_hipotheque=0
        self.prix_maison=0
        self.prix_hotel=0
        self.loyer_terrain_nu=0
        self.loyer_1maison=0
        self.loyer_2maison=0
        self.loyer_3maison=0
        self.loyer_4maison=0
        self.loyer_hotel=0

couleurs=[(150,130,20),(20,150,80),(200,90,80),(40,180,50),(20,150,200),(100,70,130),(20,50,130)]

        # NOM                   TYPE  PRIX     COULEUR
cases=[ ["départ"               ,0   ,None     ,None    ],
        ["Pays-Bas"             ,1   ,912.90   ,0       ],
        ["Australie"            ,1   ,14418.28 ,0       ],
        ["chance"               ,3   ,None     ,None    ],
        ["Indonésie"            ,1   ,1022.45  ,1       ],
        ["Mexique"              ,1   ,1223.36  ,1       ],
        ["Prison"               ,5   ,None     ,None    ],
        ["Aéroport"             ,2   ,5000     ,None    ],
        ["Espagne"              ,1   ,1425.87  ,1       ],
        ["Caisse de|communauté" ,4   ,None     ,None    ],
        ["Corée |du Sud"        ,1   ,1619.42  ,2       ],
        ["Russie"               ,1   ,1630.66  ,2       ],
        ["Canada"               ,1   ,1711.39  ,2       ],
        ["Brésil"               ,1   ,1868.18  ,3       ],
        ["Allez ou|vous voulez" ,6   ,1000     ,None    ],
        ["Italie"               ,1   ,2072.20  ,3       ],
        ["Inde"                 ,1   ,2716.75  ,3       ],
        ["Aéroport"             ,2   ,5000     ,None    ],
        ["chance"               ,3   ,None     ,None    ],
        ["France"               ,1   ,2775.25  ,4       ],
        ["Allez en|Prison"      ,8   ,None     ,None    ],
        ["Royaume-Uni"          ,1   ,2828.64  ,4       ],
        ["Allemagne"            ,1   ,4000.39  ,4       ],
        ["Japon"                ,1   ,4971.93  ,5       ],
        ["Chine"                ,1   ,13407.40 ,5       ],
        ["Caisse de|communauté" ,4   ,None     ,None    ],
        ["Union-|Européenne"    ,1   ,18750.05 ,6       ],
        ["Etats-Unis"           ,1   ,20494.05 ,6       ]
]





#############################################

pygame.init()
btex,btey=1280,1024
tex,tey=1280,1024
fenetre=pygame.display.set_mode([tex,tey],pygame.FULLSCREEN)

def rx(x): return int(x/btex*tex)
def ry(y): return int(y/btey*tey)

font=pygame.font.SysFont("Arial",ry(20))

def aff_j(joueurs):
    fenetre.fill((0,0,0))
    e=0
    xx,yy=tex-rx(300),tey-ry(150)
    tcx,tcy=rx(150),ry(100)
    px,py=-1,0
    for c in cases:
        clf=(255,255,255)
        if c[1]==1: clf=couleurs[c[3]]
        pygame.draw.rect(fenetre,clf,(xx,yy,tcx,tcy),0)
        pygame.draw.rect(fenetre,(0,0,0),(xx,yy,tcx,tcy),rx(2))
        h=0
        for tt in c[0].split("|"):
            fenetre.blit(font.render(tt,True,(0,0,0)),[xx+rx(5),yy+ry(5)+h*ry(20)])
            h+=1
        for j in joueurs:
            for cs in j.cases_possedees:
                if cs[0]==cases.index(c): 
                    pygame.draw.rect(fenetre,j.cl,(xx+rx(0),yy+tcy-ry(10),tcx,ry(10)),0)
                    pygame.draw.rect(fenetre,(0,0,0),(xx+rx(0),yy+tcy-ry(10),tcx,ry(10)),1)
        xx+=px*tcx
        yy+=py*tcy
        if e==0 and xx<=rx(100): e,px,py=1,0,-1
        elif e==1 and yy<=rx(100): e,px,py=2,1,0
        elif e==2 and xx>=tex-rx(300): e,px,py=3,0,1
    pygame.display.update()

def main_j():
    encour=True
    r_plateau=pygame.Rect(rx(100),ry(100),rx(800),ry(550))
    joueurs=[]
    j1=Joueur()
    j1.nom="Nathan"
    j1.cl=(0,50,200)
    j1.cases_possedees=[[5],[18]]
    joueurs.append(j1)
    while encour:
        aff_j(joueurs)
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if r_plateau.collidepoint(pos):
                    pass


def aff_menu():
    bts=[]
    for x in range(10): bts.append(None)
    fenetre.fill((0,0,0))
    pass
    pygame.display.update()
    return bts

def menu():
    pass
    encour_m=True
    while encour_m:
        bts=aff_menu()
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour_m=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for b in bts:
                    if b!=None and b.collidepoint(pos):
                        di=bts.index(b)
                        if di==0:
                            main_jeu()
                        
            



main_j()











