#import all the the neccesary moduels. 
import pygame
from PIL import Image, ImageDraw
import time
from pygame.locals import *
import random
import math
pygame.font.init()
#Font
Font = pygame.font.SysFont('Arial', 100)
#Grid from test.txt
map_1 = []
#Tile_1
tile_1 = []
#Tile_2
tile_2 = []
#Tile_3
tile_3 = []
#LOts of lists, that are not apparently lists or Something! I use them as lists, and I can call them easily
sprite_list_1 = (['Sprites_1/Left_1.png', 'Sprites_1/Right_1.png', 'Sprites_1/Forward_1.png', 'Sprites_1/Back_1.png', 'Sprites_1/display_IMG_1.png'])
sprite_list_2 = (['Sprites_1/Left_2.png', 'Sprites_1/Right_2.png', 'Sprites_1/Forward_2.png', 'Sprites_1/Back_2.png', 'Sprites_1/display_IMG_2.png'])
sprite_list_3 = (['Sprites_1/Left_3.png', 'Sprites_1/Right_3.png', 'Sprites_1/Forward_3.png', 'Sprites_1/Back_3.png', 'Sprites_1/display_IMG_3.png'])
sprite_list_4 = (['Sprites_1/Left_4.png', 'Sprites_1/Right_4.png', 'Sprites_1/Forward_4.png', 'Sprites_1/Back_4.png', 'Sprites_1/display_IMG_4.png'])
sprite_list_5 = (['Sprites_1/Left_5.png', 'Sprites_1/Right_5.png', 'Sprites_1/Forward_5.png', 'Sprites_1/Back_5.png', 'Sprites_1/display_IMG_5.png'])
list_for_bulletspeed = (['Speed_imgs/Speed_1.png', 'Speed_imgs/Speed_2.png', 'Speed_imgs/Speed_3.png', 'Speed_imgs/Speed_4.png', 'Speed_imgs/Speed_5.png',])
list_for_tutorial = (['Tutorial_images/Tutorial_1.png','Tutorial_images/Tutorial_2.png','Tutorial_images/Tutorial_3.png'])
game_win_or_loss = (['Win_or_loss/YouWinScreen.png', 'Win_or_loss/YouLostScreen.png'])
#multidimesional array
what_sprite_list = [sprite_list_1, sprite_list_2, sprite_list_3, sprite_list_4, sprite_list_5]
intro_rect_animation = []
enemy_bullets = []
player_bullets = []
#variables, lots and lost of variables :(
imgnumb_1 = 0
imgnumb_2 = 4
Int_for_loading_bar = 0
enemy_bullet_shoot_x = 700
enemy_bullet_shoot_y = 0
player_bullet_shoot_x = 0
player_bullet_shoot_y = 0
size_height = 1
size_width = 1
speed_of_bullet = 1
Player_Vel = 5
did_you_win_or_loose = 0
what_tutorial_you_on = 0
#Bools
movement = True
pause = False
this_thing = True
#Screen stuff
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
#For pillow
img = Image.new('RGB', (800,800), color = (0,0,0))
#Intro_thing_kinda_laggy
timed_enemy_bullet_shoot = pygame.USEREVENT
pygame.time.set_timer(timed_enemy_bullet_shoot, 1)
MOVE_SIDE = 25
#Timer for start screen AND enemy shooting! Works super duper weird!
move_down_event = pygame.USEREVENT + 2
pygame.time.set_timer(move_down_event, MOVE_SIDE)
Timer_for_rects = pygame.USEREVENT
pygame.time.set_timer(Timer_for_rects, 1)
intro_rect_animation = []
#---------------------!!!CAUTION!!!This intro is pretty laggy, skip to Start_Game_import_grid to skip lag if wanted!--------------------
def game_intro_scene(): #This function makes the starting load up screen. It is meant to be 30 seconds, but if you move your mouse, it takes 5!
    global size_height
    global size_width    
    game_intro_scene_bool = True
    while game_intro_scene_bool == True:
        start_menu = True
        intthing = 0
        if pygame.event.get(pygame.QUIT): break
        for var in pygame.event.get():
            if var.type == Timer_for_rects: # this event happens every 1000 ms
                Width = random.sample(range(800), 100)
                Height = random.sample(range(800), 100)
                pygame.draw.rect(screen, (0,255,0), (Width[intthing], Height[intthing], size_height, size_width))
                intthing += 1
                if intthing == 15:
                    size_height += 1
                    size_width += 1
                    intthing = 0
                if size_height == 35:
                    screen.fill((0,255,0))
                    pygame.display.update()
                    Loadingbarscreen() 
                    break

        pygame.display.update()
