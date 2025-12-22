import pygame, sys, random, time, pickle, pyscroll,

keys = pygame.key.get_pressed()
mouse_keys = pygame.mouse.get_pressed()

#setup pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#set width and height
WIDTH  = 16
HEIGHT = 9

#set up window  
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Galaxly of the gods')
logo = pygame.image.load("game_logo.png")
pygame.display.set_icon(logo)

#set up fonts
basic = pygame.font.SysFont(None, 75)
datas = pygame.font.SysFont(None, 25)
important = pygame.font.SysFont(None, 90)

while True:

    #make sure window can close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update screen
    pygame.display.update()

    #frame rate 60
    clock.tick(60)

    