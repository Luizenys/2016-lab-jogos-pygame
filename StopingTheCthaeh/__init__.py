from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from PPlay.collision import *
from PPlay.mouse import *
import time
import random
from random import randint
random.seed()

ctr = 0
dano = 0
flechas = 60
flechas1 = 50
flechas2 = 200
GAME_STATE = 0
DIFICUL = 4
LARGURA_JANELA = 1230
ALTURA_JANELA = 553
INTERVALO_JANELA = 3000
VEL = 400
VEL_TIRO = 1150
VEL_MT = 200
VEL_SETA = 800
INTERVALO_TIRO = 300
INTERVALO_MT = 2000
INTERVALO_SETA_CIMA = 300
INTERVALO_SETA_BAIXO = 300
dir = -1


teclado = Keyboard()
mouse = Mouse()
janela  = Window(LARGURA_JANELA,ALTURA_JANELA)
janela.set_background_color((0,0,0))
janela.set_title("The Fae")
background_01 = GameImage("bg.jpg")
background_02 = GameImage("bg.png")
janela.update()

spriteSitheInicio = Sprite("nsl3.png")
spriteSithe = Sprite("nsl2.png")
sitheShooting = Sprite("nshooting2.png")
cthaeh = GameImage("cthaeh.png")
wall = GameImage("wall.jpg")
life = GameImage("heart.png")
boss = Sprite("er.png",1)
arrow = GameImage("flecha.png")
muayThai = Sprite("mt.png")
tempocarrega = janela.last_time
tempoUltimoTiro = janela.last_time
tempoUltimoInimigo = janela.last_time
tempoUltimoInimigo1 = janela.last_time
tempoUltimoAliado = janela.last_time
tempoUltimoAliado1 = janela.last_time
tempoUltimoMt = janela.last_time
tempoUltimoBuraco = janela.last_time
tempoUltimaSetaCima = janela.last_time
tempoUltimaSetaBaixo = janela.last_time
tempoUltimoPortal = janela.last_time
tempoUltimoDourado = janela.last_time
muayThai.set_position(1030,550)

dparado = []
mt = []
tiros = []
setasCima = []
setasBaixo = []
aliados = []
inimigos = []
aliados1 = []
inimigos1 = []
buracos = []
portais = []
dourados = []
aliadoT = Sprite("running.png", 4)
aliadoT.set_position(90,445)
inimigoT1 = Sprite("kvotheDireitaAnda.png",4)
inimigoT1.set_position(320,445)
inimigoT2 = Sprite("gris.png", 4)
inimigoT2.set_position(550,445)
inimigoT3 = Sprite("haliax.png", 4)
inimigoT3.set_position(780,445)
aliado = Sprite("running.png", 4)
aliado.set_total_duration(1000)
aliado.score = 0
inimigo = Sprite("kvotheDireitaAnda.png", 4)
inimigo.set_total_duration(1000)
inimigo.score = 0
tema = Sound("theme1.wav")
tema.play()
spr1 = Sprite("running.png",4)
kills = 0
escolhedif = 0


def desenharInimigos(inimigos):
    for i in inimigos:
        i.draw()
        i.update()


def desenharAliados(aliados):
    for i in aliados:
        i.draw()
        i.update()

def desenharSetas(setas):
    for i in setas:
        i.draw()

def movimentarInimigo(inimigos,GAME_STATE,vidas,sacri):
    deltaT = janela.delta_time()
    deltaS = VEL_INI * deltaT
    for i in inimigos:
        posx = i.x + deltaS
        posy = i.y
        i.set_position(posx,posy)
        if posx > 1200 and sacri == 0:
            GAME_STATE = 3
        elif posx > 1200:
            inimigos.remove(i)
            sacri -= 1
        else:
            pass
    if vidas == 0:
        GAME_STATE = 2
    return GAME_STATE,sacri

def movimentarInimigo1(inimigos,GAME_STATE,vidas,sacri):
    deltaT = janela.delta_time()
    deltaS = VEL_INI1 * deltaT
    for i in inimigos:
        posx = i.x + deltaS
        posy = i.y
        i.set_position(posx,posy)
        if posx > 1200 and sacri == 0:
            if GAME_STATE == 5:
                GAME_STATE = 10
            elif GAME_STATE == 7:
                GAME_STATE = 6
        elif posx > 1200:
            inimigos.remove(i)
            sacri -= 1
        else:
            pass
    if vidas == 0:
        GAME_STATE = 2
    return GAME_STATE,sacri

def movimentarAliado(aliados):
    deltaT = janela.delta_time()
    deltaS = VEL_ALI * deltaT
    for i in aliados:
        posx = i.x + deltaS
        posy = i.y
        i.set_position(posx,posy)

def movimentarAliado1(aliados,setasC,setasB):
    deltaT = janela.delta_time()
    deltaS = VEL_ALI1 * deltaT
    for i in aliados:
        posx = i.x + deltaS
        posy = i.y
        for j in setasC:
            if j.collided_perfect(i):
                setasC.remove(j)
                if posy > 30:
                    posy -= 140
                else:
                    pass
            else:
                pass
        for k in setasB:
            if k.collided_perfect(i):
                setasB.remove(k)
                if posy < 400:
                    posy += 140
                else:
                    pass
            else:
                pass
        i.set_position(posx, posy)


