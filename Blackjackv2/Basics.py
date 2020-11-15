import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((1200,600))
font_1 = pygame.font.Font('Niceyear-mLZ59.ttf', 25)
card_deck = []
computer_card_deck = []
player_card_deck = []

player_bet = 6969
player_balance = 0

decksize = 1

num_of_computer_card = 1
num_of_player_card = 2

computer_card_value = 0
player_card_value = 0

rand_test = 0


suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
run = True
run2 = True
stand = True
blackjack_loaded = False
math_update = False

class IntroScreen():
    
    def __init__(self, image):
        self.image = image
        self.b = 255
        self.i = 0

    def run(self):
        global run
        if run == True:
            self.run_click()
            if self.i < 255:
                self.b -= 1
                self.i += 1
            else:
                return True
            self.image.set_alpha(self.i)
            screen.blit(self.image,(0,0))
            rect_1 = pygame.Surface((100,50))
            rect_2 = pygame.Surface((97,47))
            rect_1.set_alpha(self.i), rect_2.set_alpha(self.i)                
            rect_1.fill((self.i,self.i,self.i))
            rect_2.fill((self.i,self.i,self.i))           
            screen.blit(rect_1, (200,250)), screen.blit(rect_2, (902,252))
            start_text = font_1.render('Start', True, (self.b,self.b,self.b))
            help_text = font_1.render('Help', True, (self.b,self.b,self.b)) 
            screen.blit(start_text, (228,263)), screen.blit(help_text, (929,263))
            self.run_click()
        else:
            start = Main_Game()
            

        
    def run_click(self):
        global run
        x,y = pygame.mouse.get_pos()
        if x >= 200 and x <= 300 and y >= 250 and y <= 300:
            Rectangles((255,0,0), 200, 250, 100, 50)
        else:
            Rectangles((0,0,0), 200, 250, 100, 50)
        if x >= 900 and x <= 1000 and y >= 250 and y <= 300:
            Rectangles((255,0,0), 900, 250, 100, 50)
        else:
            Rectangles((0,0,0), 900, 250, 100, 50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x >= 200 and x <= 300 and y >= 250 and y <= 300:
                    run = False

                if x >= 900 and x <= 1000 and y >= 250 and y <= 300:
                    return
                    

class on_hover_buttons():
    #Saves so many lines
    def __init__(self, xpos, ypos, xrect, yrect, width, height, colour1, colour2):
        x,y = pygame.mouse.get_pos()
        self.xpos = xpos
        self.ypos = ypos
        self.xrect = xrect
        self.yrect = yrect
        self.width = width
        self.height = height
        self.colour1 = colour1
        self.colour2 = colour2
        self.colour3 = 0
        
        if x >= self.xpos and x <= (self.xpos + self.width) and y >= self.ypos and y <= (self.ypos + self.height):
            Rectangles((self.colour1,self.colour2,self.colour3), self.xrect, self.yrect, self.width, self.height)
        else:
            Rectangles((0,0,0), self.xrect, self.yrect, self.width, self.height)






class Rectangles():
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height), 3)


class Print_Text():
    def __init__(self, information, xpos, ypos, colour):
        self.information = information
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        print_text = font_1.render(str(self.information), 1, (self.colour,self.colour,self.colour))
        screen.blit(print_text, (xpos, ypos))


class Deck():
    def __init__(self):
        self.deck = []
        self.create_deck()
    def create_deck(self):
        for deck_size in range(0, decksize):
            for suit in suits:
                for i in range(13):
                    card1 = Card(suit,values[i],faces[i])
                    self.deck.append(card1)   


class Card():
    def __init__(self,suit,values,face):    
        self.suit = suit
        self.values = values
        self.face = face

deck = Deck()
for x in deck.deck:
    card_deck.append((str(x.face), str(x.suit), str(x.values)))
random.shuffle(card_deck)

class Generate_cards():

    def __init__(self):
        for i in range(0,5):
            randnumb = random.randint(0,len(card_deck) - 1)
            computer_card_deck.append(card_deck[randnumb])
            card_deck.remove(card_deck[randnumb])
        for i in range(0,5):
            randnumb = random.randint(0,len(card_deck) - 1)
            player_card_deck.append(card_deck[randnumb])
            card_deck.remove(card_deck[randnumb])

