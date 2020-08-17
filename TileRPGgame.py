import pygame
from collections import Counter
import time
grid = []
water = []
drawing_box_variable = 0
blue = (255,255,8)
red = (0,50,255)
width, height = 1440, 880
screen = pygame.display.set_mode((width, height))
keys = pygame.key.get_pressed()
done = False
clock = pygame.time.Clock()


#classes
class boundary:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color


def import_grid_1():
    with open('test.txt', 'r') as f:
        f_contents = f.read()
        grid.extend(f_contents)

def start_game():
    global grid
    initialRunner = True
    numbY = 0
    numbX = 0
    screen.fill((0, 0, 0))
    pygame.display.update()
    
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        if initialRunner == True:
            for value in range (0,110):
                if value == 109:
                    value = 0
                            
                else:
                    if grid[value] == '1':
                        pygame.draw.rect(screen,blue,(numbX,numbY,144,88))
                        numbX += 144
                    if numbX == 1440:
                        numbY += 88
                        numbX = 0

                    elif grid[value] == '2':
                        pygame.draw.rect(screen,red,(numbX,numbY,144,88))
                        numbX += 144
                        if numbX == 1440:
                            numbY += 88
                            numbX = 0
                            print(numbX)
                    else:
                        print('space')
                    value += 1
            initialRunner = False
                
            
        pygame.display.update()
            

            
            
            
    


def start_game_functions():
        pygame.init()
        import_grid_1()
        start_game()

        
    
start_game_functions()

#ideas: so find 1 line for the Y, then get the width of the screen and divide it by 10 to get each box space. From there we can
#like get a variable that adds the number for above each time that it is used I think. So like:
#The first one would be 50(pixels), then it would add 50 to the variable and do it again, so it would be like 100 the next time.
#Then it would keep on going until it reached the end of the list. 
