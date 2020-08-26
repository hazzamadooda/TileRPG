#import all the the neccesary moduels. 
import pygame
from PIL import Image, ImageDraw
#Grid from test.txt
grid = []
#Tile_1
tile_1 = []
#Tile_2
tile_2 = []
#Tile_3
tile_3 = []
#variables
#Pygame neccesary's 
width, height = 880, 880
screen = pygame.display.set_mode((width, height))
#For pillow
img = Image.new('RGB', (880,880), color = (0,0,0))

def Start_game_import_grid():
    with open('test.txt', 'r') as f:
        f_contents = f.read()
        grid.extend(f_contents)
    load_image()
    start_game()

def load_image():
    #:( globals. My OOP is not great and I have 2 weeks left to finish this task as of the 25/8/2020.
    #If I get time, i'll fix it up, for now however globals will have to do!
    global img
    global grid
    global pying
    loop_run = True
    numbY = 0
    numbX = 0
    water_image =pygame.image.load('images/water.png')
    tree_image = pygame.image.load('images/tree.png')
    grass_image = pygame.image.load('images/grass.png')
    if loop_run == True:
            for value in range (0,110):
                if numbX == 880:
                    numbY += 88
                    numbX = 0
                elif grid[value] == '1':
                    img.paste(Image.open('images/grass.png'), (numbX, numbY))
                    tile_1.append([numbX, numbY, 88, 88])
                    numbX += 88
                elif grid[value] == '2':
                    img.paste(Image.open('images/water.png'), (numbX, numbY))
                    tile_2.append([numbX, numbY, 88, 88])
                    numbX += 88
                elif grid[value] == '3':
                    img.paste(Image.open('images/tree.png'), (numbX, numbY))
                    tile_3.append([numbX, numbY, 88, 88])
                    numbX += 88
                else:
                    value += 1
            loop_run = False
            pying = pygame.image.fromstring(img.tobytes(), img.size, img.mode)   

def start_game():
    global pying
    global grid
    movement = True

    vel = 5
    x = 88
    y = 110
    #sprites
    
    left_sprite = pygame.image.load('Sprites_1/Left.png')
    right_sprite = pygame.image.load('Sprites_1/Right.png')
    back_sprite = pygame.image.load('Sprites_1/Forward.png')
    forward_sprite = pygame.image.load('Sprites_1/Back.png')
    
    while True:
        movement_hitbox_rect = pygame.draw.rect(screen, (0,255,0), (x + 10, y, 22, 44))
        for i in tile_1:
            if movement_hitbox_rect.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                vel = 5
        for i in tile_2:
            if movement_hitbox_rect.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                vel = 2
        for i in tile_3:
            if movement_hitbox_rect.colliderect(pygame.draw.rect(screen, (255,255,255), (i))):
                print(i)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #Keys
        keys = pygame.key.get_pressed()
        #Display image that we made before.
        screen.blit(pying, (0,0))
        #If movement == true will be useful for me as I 
        
        if movement == True:
            if keys[pygame.K_w] and keys[pygame.K_d] or keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                y -= vel
                x += vel
                screen.blit(forward_sprite, (x, y))
            elif keys[pygame.K_w] and keys[pygame.K_a] or keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                y -= vel
                x -= vel
                screen.blit(forward_sprite, (x, y))
            elif keys[pygame.K_s] and keys[pygame.K_d] or keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                y += vel
                x += vel
                screen.blit(back_sprite, (x, y))
            elif keys[pygame.K_s] and keys[pygame.K_a] or keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                y += vel
                x -= vel
                screen.blit(back_sprite, (x, y))
            
            #Movement for basic key presses such as A or W. I have made it so that it also can detect movement
            #from the arrow keys. Cool little feature for user benefit. 
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                y -= vel
                screen.blit(forward_sprite, (x, y))
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                x -= vel
                screen.blit(left_sprite, (x, y))
            elif keys[pygame.K_DOWN]or keys[pygame.K_s]:
                y += vel
                screen.blit(back_sprite, (x, y))
            elif keys[pygame.K_RIGHT]or keys[pygame.K_d]:
                x += vel
                screen.blit(right_sprite, (x, y)) 
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                x -= vel
                screen.blit(left_sprite, (x, y))
            elif keys[pygame.K_DOWN]or keys[pygame.K_s]:
                y += vel
                screen.blit(back_sprite, (x, y))
            elif keys[pygame.K_RIGHT]or keys[pygame.K_d]:
                x += vel
                screen.blit(right_sprite, (x, y))
            elif keys[pygame.K_LSHIFT]:
                vel = 10
                screen.blit(back_sprite, (x, y))

            else:
                screen.blit(back_sprite, (x, y))
                vel = 5
            #functions
            #check colision function
            pygame.display.update()
            
#Basically the main run function, it opens the text file and imports all of the neccesary data! Yippee 
Start_game_import_grid()
                
