import pygame
import sys
import time
from pygame.locals import *

white = (255,255,255)
sky = (135,206,250)
brown = (128,0,0)
black = (0,0,0)

# ブロックなどのギミックの設置
masu =[] 
for y in range(22):
    masu.append([0]*30*5)
for x in range(30*5):
    masu[18][x] = 1 # ground1 == 1
    masu[19][x] = 1
    masu[17][x] = 3 # ground3 == 3
#for y in range(17):
    #masu[y][133] = 20 # carott == 20
for i in range(15): 
    masu[15-i][i+20] = 1
    masu[15-i][i+21] = 1
    masu[3][i+60] = 2 # ground2 == 2
    masu[6][i+60] = 2
    masu[9][i+60] = 2
    masu[12][i+60] = 2
    masu[15][i+60] = 2
for i in range(13):
    masu[15-i][58] = 2
    masu[15-i][76] = 2
masu[15][59] = 2
masu[9][59] = 2
masu[3][59] = 2
masu[16][76] = 2
masu[12][75] = 2
masu[6][75] = 2

masu[12][21] = 4 # ground_blue == 4
masu[12][20] = 4
masu[11][19] = 4
masu[10][18] = 4
masu[10][19] = 4
masu[11][20] = 4
masu[15][35] = 1

for y in range(3):
    for x in range(77,150):
        masu[y+17][x] = 5 # ground5 == 5

masu[18][83] = 6 # transparent == 6
masu[19][83] = 6
masu[17][83] = 6


for i in range(7):
    masu[14-i][i+34] = 1
    masu[14-i][i+35] = 1
for i in range(3):
    masu[17+i][97] = 7
    masu[17+i][98] = 7
    masu[17+i][101] = 7
    masu[17+i][102] = 7
    masu[17+i][105] = 7
    masu[17+i][106] = 7
    masu[17+i][109] = 7
    masu[17+i][110] = 7
    masu[17+i][115] = 7
    masu[17+i][116] = 7
    for k in range(3):
        masu[17+i][45+k] = 7
for i in range(19):
    masu[19][111+i] = 6
    masu[20][110+i] = 1
masu[20][129] = 1
masu[20][130] = 1
masu[19][129] = 6
masu[18][129] = 6
masu[17][129] = 6
masu[19][115] = 0
masu[19][116] = 0

    
title = pygame.image.load('shobon_image/title.png')    
ground = pygame.image.load('shobon_image/ground.png')
ground2 = pygame.image.load('shobon_image/ground2.png')
ground2_mono = pygame.image.load('shobon_image/ground2_mono.png')
ground_blue = pygame.image.load('shobon_image/ground_blue.png')
ground_mono = pygame.image.load('shobon_image/ground_mono.png')
ground3 = pygame.image.load('shobon_image/ground3.png')
ground3_mono = pygame.image.load('shobon_image/ground3_mono.png')
ground5 = pygame.image.load('shobon_image/ground5.png')
ground5_mono = pygame.image.load('shobon_image/ground5_mono.png')
cat_right = [pygame.image.load('shobon_image/cat_right1.png'),
       pygame.image.load('shobon_image/cat_right2.png'),
       pygame.image.load('shobon_image/cat_right3.png'),
       pygame.image.load('shobon_image/cat_right4.png')]
cat_left = [pygame.image.load('shobon_image/cat_left1.png'),
       pygame.image.load('shobon_image/cat_left2.png'),
       pygame.image.load('shobon_image/cat_left3.png'),
       pygame.image.load('shobon_image/cat_left4.png')]
cat_death = pygame.image.load('shobon_image/cat_death.png')
enemy1 = [ pygame.image.load('shobon_image/かに.png'),
pygame.image.load('shobon_image/イカ.png'),
pygame.image.load('shobon_image/タコ.png'),
pygame.image.load('shobon_image/青いカバ.png'),
pygame.image.load('shobon_image/おばけ.png')
]
enemy2 = pygame.image.load('shobon_image/うんちハニワ.png')
enemy3 = pygame.image.load('shobon_image/fire.png')
enemy5 = pygame.image.load('shobon_image/face.png')
swordsman = pygame.image.load('shobon_image/swordsman.png')
waypoint = pygame.image.load('shobon_image/waypoint.png')
vector = [pygame.image.load('shobon_image/vector1.png'),
          pygame.image.load('shobon_image/vector2.png')]
