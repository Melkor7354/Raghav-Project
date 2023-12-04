import pygame
import random

import backend
import tkinter as tk
from backend import *
name_of_squad = backend.squad_name()
backend.initialize()
squad = backend.read_squad()
print(name_of_squad)
player_base = backend.player_base

pygame.init()




funds = 10000
playerprice = 4000

a , b = 1200,673
background_colour = (90, 200, 60)
clock = pygame.time.Clock()
main_font = pygame.font.Font(None, 50)
font_x = pygame.font.Font(None, 90)

base_font = pygame.font.Font(None, 32)

user_text = ''
input_rect = pygame.Rect(a/2, b/2, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

'''
start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
timer_duration = 5000  # Set the duration of the timer in milliseconds
'''

screen = pygame.display.set_mode((a, b))
background = pygame.image.load('backdrop.jpg')
bg2 = pygame.image.load("Soccer_pitch_dimensions.png")
bg3 = pygame.image.load("pngtree-background-with-a-football-or-soccer-ball-on-grass-with-spotlight-picture-image_2032894.jpg")


bg4 = pygame.image.load("market1.jpg")
pygame.display.set_caption('football unlimited')
ok = pygame.image.load("WhatsApp Image 2023-11-30 at 1.16.35 AM.jpeg")
i4bg = pygame.image.load("stadium-football-background-at-night-free-vector.jpg")
c_main = pygame.image.load("cabj.jpg")
c1 = pygame.image.load("roma.jpg")
c2 = pygame.image.load("wolfsburg.jpg")

#clubs for simulator
A=[c_main,87,'MESSI','HAALAND','VINICIUS JR','HAIDARA','MCTOMINAY','BRUNO','SHAW','MAGUIRE','RAMOS','WALKER','DE GEA'] #my club
B=[c1,78,'SALAH','KANE','SON','AMRABAT','BELLINGHAM','SAUL','PELLEGRINI','BAILLY','VARANE','TRENT ALEXANDER ARNOLD','STEELE']
C=[c2,92,'MAHREZ','HOJLUND','RASHFORD','DIABY','CASEMIRO','RICE','BALDE','WESLEY FOFANA','ALABA','DALOT','TER STEGEN']


screen.fill(background_colour)


text_price1 = main_font.render(str(playerprice), True, (20, 20, 20))
text_price2 = main_font.render(str(playerprice), True, (20, 20, 20))

textRect1 = text_price1.get_rect()
textRect2 = text_price2.get_rect()

textRect1.center = (390, 520)
textRect2.center = (890, 520)



class Button:

    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, (200,200,200))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
def man(x, a, b):
    screen.blit(pygame.image.load(x),(a,b))

def display_text(font, text, a, b):
                disp = font.render(text, False, (100, 100, 100))
                textRecty = disp.get_rect()
                textRecty.center = (a, b)
                screen.blit(disp, textRecty)

running = True
i = 0