posB0 = False
posB1 = False
posB2 = False
posB3 = False

def criarBuracos(buracos,tempoUltimoBuraco,posB0,posB1,posB2,posB3):
    buraco = Sprite("Portal.png")
    if (janela.last_time - tempoUltimoBuraco > INTERVALO_BUR):
        i = random.randint(0, 4)
        if i==0:
            if posB0 == False:
               buraco.set_position(735,20)
               buracos.append(buraco)
               tempoUltimoBuraco = janela.last_time
               posB0 = True
        if i==1:
            if posB1 == False:
                buraco.set_position(735, 160)
                buracos.append(buraco)
                tempoUltimoBuraco = janela.last_time
                posB1 = True
        if i == 2:
            if posB2 == False:
                buraco.set_position(735, 290)
                buracos.append(buraco)
                tempoUltimoBuraco = janela.last_time
                posB2 = True
        if i == 3:
            if posB3 == False:
                buraco.set_position(735, 440)
                buracos.append(buraco)
                tempoUltimoBuraco = janela.last_time
                posB3 = True
        else:
            pass
    else:
        pass
    return tempoUltimoBuraco,posB0,posB1,posB2,posB3

posP0 = False
posP1 = False
posP2 = False
posP3 = False

def criarPortais(portais,tempoUltimoPortal,posP0,posP1,posP2,posP3):
    portal = Sprite("hole1.png")
    if (janela.last_time - tempoUltimoPortal > INTERVALO_POR):
        i = random.randint(0, 4)
        if i==0:
            if posP0 == False:
                portal.set_position(620,20)
                portais.append(portal)
                tempoUltimoPortal = janela.last_time
                posP0 = True
        if i==1:
            if posP1 == False:
                portal.set_position(620, 160)
                portais.append(portal)
                tempoUltimoPortal = janela.last_time
                posP1 = True
        if i == 2:
            if posP2 == False:
                portal.set_position(620, 290)
                portais.append(portal)
                tempoUltimoPortal = janela.last_time
                posP2 = True
        if i == 3:
            if posP3 == False:
                portal.set_position(620, 440)
                portais.append(portal)
                tempoUltimoPortal = janela.last_time
                posP3 = True
        else:
            pass
    else:
        pass
    return tempoUltimoPortal,posP0,posP1,posP2,posP3

def desenharBuracos(buracos):
    for buraco in buracos:
        buraco.draw()


def criarInimigos(inimigos,tempoUltimoInimigo):
    inimigo = Sprite("kvotheanda.png", 4)
    inimigo.set_total_duration(1000)
    if (janela.last_time - tempoUltimoInimigo > INTERVALO_INI):
        i = random.randint(0, 4)
        if i==0:
            inimigo.set_position(0,40)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i==1:
            inimigo.set_position(0, 180)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i == 2:
            inimigo.set_position(0, 320)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i == 3:
            inimigo.set_position(0, 460)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        else:
            pass
    else:
        pass
    return tempoUltimoInimigo

def criarInimigos1(inimigos,tempoUltimoInimigo,GAME_STATE):
    if GAME_STATE == 1:
        inimigo = Sprite("kvotheDireitaAnda.png", 4)
        inimigo.set_total_duration(1000)
    elif GAME_STATE == 5:
        inimigo = Sprite("gris.png", 4)
        inimigo.set_total_duration(1000)
    elif GAME_STATE == 7:
        inimigo = Sprite("haliax.png", 4)
        inimigo.set_total_duration(1000)

    if (janela.last_time - tempoUltimoInimigo > INTERVALO_INI1):
        i = random.randint(0, 4)
        if i==0:
            inimigo.set_position(0,20)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i==1:
            inimigo.set_position(0, 160)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i == 2:
            inimigo.set_position(0, 300)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        if i == 3:
            inimigo.set_position(0, 440)
            inimigo.set_total_duration(1000)
            inimigos.append(inimigo)
            tempoUltimoInimigo = janela.last_time
        else:
            pass
    else:
        pass
    return tempoUltimoInimigo


def criarAliados(aliados,tempoUltimoAliado):
    aliado = Sprite("running.png", 4)
    aliado.set_total_duration(1000)
    if (janela.last_time - tempoUltimoAliado > INTERVALO_ALI):
        i = random.randint(0, 4)
        if i==0:
            aliado.set_position(0, 20)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i==1:
            aliado.set_position(0, 160)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i == 2:
            aliado.set_position(0, 300)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i == 3:
            aliado.set_position(0, 440)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        else:
            pass
    else:
        pass
    return tempoUltimoAliado

