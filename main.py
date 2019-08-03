#coding:utf-8
import random,time,pygame
from pygame.locals import *

class Joueur:
    def __init__(self,pseudo,cl):
        self.pseudo=pseudo
        self.argent=40000
        self.cases_possedees=[]
        self.caseactu=0
        self.couleur=cl
        self.cl=self.couleur
        self.emprisone=False
        self.perdu=False
        self.dprison=0

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

def rcl(): return ( random.randint(0,255) , random.randint(0,255) , random.randint(0,255) )

#effets :
#1=Le joueur gagne de l'argent
#2=le joueur perd de l'argent
#4=le joueur recule
#3=le joueur avance
#5=le joueur va sur une case
#6=le joueur va en prison
#7=le joueur doit faire des réparations sur ses maisons
#8=le joueur doit faire des réparations sur ses hotels
cartes_chances=[ ["Vous gagnez 5 M $",1,5],
                 ["Vous gagnez 10 M $",1,10],
                 ["Vous gagnez 50 M $",1,50],
                 ["Vous gagnez 100 M $",1,100],
                 ["Vous gagnez 500 M $",1,500],
                 ["Vous gagnez 1000 M $",1,1000],
                 ["Vous gagnez 5000 M $",1,5000],
                 ["Vous perdez 5 M $",2,5],
                 ["Vous perdez 10 M $",2,10],
                 ["Vous perdez 50 M $",2,50],
                 ["Vous perdez 100 M $",2,100],
                 ["Vous perdez 500 M $",2,500],
                 ["Vous perdez 1000 M $",2,1000],
                 ["Vous perdez 5000 M $",2,5000],
                 ["Vous reculez d'1 case",4,1],
                 ["Vous reculez de 2 case",4,2],
                 ["Vous reculez de 3 case",4,3],
                 ["Vous reculez de 4 case",4,4],
                 ["Vous reculez de 5 case",4,5],
                 ["Vous avancez d'1 case",3,1],
                 ["Vous avancez de 2 case",3,2],
                 ["Vous avancez de 3 case",3,3],
                 ["Vous avancez de 4 case",3,4],
                 ["Vous avancez de 5 case",3,5],
                 ["Vous allez sur la case 1",5,1],
                 ["Vous allez sur la case 2",5,2],
                 ["Vous allez sur la case 4",5,4],
                 ["Vous allez sur la case 5",5,5],
                 ["Vous allez sur la case 8",5,8],
                 ["Vous allez sur la case 10",5,10],
                 ["Vous allez sur la case 11",5,11],
                 ["Vous allez sur la case 12",5,12],
                 ["Vous allez sur la case 13",5,13],
                 ["Vous allez sur la case 15",5,15],
                 ["Vous allez sur la case 16",5,16],
                 ["Vous allez sur la case 19",5,19],
                 ["Vous allez sur la case 20",5,20],
                 ["Vous allez sur la case 21",5,20],
                 ["Vous allez sur la case 22",5,20],
                 ["Vous allez sur la case 23",5,20],
                 ["Vous allez sur la case 24",5,20],
                 ["Vous allez sur la case 25",5,20],
                 ["Vous allez sur la case 26",5,20],
                 ["Vous allez sur la case 27",5,20],
                 ["Vous allez en prison",6,0],
                 ["Vous devez faire des réparations| vous devez payer 1000 M $ pour chaque maison",7],
                 ["Vous devez faire des réparations| vous devez payer 5000 M $ pour chaque hotel",8]
]





couleurs=[(150,130,20),(20,150,80),(200,90,80),(40,180,50),(20,150,200),(100,70,130),(20,50,130)]
        # NOM                   TYPE  PRIX     COULEUR/IMAGE        PRIX TERRAIN NU   PRIX1MAISON   PRIX2MAISON   PRIX3MAISON   PRIX4MAISON    PRIXHOTEL   COUTMAISON   COUTHOTEL  