def Loadingbarscreen(): #This is my loading bar, with changing colours! Not needed, but cool
    global Int_for_loading_bar 
    global this_thing 
    
    if this_thing == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if Int_for_loading_bar == 150:
                menu()
            elif Int_for_loading_bar != 150:
                pygame.draw.rect(screen, (255,255,255), (300, 350, 150, 35))
                pygame.draw.rect(screen, (200,Int_for_loading_bar,3), (300, 350, Int_for_loading_bar, 35))
                pygame.time.wait(10)
                pygame.display.update
                Int_for_loading_bar += 1
                pygame.display.update()



def menu(): #The menu screen! Basic and easy
    menu = True
    Start_game = Font.render('Start Game', False, (0, 0, 0))
    Credits = Font.render('Credits', False, (255, 255, 255))
    Tutorial = Font.render('Tutorial', False, (0, 0, 0))
    quit_game = Font.render('Quit', False, (255, 255, 255))
    while menu == True:
        playerclickX,playerclickY = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,255), (0, 0, 800, 200))
        pygame.draw.rect(screen, (0,0,0), (0, 200, 800, 200))
        pygame.draw.rect(screen, (255,255,255), (0, 400, 800, 200))
        pygame.draw.rect(screen, (0,0,0), (0, 600, 800, 200))
        screen.blit(Start_game,(250,75)), screen.blit(Credits,(295,275)), screen.blit(Tutorial,(290,475)), screen.blit(quit_game,(330,675))
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if 0 < playerclickX < 800 and 0 < playerclickY < 200:
                            menu = False
                        if 0 < playerclickX < 800 and 200 < playerclickY < 400:
                            Credits_Func()
                        if 0 < playerclickX < 800 and 400 < playerclickY < 600:
                            Tutorial_game()
                        if 0 < playerclickX < 800 and 600 < playerclickY < 800:
                            pygame.quit()
        pygame.display.update()
    else:
        Start_game_import_grid()
    
 
def Start_game_import_grid(): #Import grid from text file
    Import_Grid = ('Maps/Map_1.txt')
    with open(Import_Grid, 'r') as f:
        f_contents = f.read()
        map_1.extend(f_contents)
    load_image()
    start_game()

def load_image(): #Make the image using pillo.
    #My OOP is not great and I have 2 weeks left to finish this task as of the 25/8/2020.
    global pying
    loop_run = True
    numbY = 0
    numbX = 0
    if loop_run == True:
            for value in range (0,110):
                if numbX == 800:
                    numbY += 80
                    numbX = 0
                elif map_1[value] == '1':
                    img.paste(Image.open('images/grass.png'), (numbX, numbY))
                    tile_1.append([numbX, numbY, 80, 80])
                    numbX += 80
                elif map_1[value] == '2':
                    img.paste(Image.open('images/water.png'), (numbX, numbY))
                    tile_2.append([numbX, numbY, 80, 80])
                    numbX += 80
                elif map_1[value] == '3':
                    img.paste(Image.open('images/tree.png'), (numbX, numbY))
                    tile_3.append([numbX, numbY, 80, 80])
                    numbX += 80

            loop_run = False
            pying = pygame.image.fromstring(img.tobytes(), img.size, img.mode)  
            img.save("scene1.png")
def Credits_Func(): #Basic credits function, with a button!
    credit = True
    
    while credit == True:
        playerclickX,playerclickY = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        tutorial_window = pygame.image.load('Credits/Credit_img.png')
        screen.blit(tutorial_window, (0,0))
        pygame.draw.rect(screen, (255,255,255), (700,25,65,20))
        


        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if 700 < playerclickX < 765 and 25 < playerclickY < 45:
                            menu()
        pygame.display.update()

    return