button = Button(a // 2 - 110, b // 2 + 200, 200, 50, (100, 190, 60), "PLAY")
b1 = Button(a // 2 - 110, b // 2 + 100, 270, 50, (100, 60, 100), "TRANSFER MARKET")
b2 = Button(a // 2 - 110, b // 2 - 100, 200, 50, (100, 60, 100), "FIXTURE")
b3 = Button(a // 2 - 110, b // 2, 200, 50, (100, 60, 100), "YOUR SQUAD")
buy1 = Button(350, 570, 150, 50, (100, 190, 100), "BUY")
buy2 = Button(850, 570, 150, 50, (100, 190, 100), "BUY")
ok1 = Button(475, 350, 150, 50, (100, 190, 100), "CONFIRM")
sim = Button(a // 2 - 110, b // 2, 200, 50, (100, 190, 60), "PLAY")
next_match = Button(500, 350, 180, 50, (100, 190, 100), "NEXT MATCH")

a1 = 0
a2 = 0
rand_int = 0
rand2 = 0
y = 0
r = 0
t = 0
# my club


# buy1 =
while running:


    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                i -=1
                y,r,t=0,0,0
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.MOUSEBUTTONDOWN:

            if button.is_clicked(pygame.mouse.get_pos()) and i==0:
                # Code to switch to a new screen goes here
                i = 1
            if b3.is_clicked(pygame.mouse.get_pos()) and i==1:
                # Code to switch to a new screen goes here
                i=2
                t = 1
            if b2.is_clicked(pygame.mouse.get_pos()) and i==1:
                # Code to switch to a new screen goes here
                r=1
                i=2
            if b1.is_clicked(pygame.mouse.get_pos()) and i==1:
                # Code to switch to a new screen goes here
                y =1
                i=2
            if buy1.is_clicked(pygame.mouse.get_pos()) and i==2 and y ==1 and playerprice <= funds:
                funds = funds - playerprice
                i =2
                y=2
                a1 =1

            if buy2.is_clicked(pygame.mouse.get_pos()) and i==2 and y==1 and playerprice <= funds:
                funds = funds - playerprice
                y =2
                a1 = -1

            if ok1.is_clicked(pygame.mouse.get_pos()) and i == 2 and  y ==2:

                y = 1

            if next_match.is_clicked(pygame.mouse.get_pos()) and i == 3 and r == 1:
                    # Code to switch to a new screen goes here
                    print("next match is clicked")
                    a2 = 0




            if sim.is_clicked(pygame.mouse.get_pos()) and i == 2 and r == 1:
                    # Code to switch to a new screen goes here
                    print("simulate is clicked")
                    a2 = 1
                    rand_int = random.randint(0, 10)
                    if A[1] >= B[1]:
                        rand2 = random.randint(0, rand_int)
                        if A[1]>B[1]:
                         funds = funds + 100
                    else:
                        rand2 = random.randint(rand_int, 10)



    if i == 0:
        screen.blit(background,(0,0))
        text = main_font.render("""FOOTBALL UNLIMITED""", False, (200, 200, 200))
        textRect = text.get_rect()
        textRect.center = (a// 2, b // 2 - 200)
        screen.blit(text,textRect)
        button.draw(screen)

    '''
#
    if i == 1:
       
        screen.blit(bg2,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                #if event.key == pygame.KSCAN_KP_ENTER:
                    i=2

                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
    '''

# this is for transfer market

    if i == 1:
      
     
      
      text_funds = main_font.render(str(funds), True, (20,20,20))
      textRect3 = text_funds.get_rect()
      textRect3.center = (1100,100)
      screen.blit(bg3,(0,0))
      screen.blit(text_funds, textRect3)
      b1.draw(screen)
      b2.draw(screen)
      b3.draw(screen)


    if i == 2:
        if y == 1:

            screen.blit(background, (0, 0))

            text_funds = main_font.render(str(funds), True, (20, 20, 20))
            textRect3 = text_funds.get_rect()
            textRect3.center = (1100, 100)
            screen.blit(text_funds, textRect3)

            players = backend.random_player_image()
        
            if a1 <= 0:
                 man(players[0][4],300,200)
                 screen.blit(text_price1, textRect1)
                 buy1.draw(screen)

            if a1 >= 0:

                 man(players[1][4],800,200)
                 buy2.draw(screen)
                 screen.blit(text_price2, textRect2)

        if  y == 2:
        
            screen.blit(text_funds, textRect3)
            screen.blit(ok,(190,100))
            text_funds = main_font.render(str(funds), True, (20,20,20))
            textRect3 = text_funds.get_rect()
            textRect3.center = (1100,100)
            ok1.draw(screen)

# this is for match simulator
    if i == 2 and r == 1:
        
     
        screen.blit(i4bg,(0,0))
        text_funds = main_font.render(str(funds), True, (20,20,20))
        textRect3 = text_funds.get_rect()
        textRect3.center = (1100,100)
        screen.blit(text_funds, textRect3)

        screen.blit(A[0],(300,100))
        screen.blit(B[0],(800,100))

        text4 = main_font.render("""V/S""", False, (200, 200, 200))
        textRect4 = text4.get_rect()
        textRect4.center = (a // 2, b // 2 - 200)
        screen.blit(text4,textRect4)

        if a2 == 0:

            sim.draw(screen)






        if a2 == 1:



            text41 = main_font.render(str(rand_int), False, (200, 200, 200))
            textRect41 = text41.get_rect()
            textRect41.center = (350, 300)
            screen.blit(text41, textRect41)

            text42 = main_font.render(str(rand2), False, (200, 200, 200))
            textRect42 = text42.get_rect()
            textRect42.center = (850, 300)
            screen.blit(text42, textRect42)

            next_match.draw(screen)

            if rand_int > rand2:

                text43 = font_x.render("you win", False, (100, 100, 100))
                textRect43 = text43.get_rect()
                textRect43.center = (600, 455)
                screen.blit(text43, textRect43)

            if rand_int == rand2:

                text44 = font_x.render("DRAW", False, (100, 100, 100))
                textRect44 = text44.get_rect()
                textRect44.center = (600, 455)
                screen.blit(text44, textRect44)

            if rand_int < rand2:
                display_text(font_x, "you loss", 600, 455)











    """
        
        # Calculate elapsed time
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time

        # Clear the screen

        # Display the timer value on the screen
            timer_text = main_font.render(f"Time: {elapsed_time / 1000:.2f}s", True, (10,10,10))
            screen.blit(timer_text, (a//2, b//2))

        # Check if the timer has reached its duration
            if elapsed_time >= timer_duration:
                print("Timer reached!")
            # You can add code here to perform actions when the timer reaches its duration
            # For example, reset the timer for a countdown effect
                start_time = pygame.time.get_ticks()

    """

    pygame.display.update()
    clock.tick(60)

    '''
    print(i)
    print(r)
    print(y)
    '''