def criarDour(aliados,tempoUltimoAliado):
    aliado = Sprite("dour.png", 4)
    aliado.set_total_duration(1000)
    if (janela.last_time - tempoUltimoAliado > INTERVALO_DOUR):
        i = random.randint(0, 4)
        if i==0:
            aliado.set_position(0, 20)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i==1:
            aliado.set_position(0, 160)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i == 2:
            aliado.set_position(0, 300)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        if i == 3:
            aliado.set_position(0, 440)
            aliado.set_total_duration(1000)
            aliados.append(aliado)
            tempoUltimoAliado = janela.last_time
        else:
            pass
    else:
        pass
    return tempoUltimoAliado

def colisaoFlechaInimigo(inimigos,tiros,INTERVALO_INI,INTERVALO_ALI,VEL_INI,VEL_ALI,kills):
    for i in inimigos:
        for tiro in tiros:
            if tiro.collided_perfect(i):
                kills = kills + 1
                tiros.remove(tiro)
                inimigos.remove(i)
                inimigo.score += 50
                if VEL_INI <210:
                   INTERVALO_INI -= 15
                   INTERVALO_ALI -=15
                   VEL_INI += 6
                   VEL_ALI += 12
                elif VEL_INI >= 210:
                    pass
    return INTERVALO_INI,INTERVALO_ALI,VEL_INI,VEL_ALI,kills

def colisaoBuracoInimigo(inimigos,buracos,inimigo,posB0,posB1,posB2,posB3):
    for i in inimigos:
        for buraco in buracos:
            if buraco.collided_perfect(i):
                posy = buraco.y
                buracos.remove(buraco)
                if posy == 20:
                    posB0 = False
                elif posy == 160:
                    posB1 = False
                elif posy == 290:
                    posB2 = False
                elif posy == 440:
                    posB3 = False
                inimigos.remove(i)
                inimigo.set_total_duration(1000)
                inimigo.set_position(990,posy)
                inimigos.append(inimigo)
    return posB0,posB1,posB2,posB3

def colisaoInimigoDourado(dour,inimigos,posD0,posD1,posD2,posD3):
    for i in inimigos:
        for j in dour:
            if j.collided_perfect(i):
                posy = i.y
                if posy == 20:
                    posD0 = False
                elif posy == 160:
                    posD1 = False
                elif posy == 300:
                    posD2 = False
                elif posy == 440:
                    posD3 = False
                inimigos.remove(i)
                dour.remove(j)
    return posD0,posD1,posD2,posD3


posD0 = False
posD1 = False
posD2 = False
posD3 = False

def colisaoBuracoDourado(dour,buracos,dparado,posB0,posB1,posB2,posB3,posD0,posD1,posD2,posD3):
    inimigo = Sprite("escdour.png")
    for i in dour:
        for buraco in buracos:
            if buraco.collided_perfect(i):
                posy = buraco.y
                buracos.remove(buraco)
                if posy == 20:
                    posB0 = False
                elif posy == 160:
                    posB1 = False
                elif posy == 290:
                    posB2 = False
                elif posy == 440:
                    posB3 = False
                if len(dparado)<4:
                  if posy == 20:
                      if posD0 == True:
                          i.set_position(1000, posy)
                      elif posD0 == False:
                          inimigo.set_position(1000, posy)
                          dparado.append(inimigo)
                          dour.remove(i)
                          posD0 = True
                  elif posy == 160 and posD1 == False:
                      if posD1 == True:
                          i.set_position(1000, posy)
                      elif posD1 == False:
                          inimigo.set_position(1000, posy)
                          dparado.append(inimigo)
                          dour.remove(i)
                          posD1 = True
                  elif posy == 290 and posD2 == False:
                      if posD2 == True:
                          i.set_position(1000, posy)
                      elif posD2 == False:
                          inimigo.set_position(1000, posy)
                          dparado.append(inimigo)
                          dour.remove(i)
                          posD2 = True
                  elif posy == 440 and posD3 == False:
                      if posD3 == True:
                          i.set_position(1000, posy)
                      elif posD3 == False:
                          inimigo.set_position(1000, posy)
                          dparado.append(inimigo)
                          dour.remove(i)
                          posD3 = True
                else:
                    i.set_position(1000, posy)

    return posB0,posB1,posB2,posB3,posD0,posD1,posD2,posD3

def desenharDparados(dparado):
    for i in dparado:
        i.draw()

def colisaoSetaInimigo(inimigos,setasC,setasB):
    for i in inimigos:
        for j in setasC:
            if j.collided_perfect(i):
                setasC.remove(j)
        for k in setasB:
            if k.collided_perfect(i):
                setasB.remove(k)