def Tutorial_game(): #Tutorial for the game, kinda hard because of the lists and out of list errors.
    global what_tutorial_you_on
    Tutorial_loop = True
    while Tutorial_loop == True:
        if what_tutorial_you_on == 3:
            what_tutorial_you_on = 0
        if what_tutorial_you_on == -3:
            what_tutorial_you_on = 0
        playerclickX,playerclickY = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        tutorial_window = pygame.image.load(list_for_tutorial[what_tutorial_you_on])
        screen.blit(tutorial_window, (0,0))
        pygame.draw.rect(screen, (255,255,255), (20, 340,20,60))
        pygame.draw.rect(screen, (255,255,255), (760, 340,20,60))
        pygame.draw.rect(screen, (0,0,0), (700,25,65,20))
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if 700 < playerclickX < 765 and 25 < playerclickY < 45:
                            menu()
                        if 20 < playerclickX < 40 and 340 < playerclickY < 400:
                            what_tutorial_you_on -= 1
                        if 760 < playerclickX < 780 and 340 < playerclickY < 400:
                            what_tutorial_you_on += 1
        pygame.display.update()
    return
def start_game():
    #shhhh, WAYYY to many globals, but hard not to use them without OOP!
    global movement
    global pause
    global pying
    global enemy_bullet_shoot_x
    global enemy_bullet_shoot_y
    global player_bullet_shoot_x
    global player_bullet_shoot_y
    global imgnumb_1
    global imgnumb_2
    global speed_of_bullet
    global did_you_win_or_loose
    movement = True
    Player_Up = True
    Player_Down = True
    Player_Left = True
    Player_Right = True
    shoot_enemy_bullet = True
    #Variables
    player_x = 80
    player_y = 400
    enemy_x = 700
    enemy_y = 110
    escape_open = 0
    sprite_sheet_numb = 0
    Enemy_health = 0
    Player_health = 0
    while True:
        playerclickX,playerclickY = pygame.mouse.get_pos()
        left_sprite = pygame.image.load(what_sprite_list[imgnumb_1][0])
        right_sprite = pygame.image.load(what_sprite_list[imgnumb_1][1])
        back_sprite = pygame.image.load(what_sprite_list[imgnumb_1][2])
        forward_sprite = pygame.image.load(what_sprite_list[imgnumb_1][3])
        #Hit box for the main rectangle
        main_rect_hitbox = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y, 20, 44))
        #Hit box for the Top, and it's just basically a short line
        movement_hitbox_rect_X_UPPER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y - 5, 5, 1))#top
        #Hit box for the Bottom, and it's just basically a short line
        movement_hitbox_rect_X_LOWER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y + 48, 6, 1))#bottom
        #Hit box for the Right, and it's just basically a short line
        movement_hitbox_rect_RIGHT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 32, player_y + 5, 1,35))#right
        #Hit box for the Left, and it's just basically a short line
        movement_hitbox_rect_LEFT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y + 5, 1,35))#left side
        #Set the bool's to true, so they are not allways false
        Player_Up = True
        Player_Down = True
        Player_Left = True
        Player_Right = True
        for i in tile_2:
            #Tile 2, water, just changes the players velocity to make it seem like they are going through water
            if main_rect_hitbox.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Vel = Player_Vel // 3
        for i in tile_3:#collision stop movement
            #If the Top line colides with the third tile, then set the bool to false
            if movement_hitbox_rect_X_UPPER.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Up = False
            #If the Bottom line colides with the third tile, then set the bool to false
            if movement_hitbox_rect_X_LOWER.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Down = False
            #If the Right line colides with the third tile, then set the bool to false
            if movement_hitbox_rect_RIGHT_SIDE.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Right = False
            #If the Left line colides with the third tile, then set the bool to false
            if movement_hitbox_rect_LEFT_SIDE.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Left = False
            
        #If you click the close button in Pygame, it will exit out of the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #Keys
        keys = pygame.key.get_pressed()
        #Display image that we made before.
        screen.blit(pying, (0,0))
        #If movement == true will be useful for me as I 
        if imgnumb_1 == 0:
            speed_of_bullet = 10
            Player_Vel = 2
        elif imgnumb_1 == 1 or imgnumb_1 == -4:
            speed_of_bullet = 8
            Player_Vel = 4
        elif imgnumb_1 == 2 or imgnumb_1 == -3:
            speed_of_bullet = 6
            Player_Vel = 6
        if imgnumb_1 == 3 or imgnumb_1 == -2:
            speed_of_bullet = 4
            Player_Vel = 8
        if imgnumb_1 == 4 or imgnumb_1 ==-1:
            speed_of_bullet = 2
            Player_Vel = 10

        if movement == True and pause == False:   
            if Enemy_health == 50:
                did_you_win_or_loose = 0
                game_over_win()
                break
            elif Player_health == 20:
                did_you_win_or_loose = 1
                game_over_win()
                break
            else:
                enemy_player_thatmoves = pygame.draw.rect(screen, (255,0,0), (700, player_y, 50, 50))
                enemy_player_thatmoves_1 = pygame.draw.rect(screen, (0,0,0), (700, player_y, 50, Enemy_health))
                player_health_bar = pygame.draw.rect(screen, (0,0,0), (player_x + 9, player_y - 8, 22, 5))
                player_health_bar = pygame.draw.rect(screen, (255,0,0), (player_x + 9, player_y - 8, 22 - Player_health, 5))

                for enemy_bullet in enemy_bullets:
                        howmanyinlist = len(enemy_bullet)
                        howmanyinlist_2 = len(enemy_bullets)
                        if enemy_bullet_shoot_x > 0 and enemy_bullet_shoot_x < 800 and enemy_bullet_shoot_y > 0 and enemy_bullet_shoot_y < 800:
                            enemy_bullet[0] += 15*math.cos(enemy_bullet[2])
                            enemy_bullet[1] += 15*math.sin(enemy_bullet[2])
                            enemy_bullet_shoot_rect = pygame.draw.rect(screen, (0,0,0), (enemy_bullet[0], enemy_bullet[1], 5, 5))
                        if enemy_bullet[0] < 0 or enemy_bullet[0] > 800 or enemy_bullet[1] < 0 or enemy_bullet[1] > 800:
                            enemy_bullets.remove(enemy_bullet)
                        elif main_rect_hitbox.colliderect(pygame.draw.rect(screen, (0,0,0), (enemy_bullet_shoot_rect))):
                            enemy_bullets.remove(enemy_bullet)
                            Player_health += 2
                for player_bullet in player_bullets:
                        if player_bullet_shoot_x >= -50 and player_bullet_shoot_x <= 850 and player_bullet_shoot_y >= -50 and player_bullet_shoot_y <= 850:
                            player_bullet[0] += speed_of_bullet*math.cos(player_bullet[2])
                            player_bullet[1] += speed_of_bullet*math.sin(player_bullet[2])
                            player_bullet_shoot_rect = pygame.draw.rect(screen, (0,0,0), (player_bullet[0] + 20, player_bullet[1] - 10, 5, 5))
                        if player_bullet[0] <= 0 or player_bullet[0] >= 800 or player_bullet[1] <= 0 or player_bullet[1] >= 800:
                            player_bullets.remove(player_bullet)
                        if player_bullet_shoot_rect.colliderect(enemy_player_thatmoves) or player_bullet_shoot_rect.colliderect(enemy_player_thatmoves_1): 
                            player_bullets.remove(player_bullet)
                            Enemy_health += 1
                #If movement is true, E.G When it's not looking at inventory then run the following
                if event.type == move_down_event:
                    enemy_bullet_shoot_y = player_y
                    enemy_bullet_shoot_x = 700
                    enemy_bullets.append([enemy_bullet_shoot_x, enemy_bullet_shoot_y + 25, math.atan2(player_y - enemy_bullet_shoot_y, player_x - enemy_bullet_shoot_x)])
                if event.type == MOUSEBUTTONDOWN:
                    player_bullet_shoot_y = player_y
                    player_bullet_shoot_x = player_x
                    player_bullets.append([player_bullet_shoot_x, player_bullet_shoot_y + 25, math.atan2(playerclickY - player_bullet_shoot_y, playerclickX - player_bullet_shoot_x)])

                elif keys[pygame.K_w] and keys[pygame.K_d] or keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                    #If the key W and D are pressed, then print the following
                    screen.blit(forward_sprite, (player_x, player_y))
                    #Print's the image even if you're not moving, so it can display something
                    if Player_Up == True and Player_Right == True:
                        #If the events above are true, then change the velocity of the char
                        player_y -= Player_Vel
                        player_x += Player_Vel
                elif keys[pygame.K_w] and keys[pygame.K_a] or keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                    screen.blit(forward_sprite, (player_x, player_y))
                    if Player_Up == True and Player_Left == True:
                        player_y -= Player_Vel
                        player_x -= Player_Vel
                elif keys[pygame.K_s] and keys[pygame.K_d] or keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    screen.blit(back_sprite, (player_x, player_y))
                    if Player_Down == True and Player_Right == True:
                        player_y += Player_Vel
                        player_x += Player_Vel
                        
                elif keys[pygame.K_s] and keys[pygame.K_a] or keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                    screen.blit(back_sprite, (player_x, player_y))
                    if Player_Down == True and Player_Left == True:
                        player_y += Player_Vel
                        player_x -= Player_Vel
                        
                #Movement for basic key presses such as A or W. I have made it so that it also can detect movement
                #from the arrow keys. Cool little feature for user benefit. 
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    screen.blit(forward_sprite, (player_x, player_y))
                    if Player_Up == True:
                        player_y -= Player_Vel
                        
                elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    screen.blit(left_sprite, (player_x, player_y))
                    if Player_Left == True:
                        player_x -= Player_Vel
                        
                elif keys[pygame.K_DOWN]or keys[pygame.K_s]:
                    screen.blit(back_sprite, (player_x, player_y))
                    if Player_Down == True:
                        player_y += Player_Vel
                        
                elif keys[pygame.K_RIGHT]or keys[pygame.K_d]:
                    screen.blit(right_sprite, (player_x, player_y)) 
                    if Player_Right == True:
                        player_x += Player_Vel
                        
                elif keys[pygame.K_e]:
                    pause = True
                        
            while pause == True:
                screen.blit(back_sprite, (player_x, player_y))
                playerclickX,playerclickY = pygame.mouse.get_pos()
                #main draw rect
                pygame.draw.rect(screen, (255,255,255), (225, 100, 350, 450))
                #Left movement rect
                pygame.draw.rect(screen, (0,0,0), (250, 275, 20, 60), 1)
                #Right movement rect
                pygame.draw.rect(screen, (0,0,0), (525, 275, 20, 60), 1)
                #Exit movement rect
                pygame.draw.rect(screen, (0,0,0), (475, 125, 80, 30))
                backgroundfile = pygame.image.load(what_sprite_list[imgnumb_1][imgnumb_2])
                background_file_2 = pygame.image.load(list_for_bulletspeed[imgnumb_1])
                screen.blit(backgroundfile, (300,225))
                screen.blit(background_file_2, (250,475))
                pygame.display.update()
                movement = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if imgnumb_1 == -5:
                            imgnumb_1 = 0
                        elif imgnumb_1 == 4:
                            imgnumb_1 = -1
                            #Move Left
                        if 250 < playerclickX < 270:
                            if 275 < playerclickY < 335:
                                imgnumb_1 -= 1
                            #Move Right
                        if 525 < playerclickX < 545:
                            if 275 < playerclickY < 335:
                                imgnumb_1 += 1
                            #Exit
                        if 475 < playerclickX < 555:
                            if 125 < playerclickY < 155:
                                pause = False
                                movement = True
            else:
                movement = True
                pause = False
                screen.blit(back_sprite, (player_x, player_y))
            pygame.display.update()

def game_over_win():
    global did_you_win_or_loose
    game_over_win = True
    while game_over_win == True:
        playerclickX,playerclickY = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        game_win = pygame.image.load(game_win_or_loss[did_you_win_or_loose])
        screen.blit(game_win, (0,0))
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if 150 < playerclickX < 280 and 540 < playerclickY < 610:
                            menu()
                        if 510 < playerclickX < 630 and 540 < playerclickY < 610:
                            pygame.quit()
        pygame.display.update()
    return

#Start game!
game_intro_scene()

#Total Lines: 485
#Total comments: 71