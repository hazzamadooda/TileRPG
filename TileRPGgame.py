import sys
import pygame as pg
import time

#Start date: Wednesday 29th / 7 / 2020
#First things to implement:
#Have to draw out the map and illustrate boxes.
#yeah that's all for now.


width, height = 1440, 880
hboundaries, vboundaries = 20, 20
red = (255,0,0)
green = (50,205,50)
white = (255,255,255)
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
#pos where it starts
rect = pg.Rect(300, 220, hboundaries, vboundaries)
velocity = (0, 0)
game_1_stock_1 = str(rect.x),(rect.y)
Travelers_lounge_background = pg.image.load("Image.png")
boundaries = []


#classes
class boundary:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color




def textBoxBlack(text, size, position, color):
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color, (255,0,0))
    textRect = text.get_rect()
    textRect.center = position
    screen.blit(text, textRect)




def main():
    global boundary_colour
    myfont=pg.font.SysFont("freesansbold.ttf", 20)
    done = False
    colour = False
    boundary_colour = red

    #boundaries_tile
    boundaries.append(boundary((0,0),(1440,55),red))
    boundaries.append(boundary((0,825),(1440,55),red))
    boundaries.append(boundary((585,300),(40,250),red))
    boundaries.append(boundary((813,300),(40,250),red))






    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        keys = pg.key.get_pressed()

        # booster
        move = 18 if keys[pg.K_LSHIFT] else 4


        if keys[pg.K_a]:  #to move left
            collide = False
            for b in boundaries:
                testRect = rect.copy()
                testRect.x -= move
                if testRect.colliderect((b.position, b.size)):
                    collide = True
                    break
            if collide == False:
                rect.x -= move
        
        if keys[pg.K_d]: #to move right
            collide = False
            for b in boundaries:
                testRect = rect.copy()
                testRect.x += move
                if testRect.colliderect((b.position, b.size)):
                    collide = True
                    break
            if collide == False:
                rect.x += move


        

        if keys[pg.K_w]:  #to move up
            collide = False
            for b in boundaries:
                testRect = rect.copy()
                testRect.y -= move
                if testRect.colliderect((b.position, b.size)):
                    collide = True
                    break
            if collide == False:
                rect.y -= move

        if keys[pg.K_s]: #to move down
            collide = False
            for b in boundaries:
                testRect = rect.copy()
                testRect.y += move
                if testRect.colliderect((b.position, b.size)):
                    collide = True
                    break
            if collide == False:
                rect.y += move
        


        #boundary:
        #1
        if rect.y < 15: 
            rect.y = 15
        #2
        if rect.x > 1440:
            rect.x = 0
        #3
        if rect.x < 0:
            rect.x = 1440

        if rect.x > 850 and rect.x < 855 and rect.y > 350 and rect.y < 480:
            rect.x = 550
            rect.y = rect.y
        if rect.x > 580 and rect.x < 590 and rect.y > 350 and rect.y < 480:
            rect.x = 860
            rect.y = rect.y
        #4
        if rect.y > height - hboundaries:
            rect.y = height - vboundaries

        
        
        screen.fill((0, 0, 0))
        screen.blit(Travelers_lounge_background, (0, 0))
        ## draw all boundaries
        for b in boundaries:
            pg.draw.rect(screen, b.color, ((b.position),(b.size)))
        pg.display.update()
        pg.draw.rect(screen, (boundary_colour), rect)


        pg.display.flip()
        clock.tick(30)
        


if __name__ == '__main__':

    pg.init()
    main()
    pg.quit()
    sys.exit()