def colisaoInimigoSithe(inimigos,aliados,sithe,vidas,dano,escudo,spriteDef,tiros,portais,posP0,posP1,posP2,posP3):
    for i in inimigos:
        if escudo == True:
            if i.collided_perfect(spriteDef):
                inimigos.remove(i)
                inimigo.score+=30
                dano = dano + 1
        elif escudo == False and arco == True:
            if i.collided_perfect(sithe["spriteAtira"]):
                inimigos.remove(i)
                inimigo.score -= 20
                vidas = vidas - 1
        elif escudo == False and arco == False:
            if i.collided_perfect(sithe["spriteParado"]):
                inimigos.remove(i)
                inimigo.score -= 20
                vidas = vidas - 1
    for j in aliados:
        if escudo == True:
            if j.collided_perfect(spriteDef):
                aliados.remove(j)
                dano = dano + 1
        elif escudo == False and arco == True:
            if j.collided_perfect(sithe["spriteAtira"]):
                aliados.remove(j)
                vidas = vidas - 1
        elif escudo == False and arco == False:
            if j.collided_perfect( sithe["spriteParado"]):
                aliados.remove(j)
                vidas = vidas - 1


    for k in aliados:
        for tiro in tiros:
            if k.collided_perfect(tiro):
                aliados.remove(k)
                tiros.remove(tiro)
                vidas = vidas - 1

        for por in portais:
            if por.collided_perfect(k):
                posy = por.y
                portais.remove(por)
                aliados.remove(k)
                if posy == 20:
                    posP0 = False
                elif posy == 160:
                    posP1 = False
                elif posy == 290:
                    posP2 = False
                elif posy == 440:
                    posP3 = False
                vidas = vidas - 1


    if dano >= 4:
        vidas = vidas - 1
        dano = 0

    for m in inimigos:
        for portal in portais:
            if portal.collided_perfect(m):
                posy = portal.y
                portais.remove(portal)
                inimigos.remove(m)
                if posy == 20:
                    posP0 = False
                elif posy == 160:
                    posP1 = False
                elif posy == 290:
                    posP2 = False
                elif posy == 440:
                    posP3 = False

    return vidas,dano,posP0,posP1,posP2,posP3


def desenharBarra(dano):
    if dano == 0:
        damage = GameImage("dano.png")
        damage.set_position(0, 500)
        damage.draw()
    elif dano == 1:
        damage = GameImage("dano1.png")
        damage.set_position(0, 500)
        damage.draw()
    elif dano == 2:
        damage = GameImage("dano2.png")
        damage.set_position(0, 500)
        damage.draw()
    elif dano == 3:
        damage = GameImage("dano3.png")
        damage.set_position(0, 500)
        damage.draw()


def capturarEntrada(sithe,tiros,tempoUltimoTiro,flechas):
    x = sithe["posX"]
    y = sithe["posY"]
    deltaT = janela.delta_time()
    deltaS = VEL*deltaT
    if teclado.key_pressed("ESC"):
        janela.close()
    if teclado.key_pressed("UP"):
        y = y - deltaS
    elif teclado.key_pressed("DOWN"):
        y = y + deltaS
    if (teclado.key_pressed("H")):
        escudo = True
    else:
        escudo = False
    if (teclado.key_pressed("SPACE")):
        if escudo == False:
            arco = True
            if (janela.last_time-tempoUltimoTiro>INTERVALO_TIRO) and flechas>0:
                flechas -= 1
                tiro = Sprite("flecha.png")
                tiro.set_position(sithe["posX"]-sithe["spriteParado"].width/2+2*(tiro.width), sithe["posY"]-8+sithe["spriteParado"].height/2)
                tiros.append(tiro)
                tempoUltimoTiro = janela.last_time
        elif escudo == True:
            arco = False
    else:
        arco = False


    sithe["posX"] = x
    sithe["posY"] = y

    return tempoUltimoTiro , arco , flechas, escudo


def capturarEntrada2(sithe,tiros,tempoUltimoTiro,flechas,setasCima,setasBaixo,tempoUltimaSetaCima,tempoUltimaSetaBaixo):
    x = sithe["posX"]
    y = sithe["posY"]
    deltaT = janela.delta_time()
    deltaS = VEL*deltaT
    if teclado.key_pressed("ESC"):
        janela.close()
    if teclado.key_pressed("UP"):
        y = y - deltaS
    elif teclado.key_pressed("DOWN"):
        y = y + deltaS
    if (teclado.key_pressed("H")):
        escudo = True
    else:
        escudo = False
    if (teclado.key_pressed("SPACE")):
        if escudo == False:
            arco = True
            if (janela.last_time-tempoUltimoTiro>INTERVALO_TIRO) and flechas>0:
                flechas -= 1
                tiro = Sprite("flecha.png")
                tiro.set_position(sithe["posX"]-sithe["spriteParado"].width/2+2*(tiro.width), sithe["posY"]-8+sithe["spriteParado"].height/2)
                tiros.append(tiro)
                tempoUltimoTiro = janela.last_time
        elif escudo == True:
            arco = False
    else:
        arco = False
    if (teclado.key_pressed("LEFT")):
        if escudo == False and arco == False:
            if (janela.last_time - tempoUltimaSetaCima > INTERVALO_SETA_CIMA):
                setaCima = Sprite("setacima.png")
                setaCima.set_position(sithe["posX"] - sithe["spriteParado"].width / 2 + 2 * (setaCima.width),
                                  sithe["posY"] - 8 + sithe["spriteParado"].height / 2)
                setasCima.append(setaCima)
                tempoUltimaSetaCima = janela.last_time

    if (teclado.key_pressed("RIGHT")):
        if escudo == False and arco == False:
            if (janela.last_time - tempoUltimaSetaBaixo > INTERVALO_SETA_BAIXO):
                setaBaixo = Sprite("setabaixo.png")
                setaBaixo.set_position(sithe["posX"] - sithe["spriteParado"].width / 2 + 2 * (setaBaixo.width),
                                  sithe["posY"] - 8 + sithe["spriteParado"].height / 2)
                setasBaixo.append(setaBaixo)
                tempoUltimaSetaBaixo = janela.last_time


    sithe["posX"] = x
    sithe["posY"] = y

    return tempoUltimoTiro , arco , flechas, escudo , tempoUltimaSetaCima, tempoUltimaSetaBaixo


