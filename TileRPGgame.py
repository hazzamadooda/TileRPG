import sys
import pygame as pg


width, height = 1440, 880
hbox, vbox = 20, 20
red = (255,0,0)
green = (50,205,50)
white = (255,255,255)
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
rect = pg.Rect(300, 220, hbox, vbox)
velocity = (0, 0)
game_1_stock_1 = str(rect.x),(rect.y)
Travelers_lounge_background = pg.image.load("Image.png")



def textBoxBlack(text, size, position, color):
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color, (255,0,0))
    textRect = text.get_rect()
    textRect.center = position
    screen.blit(text, textRect)

def draw_the_map():
    pg.draw.rect(screen,red,(0,0,1440,15))


def main():
    global box_colour
    myfont=pg.font.SysFont("freesansbold.ttf", 20)
    done = False
    colour = False
    box_colour = red


    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        keys = pg.key.get_pressed()

        # booster
        move = 18 if keys[pg.K_LSHIFT] else 4


        if keys[pg.K_a]:  #to move left
            rect.x -= move
        if rect.x < 0:
            rect.x = 0
        if keys[pg.K_d]: #to move right
            rect.x += move

        if rect.x > width-hbox:
            rect.x = width - hbox
        if rect.x > 0 and rect.y > -5 and rect.x < 1440 and rect.y < 15:
            colour = True
        else:
            colour = False

        if keys[pg.K_w]:  #to move up
            rect.y -= move
        if rect.y < 0: rect.y = 0

        if keys[pg.K_s]: #to move down
            rect.y += move
        if rect.y > height - hbox:
            rect.y = height - vbox



        if colour == True:
            box_colour = green
        if colour == False:
            box_colour = red

        screen.fill((0, 0, 0))
        screen.blit(Travelers_lounge_background, (0, 0))
        draw_the_map()
        pg.display.update()
        pg.draw.rect(screen, (box_colour), rect)
        pg.draw.rect(screen, (box_colour), rect)


        pg.display.flip()
        clock.tick(30)
        


if __name__ == '__main__':

    pg.init()
    main()
    pg.quit()
    sys.exit()