cases=[ ["départ"               ,0   ,None     ,"cdep.png"          ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Pays-Bas"             ,1   ,912.90   ,0                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Australie"            ,1   ,1418.28  ,0                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["chance"               ,3   ,None     ,"cchance.png"       ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Indonésie"            ,1   ,1022.45  ,1                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Mexique"              ,1   ,1223.36  ,1                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Prison"               ,5   ,None     ,"cprison.png"       ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Aéroport"             ,2   ,5000     ,"cavion.png"        ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Espagne"              ,1   ,1425.87  ,1                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["chance"               ,3   ,None     ,"cchance.png"       ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Corée |du Sud"        ,1   ,1619.42  ,2                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Russie"               ,1   ,1630.66  ,2                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Canada"               ,1   ,1711.39  ,2                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Brésil"               ,1   ,1868.18  ,3                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Allez ou|vous voulez" ,6   ,1000     ,None                ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Italie"               ,1   ,2072.20  ,3                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Inde"                 ,1   ,2716.75  ,3                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Aéroport"             ,2   ,5000     ,"cavion.png"        ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["chance"               ,3   ,None     ,"cchance.png"       ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["France"               ,1   ,2775.25  ,4                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Allez en|Prison"      ,8   ,None     ,"callerprison.png"  ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Royaume-Uni"          ,1   ,2828.64  ,4                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Allemagne"            ,1   ,4000.39  ,4                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Japon"                ,1   ,4971.93  ,5                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Chine"                ,1   ,13407.40 ,5                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["chance"               ,3   ,None     ,"cchance.png"       ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Union-|Européenne"    ,1   ,18750.05 ,6                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0],
        ["Etats-Unis"           ,1   ,20494.05 ,6                   ,0             ,0         ,0         ,0         ,0          ,0       ,0        ,0]
]

nbprop=0
for c in cases:
    if c[1] in [1,2]: nbprop+=1
    if c[1]==1:
        c[4]=c[2]*0.25
        c[5]=c[2]*0.5
        c[6]=c[2]*1.5
        c[7]=c[2]*2.25
        c[8]=c[2]*3.5
        c[9]=c[2]*5
        c[10]=c[2]*0.25
        c[11]=c[2]*0.5
        

#############################################

pygame.init()
btex,btey=1280,1024
tex,tey=1280,1024
fenetre=pygame.display.set_mode([tex,tey],pygame.FULLSCREEN)

def rx(x): return int(x/btex*tex)
def ry(y): return int(y/btey*tey)

font=pygame.font.SysFont("Arial",ry(20))
font2=pygame.font.SysFont("Arial",ry(16))
font3=pygame.font.SysFont("Arial",ry(30))
font4=pygame.font.SysFont("Arial",ry(50))

dimg="images/"

tcx,tcy=rx(150),ry(100)

for c in cases:
    if type(c[3])==str: c[3]=pygame.transform.scale( pygame.image.load(dimg+c[3]), [tcx,tcy] )

##

def aff_pyinput(txt,inp):
    pygame.draw.rect(fenetre,(100,100,100),(rx(300),ry(400),rx(600),ry(300)),0)
    pygame.draw.rect(fenetre,(255,255,255),(rx(400),ry(500),rx(400),ry(60)),0)
    fenetre.blit( font.render(txt,True,(255,255,255)) , [rx(500),ry(430)])
    fenetre.blit( font.render(inp,True,(0,0,0)) , [rx(450),ry(515)])
    fenetre.blit( font.render("Appuyez sur entrée pour continuer",True,(255,255,255)) , [rx(400),ry(600)])
    pygame.display.update()
ke={K_a:"a",K_b:"b",K_c:"c",K_d:"d",K_e:"e",K_f:"f",K_g:"g",K_h:"h",K_i:"i",K_j:"j",K_k:"k",K_l:"l",K_m:"m",K_n:"n",K_o:"o",K_p:"p",K_q:"q",K_r:"r",K_s:"s",K_t:"t",K_u:"u",K_v:"v",K_w:"w",K_x:"x",K_y:"y",K_z:"z",K_KP0:"0",K_KP1:"1",K_KP2:"2",K_KP3:"3",K_KP4:"4",K_KP5:"5",K_KP6:"6",K_KP7:"7",K_KP8:"8",K_KP9:"9",K_SPACE:" "}
def pynput(txt):
    inp,limcar,encour_i,affcurs,taffc,daffc="",64,True,True,0.4,time.time()
    while encour_i:
        if time.time()-daffc >= taffc: affcurs,daffc=not affcurs,time.time()
        if affcurs: aff_pyinput(txt,inp+"|")
        else: aff_pyinput(txt,inp)
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                v,k=ke.get(event.key),None
                if v!=None: k=v
                elif event.key==K_BACKSPACE: inp=inp[:-1]
                elif event.key==K_RETURN: return inp
                if k!=None and ( pygame.key.get_pressed()[K_LSHIFT] or pygame.key.get_pressed()[K_RSHIFT]): k=k.upper()
                if k!=None and len(inp) < limcar : inp+=k

def lancerdes():
    nbd=2
    mind,maxd=1,4
    nbfr=30
    td=rx(50)
    des=[]
    dchg=time.time()
    tbg=0.2
    dbg=time.time()
    tchg=0.7
    for x in range(nbd):
        des.append( [random.randint(mind,maxd),random.randint(rx(100),rx(900)),random.randint(ry(100),ry(600))] )
    nbf=0
    encour_d=True
    while encour_d and nbf<nbfr:
        nbf+=1
        fenetre.fill((100,100,100))
        pbg=False
        if time.time()-dbg>=tbg:
            dbg=time.time()
            pbg=True
        pchg=False
        if time.time()-dchg >= tchg:
            dchg=time.time()
            pchg=True
        for d in des:
            if pbg:
                d[1]+=random.randint(-td,td)
                d[2]+=random.randint(-td,td)
                if d[1]<0: d[1]=0
                if d[1]>tex-td: d[1]=tex-td
                if d[2]<0: d[2]=0
                if d[2]>tey-td: d[2]=tey-td
            if pchg:
                d[0]=random.randint(mind,maxd)
            pygame.draw.rect(fenetre,(255,255,255),(d[1],d[2],td,td),0)
            pygame.draw.rect(fenetre,(0,0,0),(d[1],d[2],td,td),2)
            fenetre.blit( font.render(str(d[0]),True,(0,0,0)), [d[1]+rx(5),d[2]+ry(5)])
        time.sleep(0.05)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour_d=False
                    for d in des: d[0]=random.randint(mind,maxd)
    vls=[]
    for d in des: vls.append(d[0])
    fenetre.blit( font.render("Appuyez sur espace pour continuer",True,(255,255,255)) , [rx(300),ry(300)])
    pygame.display.update() 
    encour_d=True
    while encour_d:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE: encour_d=False
    return vls

def alert(txt):
    pygame.draw.rect(fenetre,(100,100,100),(rx(200),ry(300),rx(500),ry(300)),0)
    xx,yy=rx(300),ry(350)
    for t in txt.split("|"):
        fenetre.blit( font.render( t , True ,(255,255,255)) , [xx,yy] )
        yy+=ry(30)
    button=pygame.draw.rect(fenetre,(200,200,0),(rx(450),ry(500),rx(75),ry(50)),0)
    pygame.draw.rect(fenetre,(0,0,0),(rx(450),ry(500),rx(75),ry(50)),rx(2))
    fenetre.blit( font.render("ok",True,(0,0,0)) , [rx(450),ry(510)])
    pygame.display.update()
    encour_a=True
    while encour_a:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour_a=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    encour_a=False

def aff_j(joueurs,tourjoueur):
    bts=[]
    for x in range(20): bts.append(None)
    crs=[]
    cpos=[]
    fenetre.fill((0,0,0))
    e=0
    xx,yy=tex-rx(300),tey-ry(150)
    px,py=-1,0
    for c in cases:
        clf=(255,255,255)
        if type(c[3])==int:
            clf=couleurs[c[3]]
            crs.append( pygame.draw.rect(fenetre,clf,(xx,yy,tcx,tcy),0) )
        elif c[3]==None:
            crs.append( pygame.draw.rect(fenetre,clf,(xx,yy,tcx,tcy),0) )
        else:
            crs.append( fenetre.blit( c[3] , [xx,yy] ) )
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
                    if cs[1]<=4:
                        xxx,yyy=xx+rx(5),yy+ry(1)
                        ctxx,ctyy=rx(5),ry(5)
                        for x in range(cs[1]):
                            pygame.draw.rect(fenetre,j.cl,(xxx,yyy,ctxx,ctyy),0)
                            pygame.draw.rect(fenetre,(0,0,0),(xxx,yyy,ctxx,ctyy),rx(1))
                            xxx+=ctxx+rx(5)
                    else:
                        pygame.draw.rect(fenetre,j.cl,(xx+rx(5),yy+ry(1),tcx-rx(10),ry(5)),0)
                        pygame.draw.rect(fenetre,(0,0,0),(xx+rx(5),yy+ry(1),tcx-rx(10),ry(5)),rx(1))
        if c[1]==1: fenetre.blit( font.render(str(c[2])+" M $",True,(0,0,0)) , [xx+rx(5),yy+ry(50)])
        cpos.append([xx,yy])
        xx+=px*tcx
        yy+=py*tcy
        if e==0 and xx<=rx(100): e,px,py=1,0,-1
        elif e==1 and yy<=rx(100): e,px,py=2,1,0
        elif e==2 and xx>=tex-rx(300): e,px,py=3,0,1
    xx,yy=rx(300),ry(300)
    tjx,tjy=rx(200),ry(175)
    tail=int(ry(40)/len(joueurs))
    for j in joueurs:
        if not j.perdu:
            k=joueurs.index(j)
            #pion
            tt=tail
            if joueurs.index(j)==tourjoueur: tt=tail+ry(10)
            pygame.draw.circle(fenetre,j.cl,(cpos[j.caseactu][0]+(k+1)*(tail*2+rx(5)),cpos[j.caseactu][1]+ry(50)),tt,0)
            pygame.draw.circle(fenetre,(0,0,0),(cpos[j.caseactu][0]+(k+1)*(tail*2+rx(5)),cpos[j.caseactu][1]+ry(50)),tt,rx(2))
            #case
            clf=(255,255,255)
            if joueurs.index(j)==tourjoueur: clf=j.cl
            pygame.draw.rect(fenetre,clf,(xx,yy,tjx,tjy),0)
            pygame.draw.rect(fenetre,(0,0,0),(xx,yy,tjx,tjy),rx(1))
            fenetre.blit( font.render(j.pseudo,True,(0,0,0)) , [xx+rx(5),yy+ry(5)] )
            fenetre.blit( font2.render("argent : "+str(j.argent)+" M $",True,(0,0,0)) , [xx+rx(2),yy+ry(30)] )
            fenetre.blit( font2.render("propriétés : "+str(len(j.cases_possedees))+"/"+str(nbprop),True,(0,0,0)) , [xx+rx(5),yy+ry(55)] )
            pygame.draw.rect( fenetre, j.cl , (xx+rx(5),yy+ry(80),rx(60),ry(60)) ,0)
            if j.emprisone: fenetre.blit( font.render("emprisoné",True,(255,0,0)) , [xx+rx(5),yy+ry(100)] )
            xx+=tjx
            if xx>=rx(750):
                xx=rx(300)
                yy+=tjy
    tbx,tby=rx(200),ry(50)
    fenetre.blit( font3.render("Tour de "+joueurs[tourjoueur].pseudo,True,joueurs[tourjoueur].cl) , [rx(350),ry(200)])
    #
    bts[0]=pygame.draw.rect(fenetre,(200,200,200),(tbx*0,0,tbx,tby),0)
    pygame.draw.rect(fenetre,(0,0,0),(tbx*0,0,tbx,tby),rx(2))
    fenetre.blit( font.render("lancer les dés",True,(0,0,0)) , [tbx*0+rx(25),ry(15)] )
    #
    bts[1]=pygame.draw.rect(fenetre,(200,200,200),(tbx*1,0,tbx,tby),0)
    pygame.draw.rect(fenetre,(0,0,0),(tbx*1,0,tbx,tby),rx(2))
    fenetre.blit( font.render("vendre propriété",True,(0,0,0)) , [tbx*1+rx(25),ry(15)] )
    #
    bts[2]=pygame.draw.rect(fenetre,(200,200,200),(tbx*2,0,tbx,tby),0)
    pygame.draw.rect(fenetre,(0,0,0),(tbx*2,0,tbx,tby),rx(2))
    fenetre.blit( font.render("proposer une vente",True,(0,0,0)) , [tbx*2+rx(25),ry(15)] )
    #
    bts[3]=pygame.draw.rect(fenetre,(200,200,200),(tbx*3,0,tbx,tby),0)
    pygame.draw.rect(fenetre,(0,0,0),(tbx*3,0,tbx,tby),rx(2))
    fenetre.blit( font.render("contstruire",True,(0,0,0)) , [tbx*3+rx(25),ry(15)] )
    #
    pygame.display.update()
    return crs,bts

def tirercartechance(j,joueurs,tourjoueur):
    ec=False
    carte=random.choice( cartes_chances )
    if carte[1]==1: j.argent+=carte[2]
    elif carte[1]==2: j.argent-=carte[2]
    elif carte[1]==3:
        j.caseactu+=carte[2]
        if j.caseactu >= len(cases):
            j.caseactu=joueurs[tourjoueur].caseactu-len(cases)
            j.argent+=5000
            alert("Vous êtes passé par la case départ|vous avez recu 5000 M $")
        ec=True
    elif carte[1]==4:
        j.caseactu-=carte[2]
        if j.caseactu <0:
            j.caseactu=len(cases)+j.caseactu
        ec=True
    elif carte[1]==5:
        j.caseactu=carte[2]
        ec=True
    elif carte[1]==6:
        j.caseactu=6
        j.emprisonne=True
    rcarte=pygame.draw.rect( fenetre, (255,255,255) , (rx(400),ry(300),rx(200),ry(400)) , 0)
    pygame.draw.rect( fenetre, (0,0,0) , (rx(400),ry(300),rx(200),ry(400)) , rx(2))
    fenetre.blit( font.render("Carte chance",True,(0,0,0)) , [rx(430),ry(320)])
    xx,yy=rx(420),ry(350)
    for t in carte[0].split("|"):
        fenetre.blit( font2.render(t,True,(0,0,0)), [xx,yy])
        yy+=ry(20)
    pygame.display.update()
    encour_carte=True
    while encour_carte:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN and event.key==K_ESCAPE: encour_carte=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if rcarte.collidepoint( pos ): encour_carte=False
    aff_j(joueurs,tourjoueur)
    if ec: ecran_choix(joueurs,tourjoueur)
        
    

def ecran_choix(joueurs,tourjoueur):
    j=joueurs[tourjoueur]
    ca=cases[j.caseactu]
    bts=[]
    for x in range(10): bts.append( None )
    pygame.draw.rect(fenetre,(150,135,20),(rx(300),ry(250),rx(600),ry(500)),0)
    fenetre.blit( font.render(j.pseudo+", vous êtes tombé sur la case : "+ca[0].replace("|"," "),True,(50,50,50)),[rx(305),ry(300)])
    if ca[1]==1:
        fenetre.blit( font.render("C'est une propriété",True,(50,50,50)),[rx(400),ry(350)])
        pos=[False,None,0]
        for jj in joueurs:
            for p in jj.cases_possedees:
                if p[0]==cases.index( ca ):
                    pos=[True,jj,ca[4+p[1]]]
                    break
        if not pos[0]:
            fenetre.blit( font.render("Elle n'est pas possédée",True,(50,50,50)),[rx(400),ry(400)])
            fenetre.blit( font.render("Voulez vous l'acheter ? ( "+str(ca[2])+" M $ )",True,(50,50,50)),[rx(400),ry(450)])
            bts[0]=pygame.draw.rect( fenetre, (255,255,255) , (rx(500),ry(600),rx(75),ry(50)) , 0)
            fenetre.blit( font.render("oui",True,(0,0,0)) , [rx(515),ry(610)])
            bts[1]=pygame.draw.rect( fenetre, (255,255,255) , (rx(700),ry(600),rx(75),ry(50)) , 0)
            fenetre.blit( font.render("non",True,(0,0,0)) , [rx(715),ry(610)])
        elif pos[1]==j:
            fenetre.blit( font.render("Vous la possedez",True,(50,50,50)),[rx(400),ry(400)])
            bts[2]=pygame.draw.rect( fenetre,(255,255,255), (rx(650),ry(550),rx(75),ry(50)) , 0)
            fenetre.blit( font.render("ok",True,(0,0,0)) , [rx(660),ry(570)])
        else:   
            fenetre.blit( font.render("Elle est possédée par "+pos[1].pseudo,True,(50,50,50)),[rx(400),ry(400)])
            print(pos[2])
            fenetre.blit( font.render("Le loyer sera de "+str(pos[2])+" M $",True,(50,50,50)),[rx(400),ry(450)])
            j.argent-=pos[2]
            pos[1].argent+=pos[2]
            bts[2]=pygame.draw.rect( fenetre,(255,255,255), (rx(650),ry(550),rx(75),ry(50)) , 0)
            fenetre.blit( font.render("ok",True,(0,0,0)) , [rx(660),ry(570)])
    elif ca[1]==3:
        fenetre.blit( font.render("C'est une case chance",True,(50,50,50)),[rx(400),ry(350)])
        fenetre.blit( font.render("Vous devez tirer une carte chance",True,(50,50,50)),[rx(400),ry(400)])
        bts[3]=pygame.draw.rect( fenetre,(255,255,255), (rx(400),ry(550),rx(250),ry(50)) , 0)
        fenetre.blit( font.render("tirer un carte chance",True,(0,0,0)) , [rx(420),ry(570)])
    else:
        bts[2]=pygame.draw.rect( fenetre,(255,255,255), (rx(650),ry(550),rx(75),ry(50)) , 0)
        fenetre.blit( font.render("ok",True,(0,0,0)) , [rx(660),ry(570)])
    pygame.display.update()
    encour_c=True
    while encour_c:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: exit()
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for b in bts:
                    if b!=None and b.collidepoint(pos):
                        encour_c=False  
                        i=bts.index(b)
                        if i==0:
                            if j.argent >= ca[2]:
                                j.argent-=ca[2]
                                j.cases_possedees.append( [cases.index(ca),0,0] )
                            else:
                                alert("Vous n'avez pas assez d'argent")
                        elif i==1:
                            pass
                        elif i==2: encour_c=False
                        elif i==3: tirercartechance(j,joueurs,tourjoueur)

def vendre_prop(j,joueurs,tourjoueur):
    rcts=[]
    pygame.draw.rect(fenetre,(100,100,100),(rx(250),ry(300),rx(700),ry(500)),0)
    b1=pygame.draw.rect(fenetre,(255,0,0),(rx(750),ry(300),rx(50),ry(50)),0)
    fenetre.blit( font4.render("X",True,(0,0,0)) , [rx(750),ry(300)])
    fenetre.blit( font.render("Séléctionnez la propriété que vous voulez vendre à la banque",True,(255,255,255)) , [rx(350),ry(350)])
    xx,yy,ctx,cty=rx(400),ry(400),rx(150),ry(150)
    for p in j.cases_possedees:
        rcts.append( pygame.draw.rect(fenetre,(255,255,255),(xx,yy,ctx,cty),0) )
        fenetre.blit( font.render( cases[p[0]][0] , True , (0,0,0)) , [xx+rx(5),yy+ry(5)])
        fenetre.blit( font.render( str(cases[p[0]][2]/2)+" M $" , True , (0,0,0)) , [xx+rx(5),yy+ry(25)])
        xx+=tcx+rx(10)
        if xx>=rx(750): xx,yy=rx(400),yy+tcy+ry(10)
    pygame.display.update()
    encour_vp=True
    while encour_vp:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if b1.collidepoint(pos): encour_vp=False
                for r in rcts:
                    if r.collidepoint(pos):
                        ii=j.cases_possedees[rcts.index(r)][0]
                        encour_vp=False
                        aff_j(joueurs,tourjoueur)
                        j.argent+=cases[ii][2]/2
                        try: del(j.cases_possedees[rcts.index(r)])
                        except: pass
                        alert("Vous avez vendu à la banque "+cases[ii][0]+"| Cela vous a rapporté "+str(cases[ii][2]/2)+" M $")

def construire(j,joueurs,tourjoueur):
    pygame.draw.rect(fenetre,(100,100,100),(rx(300),ry(200),rx(700),ry(600)),0)
    fenetre.blit( font.render("Séléctionnez la propriété sur laquelle vous voulez construire une maison :",True,(255,255,255)) , [rx(350),ry(350)])
    cr=[]
    xx,yy,ctx,cty=rx(350),ry(450),rx(200),ry(200)
    for p in j.cases_possedees:
        cr.append( pygame.draw.rect(fenetre,(255,255,255),(xx,yy,ctx,cty),0) )
        pygame.draw.rect(fenetre,(0,0,0),(xx,yy,ctx,cty),rx(2))
        fenetre.blit( font.render(cases[p[0]][0],True,(0,0,0)) , [xx+rx(5),yy+ry(5)])
        if p[1]<4: fenetre.blit( font.render(str(cases[p[0]][10])+" M $",True,(0,0,0)) , [xx+rx(5),yy+ry(30)])
        elif p[1]<5: fenetre.blit( font.render(str(cases[p[0]][11])+" M $",True,(0,0,0)) , [xx+rx(5),yy+ry(30)])
        else: fenetre.blit( font.render("complet",True,(0,0,0)) , [xx+rx(5),yy+ry(30)])
        xx+=ctx+rx(10)
        if xx>=rx(900): xx,yy=rx(350),yy+cty+ry(10)
    pygame.display.update()
    encour_co=True
    while encour_co:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for c in cr:
                    if c.collidepoint(pos):
                        encour_co=False
                        p=j.cases_possedees[cr.index(c)]
                        nbclct=0
                        nbclcj=0
                        clc=cases[p[0]][3]
                        for cc in cases:
                            if cc[3]==clc: nbclct+=1
                        for pp in j.cases_possedees:
                            if cases[pp[0]][3]==clc: nbclcj+=1
                        aff_j(joueurs,tourjoueur)
                        if nbclct==nbclcj:
                            if p[1]<5:
                                if p[1]<4:
                                    prix=cases[p[0]][10]
                                else: prix=cases[p[0]][11]
                                if j.argent >= prix:
                                    p[1]+=1
                                    j.argent-=prix
                                    t="e maison"
                                    if p[1]==5: t=" hotel"
                                    alert("Vous venez de construire un"+t+"|Sur votre propriété "+cases[p[0]][0]+"|Cela vous a couté "+str(prix)+" M $")
                                else: alert("Vous n'avez pas assez d'argent")
                            else: alert("Vous avez déjà un hotel dessus")
                        else: alert("Vous ne possédez pas toutes les propriétés|de cette couleur pour construire dessus")

def main_j(joueurs):
    tour=1
    encour=True
    r_plateau=pygame.Rect(rx(100),ry(100),rx(800),ry(550))
    tourjoueur=0
    while encour:
        for j in joueurs:
            if len(str(j.argent)) > 9: j.argent=float(str(j.argent)[:9])
        crs,bts=aff_j(joueurs,tourjoueur)
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    encour=False
            elif event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if True or r_plateau.collidepoint(pos):
                    for c in crs:
                        if c.collidepoint(pos):
                            dc=crs.index(c)
                    for b in bts:
                        if b!=None and b.collidepoint(pos):
                            di=bts.index(b)
                            if di==0:
                                crs,bts=aff_j(joueurs,tourjoueur)
                                des=lancerdes()
                                vl=0
                                for d in des: vl+=d
                                joueurs[tourjoueur].caseactu+=vl
                                if joueurs[tourjoueur].caseactu >= len(cases):
                                    joueurs[tourjoueur].caseactu=joueurs[tourjoueur].caseactu-len(cases)
                                    joueurs[tourjoueur].argent+=5000
                                    alert("Vous êtes passé par la case départ|vous avez recu 5000 M $")
                                crs,bts=aff_j(joueurs,tourjoueur)
                                ecran_choix(joueurs,tourjoueur)
                                if len(des)==2 and des[0]==des[1]:
                                    alert("Vous avez fait un double|vous rejouez")
                                else:
                                    tourjoueur+=1
                                    if tourjoueur>=len(joueurs): tourjoueur,tour=0,tour+1
                            elif di==1 and len(joueurs[tourjoueur].cases_possedees) >= 1: vendre_prop(joueurs[tourjoueur],joueurs,tourjoueur)
                            elif di==3 and len(joueurs[tourjoueur].cases_possedees) >= 1: construire(joueurs[tourjoueur],joueurs,tourjoueur)
                            

def aff_menu(joueurs):
    bts=[]
    for x in range(10): bts.append(None)
    jr=[]
    cr=[]
    fenetre.fill((0,0,0))
    fenetre.blit( font4.render("ONYPOMOL",True,(200,200,20)), [rx(350),ry(100)])
    bts[0]=pygame.draw.rect(fenetre,(200,255,50),(rx(400),ry(700),rx(100),ry(50)),0)
    fenetre.blit( font.render("jouer",True,(0,0,0)) , [rx(420),ry(710)])
    bts[1]=pygame.draw.rect(fenetre,(100,100,20),(rx(50),ry(350),rx(40),ry(40)),0)
    fenetre.blit( font4.render("+",True,(0,0,0)) , [rx(50),ry(340)])
    xx,yy,tjx,tjy=rx(200),ry(200),rx(200),ry(300)
    for j in joueurs:
        jr.append( pygame.draw.rect(fenetre,(255,255,255),(xx,yy,tjx,tjy),0) )
        pygame.draw.rect(fenetre,(30,30,30),(xx,yy,tjx,tjy),rx(2))
        fenetre.blit( font.render(j.pseudo,True,(0,0,0)) , [xx+rx(10),yy+ry(5)] )
        cr.append( pygame.draw.rect( fenetre , j.cl , (xx+rx(50),yy+ry(100),rx(50),ry(50)) , 0) )
        xx+=tjx+rx(15)
    pygame.display.update()
    return bts,jr,cr

def menu():
    joueurs=[]
    encour_m=True
    while encour_m:
        bts,jr,cr=aff_menu(joueurs)
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
                            main_j(joueurs)
                        elif di==1:
                            pseudo=pynput("pseudo :")
                            cl=rcl()
                            joueurs.append( Joueur(pseudo,cl) )
                ccr=False
                for c in cr:
                    if c.collidepoint(pos): ccr,joueurs[cr.index(c)].cl=True,rcl()
                if not ccr:
                    for j in jr:
                        if j.collidepoint(pos): joueurs[jr.index(j)].pseudo=pynput("pseudo :")
                        
            



menu()












    
    