start = Generate_cards()

class blackjack():
    def __init__(self):
        global blackjack_loaded
        global math_update
        global num_of_computer_card
        global player_card_value
        global computer_card_value
        global num_of_player_card
        global run2
        x,y = pygame.mouse.get_pos()
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(0,0,0), (0, 300, 1200, 1),1)   

        if blackjack_loaded == False:
            for i in range(0, num_of_player_card): #Displays the player cards
                if player_card_deck[i][1] == "Diamonds" or player_card_deck[i][1] == "Hearts":
                    pygame.draw.rect(screen, (255,0,0), (10 + (180*i), 358, 140, 230))
                else:
                    pygame.draw.rect(screen, (90,90,90), (10 + (180*i), 358, 140, 230))
                Print_Text((player_card_deck[i][0]), 15 + 180*i, 358, (0)), Print_Text((player_card_deck[i][1]), 15 + 180*i, 380, (0)), Print_Text((player_card_deck[i][2]), (20 + 180*i) - i*2, 553, (0))
                pygame.draw.rect(screen, (0,0,0), (10 + (180 * i), 357, 140, 230), 5)
            for i in range(0, num_of_computer_card): #Displays the computer cards
                if computer_card_deck[i][1] == "Diamonds" or computer_card_deck[i][1] == "Hearts":
                    pygame.draw.rect(screen, (255,0,0), (10 + (180 * i), 13, 140, 230))
                else:
                    pygame.draw.rect(screen, (90,90,90), (10 + (180 * i), 13, 140, 230))
                Print_Text((computer_card_deck[i][0]), 15 + 180*i, 13, (0)), Print_Text((computer_card_deck[i][1]), 15 + 180*i, 35, (0)), Print_Text((computer_card_deck[i][2]), (20 + 180*i) - i*2, 208, (0))
                pygame.draw.rect(screen, (0,0,0), (10 + 180*i, 12, 140, 230), 5)
                pygame.time.get_ticks()
            if math_update == False:
                self.math_computer()
                math_update = True
            Print_Text(("Computer card total " + str(computer_card_value)), 15, 260, (0))
            Print_Text(("Player card total  " + str(player_card_value)), 15, 310, (0))
            on_hover_buttons(1025, 50, 1025, 50, 150, 50, 0, 255) #Bal
            on_hover_buttons(1025, 125, 1025, 125, 150, 50, 255, 0) #Bet
            Print_Text(("    STAND"), 1035, 64, (0))
            Print_Text(("       HIT"), 1035, 139, (0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x >= 1025 and x <= 1175 and y >= 50 and y <= 100: #Stand
                        while computer_card_value != 21 and computer_card_value <= 21:
                            num_of_computer_card += 1
                            self.math_computer()
                        run2 = True
                        self.clean_up_function()

                        
                    if x >= 1025 and x <= 1175 and y >= 125 and y <= 175: #Hit
                        if player_card_value <= 21:
                            num_of_player_card += 1
                            self.math_computer()
        pygame.display.update()
    
    def math_computer(self):
        global computer_card_value
        global player_card_value
        player_card_value = 0
        computer_card_value = 0
        for i in range(0, num_of_computer_card):
            computer_card_value += int(computer_card_deck[i][2])
        for i in range(0, num_of_player_card):
            player_card_value += int(player_card_deck[i][2])

    def clean_up_function(self):
        global num_of_computer_card
        global num_of_player_card
        global computer_card_value
        global player_card_value
        global math_update
        math_update = False
        num_of_computer_card = 1
        num_of_player_card = 2
        computer_card_value = 0
        player_card_value = 0
        computer_card_deck.clear()
        player_card_deck.clear()
        start = Generate_cards()
        run = Main_Game()
        return


        










        
class Main_Game():
    def __init__(self):
        self.side_bar()
        self.i = 250


        
    def side_bar(self):
        global player_balance
        global player_bet
        global run2
        x,y = pygame.mouse.get_pos()  
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(0,0,0), (0, 300, 1200, 1),1)  
        if run2 == True:
            if x >= 1000 and x <= 1200 and y >= 0 and y <= 700:
                pygame.draw.rect(screen, (150,150,150), (1000, 0, 200, 700))
                #####sidebar | betting
                on_hover_buttons(1025, 50, 1025, 50, 150, 50, 0, 255) #Bal
                on_hover_buttons(1025, 125, 1025, 125, 150, 50, 255, 0) #DBet
                on_hover_buttons(1025, 205, 1025, 205, 70, 50, 0, 255) # + $100
                on_hover_buttons(1110, 205, 1110, 205, 70, 50, 255, 0) # - $100
                on_hover_buttons(1025, 275, 1025, 275, 70, 50, 0, 255) # Up
                on_hover_buttons(1110, 275, 1110, 275, 70, 50, 255, 0) # Down
                on_hover_buttons(1025, 345, 1025, 345, 70, 50, 0, 255) # + $50
                on_hover_buttons(1110, 345, 1110, 345, 70, 50, 255, 0) # - $50
                on_hover_buttons(1025, 500, 1025, 500, 150, 50, 255, 255) #Deal

                Print_Text(("---- BETTING ----"), 1035, 15, (0))
                Print_Text(("BAL $"), 1035, 64, (0))
                Print_Text(("BET $"), 1035, 139, (0))
                Print_Text(("+ 100"), 1030, 218, (0))
                Print_Text(("+ 50"), 1116, 218, (0))
                Print_Text(("- 100"), 1030, 358, (0))
                Print_Text(("- 50"), 1116, 358, (0))
                Print_Text(("---- DEAL ----"), 1050, 512, (0))
                
                
                Print_Text((player_balance), 1100, 64, (0))
                Print_Text((player_bet), 1100, 139, (0))
                pygame.draw.polygon(screen, (0,0,0),((1035,310),(1060,285), (1085,310)))
                pygame.draw.polygon(screen, (0,0,0),((1120,285),(1145,310), (1170,285)))
                                                        # 0           +25         +25

                #BETTING FUNCTIONALITY!!!!!!!!!!!!!!
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x >= 1025 and x <= 1100 and y >= 275 and y <= 325:
                        if player_balance != 0:
                            player_bet += 1
                            player_balance -= 1
                    if x >= 1110 and x <= 1170 and y >= 275 and y <= 325:
                        if player_bet >= 1:
                            player_bet -= 1
                            player_balance += 1
                    #+$100
                    if x >= 1025 and x <= 1100 and y >= 205 and y <= 255:
                        if player_bet >= 0 and player_balance >= 100:
                            player_bet += 100
                            player_balance -= 100
                    #+$50
                    if x >= 1110 and x <= 1180 and y >= 205 and y <= 255:
                        if player_bet >= 0 and player_balance >= 50:
                            player_bet += 50
                            player_balance -= 50
                    #-$100
                    if x >= 1025 and x <= 1100 and y >= 345 and y <= 395:
                        if player_balance >= 0 and player_bet >= 100:
                            player_bet -= 100
                            player_balance += 100
                    #-$50
                    if x >= 1110 and x <= 1180 and y >= 345 and y <= 395:
                        if player_balance >= 0 and player_bet >= 50:
                            player_bet -= 50
                            player_balance += 50
                                            
                    
            
                    if x >= 1025 and x <= 1175 and y >= 500 and y <= 550: #DEAL AND START THE ACTUAL GAME
                        run2 = False
                        
                        

                    

            else:
                pygame.draw.rect(screen,(100,100,100), (1185, 250, 15, 100))     
                pygame.draw.rect(screen,(0,0,0), (1185, 250, 15, 100),3) 
            pygame.display.update()
        else:
            startdisplay = blackjack() #IF THE RUN = FALSE THE RUN THIS


introScreen = IntroScreen(pygame.image.load("intro.png"))

runity = True
while runity == True: #MAIN WWHILE LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             runity = False
    introScreen.run()







