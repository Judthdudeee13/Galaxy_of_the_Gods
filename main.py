#import used modules
import pygame, sys, random, time, pickle, pyscroll
import backgrounds

#setup pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#set up window  
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)

#screen width and height
SCREEN_HEIGHT = window.get_height()
SCREEN_WIDTH = window.get_width()

#set width and height
WIDTH  = 512
HEIGHT = 288

#aspect ratio
WIDTH_RATIO = SCREEN_WIDTH/WIDTH
HEIGHT_RATIO = SCREEN_HEIGHT/HEIGHT

pygame.display.set_caption('Galaxly of the gods')
logo = pygame.image.load("game_logo.png")
pygame.display.set_icon(logo)

#set up fonts
basic = pygame.font.SysFont(None, 75)
datas = pygame.font.SysFont(None, 25)
important = pygame.font.SysFont(None, 90)


# Player
player = pygame.sprite.Sprite()
player.image = pygame.Surface((16, 16))
player.image.fill((255, 0, 0))
player.rect = player.image.get_rect(topleft = (0, 0))

#backgrounds
main_world = backgrounds.background(window, "tilesets_tiled/test_world.tmx", player, (WIDTH_RATIO, HEIGHT_RATIO), WIDTH, HEIGHT)

run = True
while run:
    #recive mouse and keyboard inputs
    keys = pygame.key.get_pressed()
    mouse_keys = pygame.mouse.get_pressed()

    #temporary player
    if keys[pygame.K_w]:
        player.rect.y -= 2
    if keys[pygame.K_s]:
        player.rect.y +=2
    if keys[pygame.K_a]:
        player.rect.x -= 2
    if keys[pygame.K_d]:
        player.rect.x += 2

    #load main world map
    main_world.load()

    #make sure window can close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_ESCAPE]:
        run = False

    #update screen
    pygame.display.update()

    #frame rate 60
    clock.tick(60)

pygame.quit()
sys.exit()
    