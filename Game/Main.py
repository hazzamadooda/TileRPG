#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#import all the the neccesary moduels. 
import pygame
from PIL import Image, ImageDraw
import time
#Grid from test.txt
grid = []
#Tile_1
tile_1 = []
#Tile_2
tile_2 = []
#Tile_3
tile_3 = []
#Weapons
movement = True

#SpriteLists
sprite_list_1 = ['Sprites_1/Left_1.png', 'Sprites_1/Right_1.png', 'Sprites_1/Forward_1.png', 'Sprites_1/Back_1.png']
sprite_list_2 = ['Sprites_1/Left_2.png', 'Sprites_1/Right_2.png', 'Sprites_1/Forward_2.png', 'Sprites_1/Back_2.png']
sprite_list_3 = ['Sprites_1/Left_3.png', 'Sprites_1/Right_3.png', 'Sprites_1/Forward_3.png', 'Sprites_1/Back_3.png']
sprite_list_4 = ['Sprites_1/Left_4.png', 'Sprites_1/Right_4.png', 'Sprites_1/Forward_4.png', 'Sprites_1/Back_4.png']
sprite_list_5 = ['Sprites_1/Left_5.png', 'Sprites_1/Right_5.png', 'Sprites_1/Forward_5.png', 'Sprites_1/Back_5.png']


what_sprite_list = [sprite_list_1, sprite_list_2, sprite_list_3, sprite_list_4, sprite_list_5]
#Pygame neccesary's 
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
#For pillow
img = Image.new('RGB', (800,800), color = (0,0,0))
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

        

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
def Start_game_import_grid():
    with open('test.txt', 'r') as f:
        f_contents = f.read()
        grid.extend(f_contents)
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
                elif grid[value] == '1':
                    img.paste(Image.open('images/grass.png'), (numbX, numbY))
                    tile_1.append([numbX, numbY, 80, 80])
                    numbX += 80
                elif grid[value] == '2':
                    img.paste(Image.open('images/water.png'), (numbX, numbY))
                    tile_2.append([numbX, numbY, 80, 80])
                    numbX += 80
                elif grid[value] == '3':
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
    movement = True
    Player_Up = True
    Player_Down = True
    Player_Left = True
    Player_Right = True
    pause = False
    #Lists:

    Player_Vel = 5
    player_x = 80
    player_y = 110
    escape_open = 0

    #sprites
    #images
    left_sprite = pygame.image.load(what_sprite_list[0][0])
    right_sprite = pygame.image.load(what_sprite_list[0][1])
    back_sprite = pygame.image.load(what_sprite_list[0][2])
    forward_sprite = pygame.image.load(what_sprite_list[0][3])
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
    while True:
        #Hit box for the main rectangle
        
        #Hit box for the Top, and it's just basically a short line
        movement_hitbox_rect_X_UPPER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y, 5, 1))#top
        #Hit box for the Bottom, and it's just basically a short line
        movement_hitbox_rect_X_LOWER = pygame.draw.rect(screen, (0,0,0), (player_x + 18, player_y + 48, 6, 1))#bottom
        #Hit box for the Right, and it's just basically a short line
        movement_hitbox_rect_RIGHT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 32, player_y + 11, 1, 20))#right
        #Hit box for the Left, and it's just basically a short line
        movement_hitbox_rect_LEFT_SIDE = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y + 11, 1, 20))#left side
        #Set the bool's to true, so they are not allways false
        main_rect_hitbox = pygame.draw.rect(screen, (0,0,0), (player_x + 10, player_y, 20, 44))
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
        if movement == True:       
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
            else:
                movement = True
                screen.blit(back_sprite, (player_x, player_y))
        #functions
        #check colision function
        
        pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------            
#Basically the main run function, it opens the text file and imports all of the neccesary data!
Start_game_import_grid()