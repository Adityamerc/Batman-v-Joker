import pygame
import random
import math
import time
from pygame import mixer

#initialize
pygame.init()

#blank screen window
screen = pygame.display.set_mode((800,600)) #(x,y)

#title
pygame.display.set_caption("Batman vs Joker")


#batman icon
batmanIcon = pygame.image.load('batman.png') #get and load the img
batmanX = 400
batmanY = 500
batmanX_change = 0
batmanY_change = 0

#joker icon
jokerIcon = pygame.image.load('joker.png') #get and load the img
jokerX = random.randint(0,800) #so that the loop keeps moving
jokerY = 50
jokerX_change = 2

#throw batarang ball
batarangIcon = pygame.image.load('batarang.png') #get and load the img
batarangX = 0 #value changed inside while loop
batarangY = 500 #so that this ball hides behind the player ball
batarangY_change = 3
state = "ready"

#batman joker background
batjokIcon = pygame.image.load('batmanjoker.jpeg')

#bgm
mixer.music.load("batman-song.mp3") #song on  loop
mixer.music.play(-1)

#function to load the batman img on the window
def batman(x,y):
    screen.blit(batmanIcon, (x,y))

#function to load the batarang img on the window
def batarang(x,y):
    global state
    state = "shoot" #state changes from ready to shoot when this func is called
    screen.blit(batarangIcon, (x,y))    

#function to load the joker img on the window
def joker(x,y):
    screen.blit(jokerIcon, (x,y))

#function to detect when batarang hits the joker
def isHit(jokerX,jokerY,batarangX,batarangY):
    d = math.sqrt(math.pow(jokerX - batarangX,2) + math.pow(jokerY - batarangY,2))
    
    if d < 50:
        return True
    else:
        return False
        
#score
score_val = 0

#to show the score on window
font = pygame.font.Font("Retro Computer.otf", 32)
scoreX = 10
scoreY = 10

title_font = pygame.font.Font("BARIKA.ttf", 50)
title_1X = 325
title_1Y = 280

title_2X = 355
title_2Y = 310

title_3X = 335
title_3Y = 340

def show_score(x,y):
    score = font.render("Score: " + str(score_val), True, (255,255,255))
    screen.blit(score, (x,y))

def gameTitle(a,b,c,d,e,f):
    title_1 =  title_font.render("Batman", True, (0,0,0))
    screen.blit(title_1, (a,b))

    title_2 =  title_font.render("vs", True, (0,0,0))
    screen.blit(title_2, (c,d))

    title_3 =  title_font.render("Joker", True, (0,0,0))
    screen.blit(title_3, (e,f))
#game window 
boo = True
while boo:
    screen.fill((255,0,0)) #bg color

    #batjok background
    screen.blit(batjokIcon, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit wehn 'x' is clicked
            
            boo = False
    
    #to control the movements of batman
    #to check if a button is pressed
    if event.type == pygame.KEYDOWN:       

        if event.key == pygame.K_LEFT:            
                batmanX_change = -3            

        if event.key == pygame.K_RIGHT:
                batmanX_change = 3

        if event.key == pygame.K_UP:
                batmanY_change = -3

        if event.key == pygame.K_DOWN:
                batmanY_change = 3                

        if event.key == pygame.K_SPACE:
            if state == "ready":
                
                batarangX = batmanX
                batarangY = batmanY
                batarang(batarangX, batarangY)
            
                
    #to check if a button is released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:            
            batmanX_change = 0
            batmanY_change = 0

    #while pressing spacebar
    if state is "shoot":

        #calling batarang icon func
        batarang(batarangX, batarangY)
        batarangY -= batarangY_change
    if batarangY <= 0:#when the ball reaches y=0 it resets the ball to its og pos
        batarangY = 500
        state = "ready"
        
    #to control the batman
    batmanX += batmanX_change
    batmanY += batmanY_change


    #to not go out of bounds
    if batmanX <= 0:
        batmanX = 0
    if batmanX >= 704:
        batmanX = 704 

    #to keep the loop moving in x
    jokerX += jokerX_change
    #to not go out of bounds
    if jokerX <= 0:
        if jokerY < 200:
            jokerY = random.randint(0,50)        
        jokerX_change = 2
    if jokerX >= 704:
        if jokerY < 200:
            jokerY = random.randint(0,50)        
        jokerX_change = -2

    if isHit(jokerX,jokerY,batarangX,batarangY):
        
        state = "ready"
        batarangY  = 500
        score_val += 1       
        jokerX = random.randint(0,800)
        jokerY = 50
        
    batman(batmanX, batmanY) #func call to load the batman icon
    joker(jokerX, jokerY) #func call to load the joker icon
    show_score(scoreX, scoreY) #func call to load the score  
    gameTitle(title_1X, title_1Y, title_2X, title_2Y, title_3X, title_3Y) #func call to load the game title    

    
    pygame.display.update() #update the game window always
    
    