def limitarMovimento(altura,sithe):

    y = sithe["posY"]

    if (y<0):
        y = 0
    elif (y>altura-sithe["spriteParado"].height):
        y = altura-sithe["spriteParado"].height

    sithe["posY"] = y

def desenharTiros(tiros,sithe):
    for tiro in tiros:
        tiro.draw()


def movimentarTiros(tiros):
    deltaS = VEL_TIRO*janela.delta_time()
    for tiro in tiros:
        posx = tiro.x-deltaS
        posy = tiro.y
        tiro.set_position(posx,posy)

def movimentarSetas(setas):
    deltaS = VEL_SETA*janela.delta_time()
    for seta in setas:
        posx = seta.x-deltaS
        posy = seta.y
        seta.set_position(posx,posy)


def removerAliadosFora(aliados):
    for j in aliados:
        if j.x>1230:
            aliados.remove(j)


def removerTirosForaDaTela(tiros):
    for tiro in tiros:
        if (tiro.x<=0):
            tiros.remove(tiro)


def removerInimigosForaDaTela(inimigos):
    for i in inimigos:
        if (i.x>1230):
            inimigos.remove(i)


def criarSithe():
    spritePara = Sprite("str.png", 1)
    spriteAti = Sprite("atira.png", 1)
    spriteDef = Sprite("escudo.png", 1)
    spriteDef.set_position(700,700)
    sithe = dict(spriteParado = spritePara, spriteAtira = spriteAti, lives=3, posX=850,
                 posY=ALTURA_JANELA - spriteSithe.height)
    return sithe,spriteDef


def desenharSithe(sithe,arco,escudo,spriteDef):
    if arco == False and escudo == False:
       sithe["spriteParado"].set_position(sithe["posX"], sithe["posY"])
       sithe["spriteParado"].draw()
    if arco == True:
       sithe["spriteAtira"].set_position(sithe["posX"]+18, sithe["posY"])
       sithe["spriteAtira"].draw()
    if escudo == True:
       spriteDef.set_position(sithe["posX"] + 23, sithe["posY"])
       spriteDef.draw()


def desenharTudo(fundo,sithe,tiros,dir):
    tema2 = Sound("toasty1.wav")
    fundo.draw()
    desenharTiros(tiros,sithe)
    wall.set_position(1000, 0)
    wall.draw()
    cthaeh.set_position(980, 10)
    cthaeh.draw()
    life.set_position(15, 0)
    life.draw()
    arrow.set_position(0,30)
    arrow.draw()
    if inimigo.score%500==0 and inimigo.score!=0:
        posy,dir = movimentarMt(dir)
        muayThai.set_position(1030, posy)
        tema2.play()
        muayThai.draw()
    else:
        muayThai.set_position(1030,550)

def movimentarMt(dir):
    deltaT = janela.delta_time()
    deltaS = VEL_MT*deltaT
    posy = muayThai.y + (deltaS*dir)
    if posy<380:
        posy = 380

    return posy,dir

def gameintro():
    janela.draw_text("Stopping the Cthaeh"
               , 200, 100, 100, (255, 255, 255), "Impact")
    janela.draw_text("Clique em uma dificuldade para jogar | ESC para sair",
                     250, 0, 35, (255, 255, 255), "Calibri")
    #janela.draw_text("VS"
                     #, 550, 350, 70, (255, 255, 255), "Impact")
    janela.update()
    background_02.draw()

def movimentarCharTela(spr):
    spr.set_total_duration(1000)
    deltaT = janela.delta_time()
    deltaS = 200 * deltaT
    posx = spr.x + deltaS
    posy = spr.y
    if posx > 1000:
        posx = 90
    spr.set_position(posx, posy)
    spr.draw()
    spr.update()

sithe,spriteDef = criarSithe()
kvothe = GameImage("kvothe111.png")

def escolherDif(escolhedif):
    if teclado.key_pressed("UP"):
        escolhedif -=1
    elif teclado.key_pressed("DOWN"):
        escolhedif += 1
    if escolhedif > 2:
        escolhedif = 0
    if escolhedif < 0:
        escolhedif = 2

    return escolhedif

def desenharCont(dif):
    barra = GameImage("difdou.png")
    if mouse.is_over_object(dif):
        posy = dif.y
        barra.set_position(530,posy)
        barra.draw()