fish = pygame.image.load('shobon_image/fish.png')
fisherman = pygame.image.load('shobon_image/fisherman.png')
banana = pygame.image.load('shobon_image/banana.png')
enemy6 = pygame.image.load('shobon_image/bat.png')
goal_flug = pygame.image.load('shobon_image/goal_flug.png')


idx = 0
index = 0
sc = 0
hi = 0
hi_plus = 0
ene1 = 1
ene2 = 1
ene3 = 1
ene4 = 1
ene5 = 1
ene6 = 1
pl_x = 0
tmr = 0
ene1_t = 1
ene2_t = 1
ene3_t = 1
ene4_t = 1
ene5_t = 1
ene6_t = 1
goal = 1
cat_direct = 1
tmr_1 = 0
life = 0


def masu_init():
    for y in range(20):
        for x in range(30*5):
            masu[y][x] = 0

def game_over():
    global idx,life
    life = life - 1
    idx = 10
    death_sound = pygame.mixer.Sound('shobon_sound/death_sound.mp3')
    death_sound.set_volume(0.03)
    death_sound.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.load('shobon_sound/death_bgm.mp3')
    pygame.mixer.music.play()

def game_set():
    global sc,hi,hi_plus,idx,pl_x,ene1,ene2,ene3,ene4,ene5,ene6,tmr,ene1_t,ene2_t,ene3_t,ene4_t,ene5_t,ene6_t,goal,cat_direct,tmr_1,life
    if index == 0:
        sc = 0
        hi = 0
        hi_plus = 0
        pl_x = 0
        ene1 = 1
        ene2 = 1
        ene3 = 1
        ene1_t = 1
        ene2_t = 1
        ene3_t = 1
        tmr = 0
        goal = 1
        cat_direct = 1
        tmr_1 = 0
        if idx == 9:
            life = 0
            time.sleep(1)
        elif idx == 10:
            time.sleep(4)
        idx = 0
    if index == 1:
        tmr = 0
        tmr_1 = 0
        idx = 2
        hi = 0
        hi_plus = 0
        cat_direct = 1
        ene4 = 1
        ene4_t = 1
        ene5 = 1
        ene5_t = 1
        ene6 = 1
        ene6_t = 1
        sc = 480-30-30*85
        time.sleep(4)
    pygame.mixer.music.load('shobon_sound/bgm.mp3')
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)

def game_goal():
    global idx
    idx = 9
    goal_sound = pygame.mixer.Sound('shobon_sound/goal_sound.mp3')
    goal_sound.set_volume(0.03)
    goal_sound.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('shobon_sound/goal_bgm.mp3')
    pygame.mixer.music.play(-1)

    
