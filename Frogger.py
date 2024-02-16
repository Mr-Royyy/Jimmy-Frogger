import pygame
import sys
from pygame.locals import *
pygame.init()
WINDOW = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Hello World!")
fps = 60
fpsClock = pygame.time.Clock()
score = 0
cell_size = 100
frog_x = 550
frog_y = 950

car_x = 0
car_y = 725

car1_x = 1000
car1_y = 612

car2_x = 0
car2_y = 425

car3_x = 0
car3_y = 25

car4_x = 1000
car4_y= 230

car5_x = 0
car5_y = 133
#DEFINING COLOURS
GRASS = (80, 255, 0)
WHITE = (255,255,255)
GRAY = (128,128,128)
BLACK = (0,0,0)
BLUE = (30,0,250)
RED = (166,44, 43)
DARK_GRAY = (70, 70, 70)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
FROG = (1,80,32)
MAGENTA = (255, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                frog_x = frog_x - (cell_size )
            if event.key == K_RIGHT:
                frog_x = frog_x + (cell_size)
            if event.key == K_UP:
                frog_y = frog_y - (cell_size)
            if event.key == K_DOWN:
                frog_y = frog_y + (cell_size)
                
    WINDOW.fill(WHITE)
#PRINT THE GRASS
    pygame.draw.rect(WINDOW, GRASS, (0, 800, 1000, 200))
#PRINTING THE FIRST ROAD
    pygame.draw.rect(WINDOW, BLACK,(0, 600, 1000, 200))
    
    pygame.draw.rect(WINDOW, WHITE, (0, 700, 100, 2))
    pygame.draw.rect(WINDOW, WHITE, (200, 700, 100, 2))
    pygame.draw.rect(WINDOW, WHITE, (400, 700, 100, 2))
    pygame.draw.rect(WINDOW, WHITE, (600, 700, 100, 2))
    pygame.draw.rect(WINDOW, WHITE, (800, 700, 100, 2))
#PRINTING THE SECOND GRASS
    pygame.draw.rect(WINDOW, GRASS, (0, 500, 1000, 100))
#PRINTING THE WATER
    pygame.draw.rect(WINDOW, BLUE, (100, 500, 100, 100))
    pygame.draw.rect(WINDOW, BLUE, (400, 500, 200, 100))
#PRINTING THE SECOND ROAD
    pygame.draw.rect(WINDOW, BLACK,(0, 400, 1000, 100))
    
    pygame.draw.rect(WINDOW, WHITE,(0, 450, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(200, 450, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(400, 450, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(600, 450, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(800, 450, 100, 2))
#PRINTING THE THIRD GRASS
    pygame.draw.rect(WINDOW, GRASS, (0, 300, 1000, 100))
#PRINTING THE SECOND WATER
    pygame.draw.rect(WINDOW, BLUE, (700, 300, 100, 100))
    pygame.draw.rect(WINDOW, BLUE, (200, 300, 200, 100))
    

#PRINTING THE THIRD ROAD
    pygame.draw.rect(WINDOW, BLACK,(0, 0, 1000, 300))
    
    pygame.draw.rect(WINDOW, WHITE,(0, 102, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(200, 102, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(400, 102, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(600, 102, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(800, 102, 100, 2))
    
    pygame.draw.rect(WINDOW, WHITE,(0, 200, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(200, 200, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(400, 200, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(600, 200, 100, 2))
    pygame.draw.rect(WINDOW, WHITE,(800, 200, 100, 2))
#MAKING CARS
    pygame.draw.rect(WINDOW, RED, (car_x, 725, 80, 50))
    car_x = car_x + 11
    if car_x >= 1500:
        car_x = -100
    pygame.draw.rect(WINDOW, LIGHT_BLUE, (car_x + 30,725, 30, 50))
    car_x = car_x + 11
    if car_x >= 1500:
        car_x = -100
        
    pygame.draw.rect(WINDOW, BLUE, (car1_x, 612, 80, 50))
    car1_x = car1_x - 7
    if car1_x == 1200:
        car1_x = 1000
    pygame.draw.rect(WINDOW, LIGHT_BLUE, (car1_x + 15, 612, 30, 50))
    car1_x = car1_x - 7
    if car1_x <= -100:
        car1_x = 1000
        
        
    pygame.draw.rect(WINDOW, ORANGE, (car2_x, 425, 80, 50))
    car2_x = car2_x + 8.5
    if car2_x >= 1000:
        car2_x = -100
    pygame.draw.rect(WINDOW, LIGHT_BLUE, (car2_x + 40, 425, 30, 50))
    car2_x = car2_x + 8.5
    if car2_x >= 1000:
        car2_x = -100

    pygame.draw.rect(WINDOW, RED, (car3_x, 25, 80, 50))
    car3_x = car3_x + 9.6
    if car3_x >= 1500:
        car3_x = -100
    pygame.draw.rect(WINDOW, LIGHT_BLUE, (car3_x + 40,25, 30, 50))
    car3_x = car3_x + 9.5
    if car3_x >= 1500:
        car3_x = -100
        
    pygame.draw.rect(WINDOW, BLUE, (car4_x, 230, 80, 50))
    car4_x = car4_x - 6.5
    if car4_x == 1200:
        car4_x = 1000
    pygame.draw.rect(WINDOW, LIGHT_BLUE, (car4_x+ 10, 230, 30, 50))
    car4_x = car4_x - 6.5
    if car4_x <= -100:
        car4_x = 1000
        
    pygame.draw.rect(WINDOW, GRASS, (car5_x, 133, 80, 50))
    car5_x = car5_x + 9
    if car5_x >= 1000:
        car5_x = -100
    pygame.draw.rect(WINDOW, LIGHT_BLUE , (car5_x+30, 133, 40, 50))
    car5_x = car5_x + 9
    if car5_x >= 1000:
        car5_x = -100


#MAKING THE FROG
    pygame.draw.rect(WINDOW, RED,(frog_x - 7.5, frog_y - 60, 15,25))
    pygame.draw.circle(WINDOW,FROG , (frog_x, frog_y), cell_size / 2)
    pygame.draw.circle(WINDOW,LIGHT_BLUE , (frog_x - 15, frog_y - 20), 10)
    pygame.draw.circle(WINDOW,LIGHT_BLUE , (frog_x + 15, frog_y - 20), 10)

    frogLeft = frog_x - cell_size / 2
    frogRight = frog_x + cell_size / 2
    frogTop = frog_y - cell_size / 2
    frogBottom = frog_y + cell_size / 2

#HITBOX
    #pygame.draw.rect(WINDOW, (255, 255, 0), (frogLeft, frogTop, cell_size, cell_size), 1)

#COLLISSION DETECTION FOR THE FROG THE FIRST CAR
    if frog_x+cell_size / 2 >= car_x and frog_x <= car_x + 80 and frog_y <= car_y + 50 and frog_y + cell_size / 2 >= car_y:
        frog_x = 550
        frog_y = 950
        score = 0
#COLLISSION DETECTION FOR THE FROG THE SECOND CAR
    if frog_x+cell_size / 2 >= car1_x and frog_x <= car1_x + 80 and frog_y <= car1_y + 50 and frog_y + cell_size / 2 >= car1_y:
        frog_x = 550
        frog_y = 950
        score = 0
#COLLISSION DETECTION FOR THE FROG THE SECOND CAR
    if frog_x+cell_size / 2 >= car2_x and frog_x <= car2_x + 80 and frog_y <= car2_y + 50 and frog_y + cell_size / 2 >= car2_y:
        frog_x = 550
        frog_y = 950
        score = 0
#COLLISSION DETECTION FOR THE FROG THE SECOND CAR
    if frog_x+cell_size / 2 >= car3_x and frog_x <= car3_x + 80 and frog_y <= car3_y + 50 and frog_y + cell_size / 2 >= car3_y:
        frog_x = 550
        frog_y = 950
        score = 0
#COLLISSION DETECTION FOR THE FROG THE SECOND CAR
    if frog_x+cell_size / 2 >= car4_x and frog_x <= car4_x + 80 and frog_y <= car4_y + 50 and frog_y + cell_size / 2 >= car4_y:
        frog_x = 550
        frog_y = 950
        score = 0
#COLLISSION DETECTION FOR THE FROG THE SECOND CAR
    if frog_x+cell_size / 2 >= car5_x and frog_x <= car5_x + 80 and frog_y <= car5_y + 50 and frog_y + cell_size / 2 >= car5_y:
        frog_x = 550
        frog_y = 950
        score = 0
#IF THE FROG TOUCHES THE WATER THEN THE FROG DIES
    if frogRight > 700 and frogLeft < 800 and frogTop < 400 and frogBottom > 300:
        frog_x = 550
        frog_y = 950
        score = 0
#IF THE FROG TOUCHES THE WATER THEN THE FROG DIES
    if frogRight > 200 and frogLeft < 400 and frogTop < 400 and frogBottom > 300:
        frog_x = 550
        frog_y = 950
        score = 0
#IF THE FROG TOUCHES THE WATER THEN THE FROG DIES
    if frogRight > 100 and frogLeft < 200 and frogTop < 600 and frogBottom > 500:
        frog_x = 550
        frog_y = 950
        score = 0
#IF THE FROG TOUCHES THE WATER THEN THE FROG DIES

    if frogRight > 400 and frogLeft < 600 and frogTop < 600 and frogBottom > 500:
        frog_x = 550
        frog_y = 950
        score = 0
#IF THE FROG MAKES IT PAST THE LEVEL THEN SEND THEM BACK TO THE START.
    if frog_y < 0:
        frog_y = 950
        frog_x = 550
        score = score + 1
#DOESN'T LET FROG GO OFF THE SCREEN
#RIGHT
    if frog_x >= 1000:
        frog_x = frog_x - 100
#BOTTOM      
    if frog_y >=1000:
        frog_y = frog_y - 100
#LEFT      
    if frog_x <= 0:
        frog_x = frog_x + 100
        
       
        
#SCORE OF THE GAME
    font = pygame.font.SysFont("Arial", 20, True, True)

    text = font.render("Score : " + str(score), True, WHITE )

    WINDOW.blit(text, (875,25))
        
    

    
    
    pygame.display.update()
    fpsClock.tick(fps)