while (True):


    if GAME_STATE == 0:
        gameintro()
        #tema.play()
        spriteSitheInicio.set_position(650,340)
        #spriteSitheInicio.draw()
        kvothe.set_position(400,330)
        #kvothe.draw()
        diffac = GameImage("facc.png")
        diffac.set_position(530,220)
        diffac.draw()
        difnor = GameImage("normm.png")
        difnor.set_position(530, 290)
        difnor.draw()
        difdif = GameImage("diff.png")
        difdif.set_position(530, 360)
        difdif.draw()
        #escolhedif = escolherDif(escolhedif)
        desenharCont(diffac)
        desenharCont(difnor)
        desenharCont(difdif)
        movimentarCharTela(aliadoT)
        movimentarCharTela(inimigoT1)
        movimentarCharTela(inimigoT2)
        movimentarCharTela(inimigoT3)
        if mouse.is_over_object(diffac) and mouse.is_button_pressed(1):
            vidas = 13
            sacrificios = 2
            VEL_INI = 80
            VEL_ALI = 160
            VEL_INI1 = 250
            VEL_ALI1 = 250
            INTERVALO_INI = 2500
            INTERVALO_INI1 = 1300
            INTERVALO_ALI = 3000
            INTERVALO_ALI1 = 2500
            INTERVALO_DOUR = 10000
            INTERVALO_BUR = 9000
            INTERVALO_POR = 8400
            GAME_STATE = 4
        if mouse.is_over_object(difnor) and mouse.is_button_pressed(1):
            vidas = 11
            sacrificios = 1
            VEL_INI = 90
            VEL_ALI = 180
            VEL_INI1 = 250
            VEL_ALI1 = 250
            INTERVALO_INI = 2000
            INTERVALO_INI1 = 1300
            INTERVALO_ALI = 2500
            INTERVALO_ALI1 = 2500
            INTERVALO_DOUR = 15000
            INTERVALO_BUR = 8200
            INTERVALO_POR = 8000
            GAME_STATE = 4
        if mouse.is_over_object(difdif) and mouse.is_button_pressed(1):
            vidas = 10
            sacrificios = 0
            VEL_INI = 90
            VEL_ALI = 180
            VEL_INI1 = 260
            VEL_ALI1 = 260
            INTERVALO_INI = 2000
            INTERVALO_INI1 = 1200
            INTERVALO_ALI = 2500
            INTERVALO_ALI1 = 2500
            INTERVALO_DOUR = 20000
            INTERVALO_BUR = 8000
            INTERVALO_POR = 7500
            GAME_STATE = 4
        if teclado.key_pressed("ESC"):
            janela.close()

    elif GAME_STATE == 1:
        tempoUltimoTiro, arco,flechas,escudo = capturarEntrada(sithe, tiros, tempoUltimoTiro,flechas)
        capturarEntrada(sithe, tiros, tempoUltimoTiro, flechas)

        movimentarTiros(tiros)
        desenharTudo(background_01, sithe, tiros,dir)
        desenharSithe(sithe, arco,escudo,spriteDef)
        limitarMovimento(ALTURA_JANELA, sithe)
        removerTirosForaDaTela(tiros)
        tempoUltimoInimigo1 = criarInimigos1(inimigos1, tempoUltimoInimigo1,GAME_STATE)
        desenharInimigos(inimigos1)
        GAME_STATE,sacrificios = movimentarInimigo(inimigos1,GAME_STATE,vidas,sacrificios)
        movimentarInimigo(inimigos1,GAME_STATE,vidas,sacrificios)
        tempoUltimoAliado = criarAliados(aliados,tempoUltimoAliado)
        movimentarAliado(aliados)
        desenharAliados(aliados)
        vidas,dano,posP0,posP1,posP2,posP3 = colisaoInimigoSithe(inimigos1,aliados,sithe,vidas,dano,escudo,spriteDef,tiros,portais,posP0,posP1,posP2,posP3)
        desenharBarra(dano)
        INTERVALO_INI,INTERVALO_ALI, VEL_INI,VEL_ALI,kills = colisaoFlechaInimigo(inimigos1, tiros, INTERVALO_INI,INTERVALO_ALI, VEL_INI,VEL_ALI,kills)
        tempoUltimoTiro, arco,flechas,escudo = capturarEntrada(sithe, tiros, tempoUltimoTiro,flechas)
        removerAliadosFora(aliados)
        removerInimigosForaDaTela(inimigos1)
        if kills==20:
            GAME_STATE = 5
        janela.draw_text("Score: "+str(inimigo.score),
                         1130, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text(str(flechas),
                         50, 25, 20, (255, 255, 255), "Impact")
        janela.draw_text( str(vidas),
                         50, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Stage: 1",
                         1050, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Sacrifices: " + str(sacrificios),
                         940, 0, 20, (255, 255, 255), "Impact")
        janela.update()


    elif GAME_STATE == 2:
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.draw_text("Game Over",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.draw_text("Youre dead and cant protect Temerant from the Cthaeh",
                         300, 300, 30, (255, 255, 255), "Impact")
        janela.draw_text("Score: " + str(inimigo.score),
                         470, 400, 70, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()


    elif GAME_STATE == 3:
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.draw_text("Game Over",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.draw_text("You couldnt stop Kvothe from reaching the Cthaeh",
                         300, 300, 30, (255, 255, 255), "Impact")
        janela.draw_text("Score: " + str(inimigo.score),
                         470, 400, 70, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()


    elif GAME_STATE == 4:
        story = GameImage("story.png")
        story.set_position(200,150)
        story.draw()

        janela.draw_text("Press SPACE to continue",
                         400,450, 40, (255, 255, 255), "Calibri")
        janela.draw_text("Story ",
                         470, 0, 100, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()
        if teclado.key_pressed("SPACE"):
            GAME_STATE = 1
        if teclado.key_pressed("ESC"):
            janela.close()

    elif GAME_STATE == 5:
        spr = Sprite("gris.png", 4)
        tempoUltimoTiro, arco, flechas1, escudo = capturarEntrada(sithe, tiros, tempoUltimoTiro, flechas1)
        capturarEntrada(sithe, tiros, tempoUltimoTiro, flechas1)

        movimentarTiros(tiros)
        desenharTudo(background_01, sithe, tiros, dir)
        desenharSithe(sithe, arco, escudo, spriteDef)
        limitarMovimento(ALTURA_JANELA, sithe)
        removerTirosForaDaTela(tiros)
        tempoUltimoInimigo1 = criarInimigos1(inimigos1, tempoUltimoInimigo1,GAME_STATE)
        desenharInimigos(inimigos1)
        GAME_STATE,sacrificios = movimentarInimigo1(inimigos1, GAME_STATE, vidas,sacrificios)
        tempoUltimoAliado1 = criarAliados(aliados1, tempoUltimoAliado1)
        tempoUltimoDourado = criarDour(dourados,tempoUltimoDourado)
        movimentarAliado1(dourados, setasCima, setasBaixo)
        desenharAliados(dourados)
        movimentarAliado1(aliados1,setasCima,setasBaixo)
        desenharAliados(aliados1)
        tempoUltimoBuraco,posB0,posB1,posB2,posB3 = criarBuracos(buracos, tempoUltimoBuraco,posB0,posB1,posB2,posB3)
        desenharBuracos(buracos)
        vidas, dano,posP0,posP1,posP2,posP3 = colisaoInimigoSithe(inimigos1, aliados1, sithe, vidas, dano, escudo, spriteDef, tiros,portais,posP0,posP1,posP2,posP3)
        vidas, dano ,posP0,posP1,posP2,posP3 = colisaoInimigoSithe([], dourados, sithe, vidas, dano, escudo, spriteDef, tiros, portais,posP0,posP1,posP2,posP3)
        posB0,posB1,posB2,posB3 = colisaoBuracoInimigo(inimigos1, buracos,spr,posB0,posB1,posB2,posB3)
        posB0,posB1,posB2,posB3 = colisaoBuracoInimigo(aliados1, buracos,spr1,posB0,posB1,posB2,posB3)
        desenharBarra(dano)
        INTERVALO_INI1, INTERVALO_ALI1, VEL_INI1, VEL_ALI1,kills = colisaoFlechaInimigo(inimigos1, tiros, INTERVALO_INI1,
                                                                              INTERVALO_ALI1, VEL_INI1, VEL_ALI1,kills)
        if kills == 35 :
            GAME_STATE = 7
        tempoUltimoTiro, arco, flechas1, escudo = capturarEntrada(sithe, tiros, tempoUltimoTiro, flechas1)
        removerAliadosFora(aliados1)
        removerAliadosFora(dourados)
        removerInimigosForaDaTela(inimigos1)
        posB0,posB1,posB2,posB3,posD0,posD1,posD2,posD3 = colisaoBuracoDourado(dourados, buracos, dparado,posB0,posB1,posB2,posB3,posD0,posD1,posD2,posD3)
        desenharDparados(dparado)
        posD0, posD1, posD2, posD3 = colisaoInimigoDourado(dparado, inimigos1,posD0,posD1,posD2,posD3)
        janela.draw_text("Score: " + str(inimigo.score),
                         1130, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text(str(flechas1),
                         50, 25, 20, (255, 255, 255), "Impact")
        janela.draw_text(str(vidas),
                         50, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Stage: 2",
                         1050, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Sacrifices: "+str(sacrificios),
                         940, 0, 20, (255, 255, 255), "Impact")
        janela.update()

    elif GAME_STATE == 6:
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.draw_text("Game Over",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.draw_text("You couldnt stop Haliax from reaching the Cthaeh",
                         300, 300, 30, (255, 255, 255), "Impact")
        janela.draw_text("Score: " + str(inimigo.score),
                         470, 400, 70, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()

    elif GAME_STATE == 7:
        spr = Sprite("haliax.png", 4)
        tempoUltimoTiro, arco, flechas1, escudo, tempoUltimaSetaCima, tempoUltimaSetaBaixo = capturarEntrada2(sithe, tiros, tempoUltimoTiro, flechas2, setasCima, setasBaixo, tempoUltimaSetaCima,
                         tempoUltimaSetaBaixo)
        capturarEntrada2(sithe, tiros, tempoUltimoTiro, flechas2, setasCima, setasBaixo, tempoUltimaSetaCima,
                         tempoUltimaSetaBaixo)
        movimentarSetas(setasCima)
        movimentarSetas(setasBaixo)
        movimentarTiros(tiros)
        desenharTudo(background_01, sithe, tiros, dir)
        desenharSetas(setasCima)
        desenharSetas(setasBaixo)
        desenharSithe(sithe, arco, escudo, spriteDef)
        limitarMovimento(ALTURA_JANELA, sithe)
        removerTirosForaDaTela(tiros)
        tempoUltimoInimigo1 = criarInimigos1(inimigos1, tempoUltimoInimigo1,GAME_STATE)
        desenharInimigos(inimigos1)
        GAME_STATE,sacrificios = movimentarInimigo1(inimigos1, GAME_STATE, vidas,sacrificios)
        tempoUltimoDourado = criarDour(dourados, tempoUltimoDourado)
        movimentarAliado1(dourados, setasCima, setasBaixo)
        desenharAliados(dourados)
        tempoUltimoAliado1 = criarAliados(aliados1, tempoUltimoAliado1)
        movimentarAliado1(aliados1,setasCima,setasBaixo)
        desenharAliados(aliados1)
        tempoUltimoBuraco,posB0, posB1, posB2, posB3 = criarBuracos(buracos, tempoUltimoBuraco,posB0, posB1, posB2, posB3)
        tempoUltimoPortal,posP0,posP1,posP2,posP3 = criarPortais(portais,tempoUltimoPortal,posP0,posP1,posP2,posP3)
        desenharBuracos(buracos)
        desenharBuracos(portais)
        vidas, dano,posP0,posP1,posP2,posP3 = colisaoInimigoSithe(inimigos1, aliados1, sithe, vidas, dano, escudo, spriteDef, tiros,portais,posP0,posP1,posP2,posP3)
        vidas, dano,posP0,posP1,posP2,posP3 = colisaoInimigoSithe([], dourados, sithe, vidas, dano, escudo, spriteDef, tiros, portais,posP0,posP1,posP2,posP3)
        posB0, posB1, posB2, posB3 = colisaoBuracoInimigo(inimigos1, buracos, spr, posB0, posB1, posB2, posB3)
        posB0, posB1, posB2, posB3 = colisaoBuracoInimigo(aliados1, buracos, spr1, posB0, posB1, posB2, posB3)
        colisaoSetaInimigo(inimigos1,setasCima,setasBaixo)
        desenharBarra(dano)
        INTERVALO_INI1, INTERVALO_ALI1, VEL_INI1, VEL_ALI1, kills = colisaoFlechaInimigo(inimigos1, tiros,
                                                                                         INTERVALO_INI1,
                                                                                         INTERVALO_ALI1, VEL_INI1,
                                                                                         VEL_ALI1, kills)
        tempoUltimoTiro, arco, flechas1, escudo = capturarEntrada(sithe, tiros, tempoUltimoTiro, flechas1)
        removerAliadosFora(aliados1)
        removerAliadosFora(dourados)
        removerInimigosForaDaTela(inimigos1)

        posB0, posB1, posB2, posB3,posD0,posD1,posD2,posD3 = colisaoBuracoDourado(dourados, buracos, dparado,posB0, posB1, posB2, posB3,posD0,posD1,posD2,posD3)
        desenharDparados(dparado)
        posD0, posD1, posD2, posD3 = colisaoInimigoDourado(dparado, inimigos1,posD0,posD1,posD2,posD3)

        janela.draw_text("Score: " + str(inimigo.score),
                         1130, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text(str(flechas2),
                         50, 25, 20, (255, 255, 255), "Impact")
        janela.draw_text(str(vidas),
                         50, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Stage: 3",
                         1050, 0, 20, (255, 255, 255), "Impact")
        janela.draw_text("Sacrifices: " + str(sacrificios),
                         940, 0, 20, (255, 255, 255), "Impact")
        janela.update()

    elif GAME_STATE == 8:
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.draw_text("You Won",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.draw_text("Score: " + str(inimigo.score),
                         470, 400, 70, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()
    elif GAME_STATE == 9:
        background_01.draw()
        janela.draw_text("Stage 2",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.update()
        janela.delay(500)
        GAME_STATE = 5
    elif GAME_STATE == 10:
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.draw_text("Game Over",
                         400, 200, 100, (255, 255, 255), "Impact")
        janela.draw_text("You couldnt stop Felurian from reaching the Cthaeh",
                         300, 300, 30, (255, 255, 255), "Impact")
        janela.draw_text("Score: " + str(inimigo.score),
                         470, 400, 70, (255, 255, 255), "Impact")
        janela.update()
        background_02.draw()








