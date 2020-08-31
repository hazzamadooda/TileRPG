#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#import all the the neccesary moduels. 
import pygame
from PIL import Image, ImageDraw
import time
from pygame.locals import *
#Grid from test.txt
map_1 = []
#Tile_1
tile_1 = []
#Tile_2
tile_2 = []
#Tile_3
tile_3 = []

pause_true_or_false = 1
imgnumb_1 = 0
imgnumb_2 = 4
#Weapons
movement = True

pause = False

#SpriteLists
sprite_list_1 = (['Sprites_1/Left_1.png', 'Sprites_1/Right_1.png', 'Sprites_1/Forward_1.png', 'Sprites_1/Back_1.png', 'Sprites_1/display_IMG_1.png'])
sprite_list_2 = (['Sprites_1/Left_2.png', 'Sprites_1/Right_2.png', 'Sprites_1/Forward_2.png', 'Sprites_1/Back_2.png', 'Sprites_1/display_IMG_2.png'])
sprite_list_3 = (['Sprites_1/Left_3.png', 'Sprites_1/Right_3.png', 'Sprites_1/Forward_3.png', 'Sprites_1/Back_3.png', 'Sprites_1/display_IMG_3.png'])
sprite_list_4 = (['Sprites_1/Left_4.png', 'Sprites_1/Right_4.png', 'Sprites_1/Forward_4.png', 'Sprites_1/Back_4.png', 'Sprites_1/display_IMG_4.png'])
sprite_list_5 = (['Sprites_1/Left_5.png', 'Sprites_1/Right_5.png', 'Sprites_1/Forward_5.png', 'Sprites_1/Back_5.png', 'Sprites_1/display_IMG_5.png'])


what_sprite_list = [sprite_list_1, sprite_list_2, sprite_list_3, sprite_list_4, sprite_list_5]
#Pygame neccesary's 
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
#For pillow
img = Image.new('RGB', (800,800), color = (0,0,0))
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def pause_game():
    global movement
    global pause
    global imgnumb_1
    global imgnumb_2
    pause_true_or_false=False

    while pause:
        playerclickX, playerclickY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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

            #main draw rect
            pygame.draw.rect(screen, (255,255,255), (225, 100, 350, 450))
            #Left movement rect
            pygame.draw.rect(screen, (0,0,0), (250, 275, 20, 60))
            #Right movement rect
            pygame.draw.rect(screen, (0,0,0), (525, 275, 20, 60))
            #Exit movement rect
            pygame.draw.rect(screen, (0,0,0), (475, 125, 80, 30))
            backgroundfile = pygame.image.load(what_sprite_list[imgnumb_1][imgnumb_2])
            screen.blit(backgroundfile, (300,225))
        pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def Start_game_import_grid():
    with open('Maps/Map_1.txt', 'r') as f:
        f_contents = f.read()
        map_1.extend(f_contents)
    load_image()
    start_game()
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def load_image():
    #:( globals. My OOP is not great and I have 2 weeks left to finish this task as of the 25/8/2020.
    #If I get time, i'll fix it up, for now however globals will have to do!
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
                
                else:
                    value += 1
            loop_run = False
            pying = pygame.image.fromstring(img.tobytes(), img.size, img.mode)  
            img.save("scene1.png")
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def start_game():
    #bools
    global movement
    global pause
    global pause_true_or_false
    movement = True
    Player_Up = True
    Player_Down = True
    Player_Left = True
    Player_Right = True
    MOUSEBUTTONDOWN = True
    #Lists:
    

    Player_Vel = 5
    player_x = 80
    player_y = 110
    escape_open = 0
    sprite_sheet_numb = 0
    #sprites
    #images

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
    while True:
        left_sprite = pygame.image.load(what_sprite_list[sprite_sheet_numb][0])
        right_sprite = pygame.image.load(what_sprite_list[sprite_sheet_numb][1])
        back_sprite = pygame.image.load(what_sprite_list[sprite_sheet_numb][2])
        forward_sprite = pygame.image.load(what_sprite_list[sprite_sheet_numb][3])
        player_x_click,player_y_click = pygame.mouse.get_pos()
        #Hit box for the main rectangle
        main_rect_hitbox = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y, 20, 44))
        #Hit box for the Top, and it's just basically a short line
        movement_hitbox_rect_X_UPPER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y, 5, 1))#top
        #Hit box for the Bottom, and it's just basically a short line
        movement_hitbox_rect_X_LOWER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y + 48, 6, 1))#bottom
        #Hit box for the Right, and it's just basically a short line
        movement_hitbox_rect_RIGHT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 32, player_y + 11, 1, 20))#right
        #Hit box for the Left, and it's just basically a short line
        movement_hitbox_rect_LEFT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y + 11, 1, 20))#left side
        #Set the bool's to true, so they are not allways false
        Player_Up = True
        Player_Down = True
        Player_Left = True
        Player_Right = True
        for i in tile_1:
            #Tile one, gets the data from the rectangle above and the rectangles from the list Grid
            if main_rect_hitbox.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                #If the collision is true then: Make the player velocity 5
                Player_Vel = 5
                
                
        for i in tile_2:
            #Tile 2, water, just changes the players velocity to make it seem like they are going through water
            if main_rect_hitbox.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                Player_Vel = 2
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
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------                  
        if movement == True and pause == False:      
            #If movement is true, E.G When it's not looking at inventory then run the following
            


            if keys[pygame.K_w] and keys[pygame.K_d] or keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
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
                    
            elif keys[pygame.K_p]:
                movement = False
                pause = True
                
            elif player_x < -35:
                player_x = -40
            elif player_x > 790:
                player_x = 800
            elif player_y < -45:
                player_y = -45
            elif player_y > 790:
                player_y = 800
                
                
            

            else:
                MOUSEBUTTONDOWN = False
                movement = True
                screen.blit(back_sprite, (player_x, player_y))
            pause_game()
        #functions
        #check colision function
        
        pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------            
#Basically the main run function, it opens the text file and imports all of the neccesary data!
Start_game_import_grid()