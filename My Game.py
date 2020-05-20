import pygame
from pygame import mixer
from random import randint

pygame.init()

x = 540
y = 360
pos_x = 330
pos_y = 800

pos_y_a = 1200
pos_y_c = 1600

velocity = 15
velocity_others = 20
mixer.music.load('Vintage_mix.mp3')
mixer.music.play(-1)
bottom = pygame.image.load('track.png')
car = pygame.image.load('main_car.png')
blue_car = pygame.image.load('blue_car.png')
white_car = pygame.image.load('white_car.png')
black_car = pygame.image.load('black_car.png')

timer = 0
tempo_second = 0

font = pygame.font.SysFont('arial black', 30) 
text = font.render("Seconds: ", True, (255,255,255), (0,0,0)) 
post_text = text.get_rect()
post_text.center = (68,60) 

window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("My Car Game") 
window_open = True 

while window_open :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False

    commands = pygame.key.get_pressed()
    if commands[pygame.K_UP]:
        y -= velocity
    if commands[pygame.K_DOWN]:
        y += velocity
    if commands[pygame.K_RIGHT] and x <= 650:
        x += velocity
    if commands[pygame.K_LEFT] and x >= 327:
        x -= velocity

    if (timer < 10):
        timer += 1
    else:
        tempo_second += 1
        text = font.render("  Seconds: "+str(tempo_second), True, (255,255,255), (0,0,0))
        timer = 0


    if (pos_y <= -200) and (pos_y_a <= -200) and (pos_y_c <= -200):
        pos_y = randint(800,1100) 
        pos_y_a = randint(1400,2000)
        pos_y_c = randint(2300,3000)

    pos_y -= velocity_others + randint(1,10)
    pos_y_a -= velocity_others + randint(1,10)
    pos_y_c -= velocity_others + randint(1,10)

    window.blit(bottom,(0,0)) 
    window.blit(car, (x,y))
    window.blit(blue_car, (pos_x, pos_y)) 
    window.blit(white_car,(pos_x + 163, pos_y_a)) 
    window.blit(black_car,(pos_x + 310, pos_y_c)) 
    window.blit(text, post_text) 

    pygame.display.update()

pygame.quit()