def main():
    global sc,hi,hi_plus,idx,pl_x,ene1,ene2,ene3,ene4,ene5,ene6,tmr,ene1_t,ene2_t,ene3_t,ene4_t,ene5_t,ene6_t,goal,cat_direct,tmr_1,index,life
    pygame.init()
    pygame.display.set_caption('carzy cat')
    screen = pygame.display.set_mode((990,600))
    pygame.mixer.music.load('shobon_sound/bgm.mp3')
    se = pygame.mixer.Sound('shobon_sound/jump_sound.mp3')
    se.set_volume(0.03)
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    fontl = pygame.font.Font(None,40)
    fontg = pygame.font.Font(None,150)
    fonts = pygame.font.Font(None,180)
    
        
        
    while True:
        tmr = tmr+1
        cat_change = (int((tmr/20)))%4
        vector_change = int((tmr/15))%2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(sky)
        key = pygame.key.get_pressed()

                
        if idx == 1: # ゲーム開始
            # キーの処理
            pl_x = int((480 - sc+13)/30)
            if key[pygame.K_RIGHT] == 1 and (masu[int((480+hi)/30)][int((480-sc+30)/30)] == 0 ): # 右に動く
                sc = sc - 8
                cat_direct = 1
            if key[pygame.K_LEFT] == 1 and sc < 0 and (masu[int((480+hi)/30)][int((480-sc)/30)] == 0) : # 左に動く
                sc = sc + 8
                cat_direct = -1
            if key[pygame.K_UP] == 1 and hi_plus == 0 and (masu[int((480+hi+30)/30)][pl_x] != 0 ) and tmr_1 == 0:# ジャンプ動作を始めるフラグを立てる
                hi_plus = 1
                se.play()
            if 1 <= hi_plus <= 11: # ジャンプ開始(上に上がる)
                if 1 <= hi_plus <= 7 :
                    if (masu[int((480+hi-30)/30)][pl_x] == 0 ):
                        hi = hi - 30
                    else:
                        hi_plus = 7
                if hi_plus == 7:# ジャンプ終了
                    hi_plus = -1
                    tmr_1 = 10
                hi_plus = hi_plus + 1

            if tmr_1 > 0: # ジャンプクールタイム
                tmr_1 = tmr_1 - 1
                
            if hi_plus == 0 :# 落ちる処理
                if  (masu[int((480+hi+30)/30)][pl_x] == 0 or masu[int((480+hi+30)/30)][pl_x] == 6 ):
                    hi =hi+ 30
                elif 30*45+sc < 480 and 480 < 30*47+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi + 30
                elif 30*97+sc < 480 and 480 < 30*98+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*101+sc < 480 and 480 < 30*102+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*105+sc < 480 and 480 < 30*106+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*109+sc < 480 and 480 < 30*110+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*115+sc < 480 and 480 < 30*116+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30

        

            if ene1 == 1 and pl_x == 20: # 敵1号たちの登場 
                ene1 = 2 
            if  ene1 == 2 and 0 < 1000-ene1_t*10+(30*4+60)*4+300 : # 敵1号たち
                    ene1_t = ene1_t + 1
                    #for i in range(4):
                    screen.blit(enemy1[0],[1000-ene1_t*3+(30*i+60)*0+sc,480-30*0])
                    #screen.blit(enemy1[4],[1000-ene1_t*10+(30*4+60)*4,480-30*10-10]) 
            if ((-30 < hi <= 0) and 1000-ene1_t*3+sc < 480+30 and 480 < 1000-ene1_t*3+30+sc): # 敵1号たちと当たったら
                """((-(30+30) < hi <= 0) and 1000-ene1_t*10+(30+60) < 480+30 and 480 < 1000-ene1_t*10+(30+60)+30*2) or
                ((-(30+30*2) < hi <= 0) and 1000-ene1_t*10+(30*2+60)*2 < 480+30 and 480 < 1000-ene1_t*10+(30*2+60)*2+30*3) or
                ((-(30+30*3) < hi <= 0) and 1000-ene1_t*10+(30*3+60)*3 < 480+30 and 480 < 1000-ene1_t*10+(30*3+60)*3+30*4) or
                ((-(30+30*10) < hi <= -30) and 1000-ene1_t*10+(30*4+60)*4 < 480+30 and 480 < 1000-ene1_t*10+(30*4+60)*4+30*10)
                ) :"""
                game_over()

    

            if hi == 30*4: # 落とし穴に落ちたら
                game_over()

            if ene2 == 1 and pl_x == 47: # 敵2号たちの登場
                ene2 = 2
            if ene2 == 2 and 600-10*ene2_t+200+60 > 0: # 敵2号たち
                ene2_t = ene2_t + 1
                screen.blit(enemy2,[30*49+sc,600-10*ene2_t])
                screen.blit(enemy2,[30*51+sc,600-10*ene2_t+100])
                screen.blit(enemy2,[30*53+sc,600-10*ene2_t+200])
            if ((30*49+sc < 480+30 and 480 < 30*49+sc+30 and 600-10*ene2_t < 480+hi+30 and 480+hi < 600-10*ene2_t+60)or # 敵2号たちとあたったら
                (30*51+sc < 480+30 and 480 < 30*51+sc+30 and 600-10*ene2_t+100 < 480+hi+30 and 480+hi < 600-10*ene2_t+100+60)or
                (30*53+sc < 480+30 and 480 < 30*53+sc+30 and 600-10*ene2_t+200 < 480+hi+30 and 480+hi < 600-10*ene2_t+200+60)):
                game_over()

            if ene3 == 1 and pl_x == 55: # 敵3号たちの登場
                ene3 = 2
            if ene3 == 2 and pl_x <= 80: # 敵3号たち
                ene3_t = ene3_t + 1
                ene3_1 = ene3_t%60
                ene3_2 = (ene3_t+10)%60
                ene3_3 = (ene3_t+20)%60
                ene3_4 = (ene3_t+30)%60
                ene3_5 = (ene3_t+40)%60
                ene3_6 = (ene3_t+50)%60
                screen.blit(enemy3,[30*61+sc,ene3_1*10])
                screen.blit(enemy3,[30*63+sc,ene3_3*10])
                screen.blit(enemy3,[30*65+sc,ene3_5*10])
                screen.blit(enemy3,[30*67+sc,ene3_4*10])
                screen.blit(enemy3,[30*69+sc,ene3_2*10])
                screen.blit(enemy3,[30*71+sc,ene3_1*10])
                screen.blit(enemy3,[30*73+sc,ene3_3*10])
            if ((30*61+sc < 480+30 and 480 < 30*61+sc+30 and ene3_1*10 < 480+hi+30 and 480+hi < ene3_1*10+30)or # 敵3号に当たったら
                (30*63+sc < 480+30 and 480 < 30*63+sc+30 and ene3_3*10 < 480+hi+30 and 480+hi < ene3_3*10+30)or
                (30*65+sc < 480+30 and 480 < 30*65+sc+30 and ene3_5*10 < 480+hi+30 and 480+hi < ene3_5*10+30)or
                (30*67+sc < 480+30 and 480 < 30*67+sc+30 and ene3_4*10 < 480+hi+30 and 480+hi < ene3_4*10+30)or
                (30*69+sc < 480+30 and 480 < 30*69+sc+30 and ene3_2*10 < 480+hi+30 and 480+hi < ene3_2*10+30)or
                (30*71+sc < 480+30 and 480 < 30*71+sc+30 and ene3_1*10 < 480+hi+30 and 480+hi < ene3_1*10+30)or
                (30*73+sc < 480+30 and 480 < 30*73+sc+30 and ene3_3*10 < 480+hi+30 and 480+hi < ene3_3*10+30)):
                game_over()

            if 30*85+sc < 480+30 and 480 < 30*85+sc+30 and 420 < 480+hi+30 and 480+hi < 420+90: # 中間地点
                way = pygame.mixer.Sound('shobon_sound/waypoint_sound.mp3')
                way.set_volume(0.03)
                way.play()
                idx = 2
                

        if idx == 2: # 中間地点から
            pl_x = int((480 - sc+13)/30)
            index = 1
            if key[pygame.K_RIGHT] == 1 and (masu[int((480+hi)/30)][int((480-sc+30)/30)] == 0 or masu[int((480+hi)/30)][int((480-sc+30)/30)] == 6): # 右に動く
                sc = sc - 8
                cat_direct = 1
            if key[pygame.K_LEFT] == 1 and sc < 0 and (masu[int((480+hi)/30)][int((480-sc)/30)] == 0) : # 左に動く
                sc = sc + 8
                cat_direct = -1
            if key[pygame.K_UP] == 1 and hi_plus == 0 and (masu[int((480+hi+30)/30)][pl_x] != 0 ) and tmr_1 == 0:# ジャンプ動作を始めるフラグを立てる
                hi_plus = 1
                se.play()
            if 1 <= hi_plus <= 11: # ジャンプ開始(上に上がる)
                if 1 <= hi_plus <= 7 :
                    if (masu[int((480+hi-30)/30)][pl_x] == 0 )or(masu[int((480+hi-30)/30)][pl_x] == 6 ) :
                        hi = hi - 30
                    else:
                        hi_plus = 7
                if hi_plus == 7:# ジャンプ終了
                    hi_plus = -1
                    tmr_1 = 10
                hi_plus = hi_plus + 1

            if tmr_1 > 0: # ジャンプクールタイム
                tmr_1 = tmr_1 - 1
                
            if hi_plus == 0 :# 落ちる処理
                if  (masu[int((480+hi+30)/30)][pl_x] == 0 or masu[int((480+hi+30)/30)][pl_x] == 6 ):
                    hi =hi+ 30
                elif 30*45+sc < 480 and 480 < 30*47+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi + 30
                elif 30*97+sc < 480 and 480 < 30*98+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*101+sc < 480 and 480 < 30*102+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*105+sc < 480 and 480 < 30*106+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*109+sc < 480 and 480 < 30*110+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30
                elif 30*115+sc < 480 and 480 < 30*116+sc+30 and 0 <= hi and masu[int((480+hi+30)/30)][pl_x] == 7:
                    hi = hi+30

            if hi == 30*4: # 落とし穴に落ちたら
                game_over()

            if 30*90+sc < 480+30 and 480 < 30*90+sc+30 and 480 < 480+hi+30 and 480+hi < 480+30 and ene4 == 1: # 敵4号の登場
                ene4 = 2
            if ene4 == 2 and 30*100+sc-10*ene4_t+510 > 0: # 敵4号
                ene4_t = ene4_t + 1
                screen.blit(fisherman,[30*100+sc-10*ene4_t,0])
            if 480+30 > 30*100+sc-10*ene4_t and ene4 == 2: # 敵4号に当たったら
                ene4 = 3
                game_over()

            if ene5 == 1 and pl_x == 95: # 敵5号たち
                ene5 = 2
            if ene5 == 2 and 600-10*ene5_t+60 > 0: # 敵5号-1
                ene5_t = ene5_t + 1
                screen.blit(enemy5,[30*97+sc,600-15*ene5_t])
                if 30*97+sc < 480+30 and 480 < 30*97+sc+60 and 600-15*ene5_t < 480+hi+30 and 480+hi < 600-15*ene5_t+60:
                    game_over()
            if ene5 == 2 and pl_x == 100: # 敵5号-2
                ene5 = 3
                ene5_t = 1
            if ene5 == 3 and 300+10*ene5_t < 600:
                ene5_t = ene5_t + 1
                screen.blit(enemy5,[30*101+sc,200+15*ene5_t])
                if  30*101+sc < 480+30 and 480 < 30*101+sc+60 and 200+15*ene5_t < 480+hi+30 and 480+hi < 200+15*ene5_t+60:
                    game_over()
            if ene5 == 3 and pl_x == 103: # 敵5号-3
                ene5 = 4
                ene5_t = 1
            if ene5 == 4 and 600-25*ene5_t+60 > 0:
                ene5_t = ene5_t + 1
                screen.blit(swordsman,[30*104+sc,600-25*ene5_t])
                if  30*104+sc < 480+30 and 480 < 30*104+sc+30 and 600-25*ene5_t < 480+hi+30 and 480+hi < 600-25*ene5_t+60:
                    game_over()

            if 30*113+sc < 480+30 and 480 < 30*113+sc+30 and 480 < 480+hi+30 and 480+hi < 480+30: # bananaに当たったら
                idx = 3
                
            if hi == 30*2 and (pl_x == 115 or pl_x == 116): # 特殊な落ち方
                game_over()

            if ene6 == 1 and pl_x == 119: # 敵6号たち
                ene6 = 2
            if ene6 == 2 :
                ene6_t = ene6_t + 1
                ene6_mod = int((ene6_t/5))%2
                screen.blit(enemy6,[30*122+sc,480-ene6_mod*20])
                screen.blit(enemy6,[30*123+sc,450+ene6_mod*15])
                screen.blit(enemy6,[30*124+sc,430-ene6_mod*20])
                screen.blit(enemy6,[30*124+sc,420+ene6_mod*30])
                screen.blit(enemy6,[30*125+sc,460-ene6_mod*50])
                screen.blit(enemy6,[30*126+sc,450-ene6_mod*25])
            if ((30*122+sc < 480+30 and 480 < 30*122+sc+60 and 480-ene6_mod*20 < 480+hi+30 and 480+hi < 480-ene6_mod*20+30)or
                (30*123+sc < 480+30 and 480 < 30*123+sc+60 and 450+ene6_mod*15 < 480+hi+30 and 480+hi < 450+ene6_mod*15+30)or
                (30*124+sc < 480+30 and 480 < 30*124+sc+60 and 430-ene6_mod*20 < 480+hi+30 and 480+hi < 430-ene6_mod*20+30)or
                (30*124+sc < 480+30 and 480 < 30*124+sc+60 and 420+ene6_mod*30 < 480+hi+30 and 480+hi < 420+ene6_mod*30+30)or
                (30*125+sc < 480+30 and 480 < 30*125+sc+60 and 460-ene6_mod*50 < 480+hi+30 and 480+hi < 460-ene6_mod*50+30)or
                (30*126+sc < 480+30 and 480 < 30*126+sc+60 and 450-ene6_mod*25 < 480+hi+30 and 480+hi < 450-ene6_mod*25+30)):
                game_over()


            
        if idx == 3: # banana処理
            if 30*90+sc < 480:
                sc = sc + 15
            else :
                idx = 2

        

            


        if 135 <= pl_x and goal == 1: # Goal判定
                goal = 0
                game_goal()

        for y in range(20):# ブロックandラビットの表示
             for x in range(30*5):
                 if masu[y][x] == 1: 
                     screen.blit(ground,[30*x+sc,30*y])
                 if masu[y][x] == 2:
                     screen.blit(ground2,[30*x+sc,30*y])    
                 if masu[y][x] == 3:
                     screen.blit(ground3,[30*x+sc,30*y])
                 if masu[y][x] == 4:
                     screen.blit(ground_blue,[30*x+sc,30*y])
                 if masu[y][x] == 5 or masu[y][x] == 6:
                     screen.blit(ground5,[30*x+sc,30*y])
             txtl = fontl.render('life {}'.format(life),True,black)
             screen.blit(txtl,[20,20])       
             screen.blit(waypoint,[30*85+sc,420])
             screen.blit(vector[vector_change],[30*85+sc,420-60])
             screen.blit(fish,[30*90+sc,480])
             screen.blit(banana,[30*113+sc,480])
             screen.blit(goal_flug,[30*134+sc,420])
        if cat_direct == 1:
             screen.blit(cat_right[cat_change],[480,480+hi])
        if cat_direct == -1:
             screen.blit(cat_left[cat_change],[480,480+hi])

        if idx == 0: # タイトル画面
            txt1 = fonts.render('CRAZY CAT',True,white)
            txt2 = font.render('Press SPACE',True,white)
            screen.blit(title,[65,70])
            screen.blit(txt1,[140,120])
            screen.blit(txtl,[20,20])
            if 3 <= tmr%20 <= 18:
                screen.blit(txt2,[320,300])
            if key[K_SPACE] == 1:
                idx = 1
                
        if idx == 9: # Goal
            txt3 = fontg.render('Congratulations!!',True,white)
            txt2 = font.render('Restart [R]key',True,white)
            screen.blit(txt3,[35,150])
            screen.blit(txtl,[20,20])
            if 3 <= tmr%20 <= 18:
                screen.blit(txt2,[300,300])
            pygame.display.update()
            if key[K_r] == 1:
                index = 0
                game_set()
            
            
               
        if idx == 10: # ゲームオーバー
            screen.fill((102,102,102))
            for y in range(22):
                for x in range(30*5):
                    if masu[y][x] == 1 or masu[y][x] == 4: 
                        screen.blit(ground_mono,[30*x+sc,30*y])
                    if masu[y][x] == 2:
                        screen.blit(ground2_mono,[30*x+sc,30*y])
                    if masu[y][x] == 3:
                        screen.blit(ground3_mono,[30*x+sc,30*y])
                    if masu[y][x] == 5:
                        screen.blit(ground5_mono,[30*x+sc,30*y])
            screen.blit(txtl,[20,20])
            screen.blit(waypoint,[30*85+sc,420])
            screen.blit(vector[vector_change],[30*85+sc,420-60])
            screen.blit(fish,[30*90+sc,480])
            screen.blit(banana,[30*113+sc,480])
            screen.blit(goal_flug,[30*134+sc,420])
            screen.blit(cat_death,[480,480+hi+10])
            txt1 = fonts.render('Game Over',False,black)
            screen.blit(txt1,[150,200])
            pygame.display.update()
            game_set()
            
            
        pygame.display.update()
        clock.tick(22)

if __name__ == '__main__':
    main()
