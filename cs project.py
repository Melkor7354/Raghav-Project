import pygame, sqlite

pygame.init()

a,b=1200,673
background_colour = (90, 200, 60)
clock = pygame.time.Clock()
main_font = pygame.font.Font(None, 50)


base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(a/2, b/2, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

screen = pygame.display.set_mode((a, b))
background = pygame.image.load('backdrop.jpg')
bg2 = pygame.image.load("Soccer_pitch_dimensions.png")
bg3 = pygame.image.load("pngtree-background-with-a-football-or-soccer-ball-on-grass-with-spotlight-picture-image_2032894.jpg")
player = pygame.image.load("man1.png")
bg4 = pygame.image.load("market1.jpg")
pygame.display.set_caption('football unlimited')
screen.fill(background_colour)

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
def man(a,b):
    screen.blit(player,(a,b))
running = True
i = 0
button = Button(a // 2 -110 , b // 2 + 200, 200, 50, (100, 190, 60), "PLAY")
b1 = Button(a // 2 - 110, b // 2 + 100, 270, 50, (100, 60, 100), "TRANSFER MARKET")
b2 = Button(a // 2 - 110, b // 2 - 100, 200, 50, (100, 60, 100), "YOUR SQUAD")
b3 = Button(a // 2 - 110, b // 2, 200, 50, (100, 60, 100), "YOUR RESULTS")
#buy1 =
while running:

    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(pygame.mouse.get_pos()) and i==0:
                # Code to switch to a new screen goes here
                i = 1
            if b3.is_clicked(pygame.mouse.get_pos()) and i==2:
                # Code to switch to a new screen goes here
                i = 5
            if b2.is_clicked(pygame.mouse.get_pos()) and i==2:
                # Code to switch to a new screen goes here
                i = 4
            if b1.is_clicked(pygame.mouse.get_pos()) and i==2:
                # Code to switch to a new screen goes here
                i = 3

    if i==0:
        screen.blit(background,(0,0))
        text = main_font.render("""FOOTBALL UNLIMITED""", False, (200, 200, 200))
        textRect = text.get_rect()
        textRect.center = (a// 2, b // 2 - 200)
        screen.blit(text,textRect)
        button.draw(screen)

#
    if i==1:

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
#
    if i==2:
      screen.blit(bg3,(0,0))
      b1.draw(screen)
      b2.draw(screen)
      b3.draw(screen)

    if i == 3:
     screen.blit(bg4,(0,0))
     man(300,200)

     man(800,200)




    pygame.display.update()
    clock.tick(30)

