#import used modules
import pygame, sys, random, time, pickle, pyscroll
import Backgrounds, Player

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

#files
main_world_tileset = "tilesets_tiled/test_world.tmx"

#set up fonts
basic = pygame.font.SysFont(None, 75)
datas = pygame.font.SysFont(None, 25)
important = pygame.font.SysFont(None, 90)


# Player
player = Player.Player(main_world_tileset)

#backgrounds
main_world = Backgrounds.Background(window, main_world_tileset, player, (WIDTH_RATIO, HEIGHT_RATIO), WIDTH, HEIGHT)

run = True
while run:
    #recive mouse and keyboard inputs
    keys = pygame.key.get_pressed()
    mouse_keys = pygame.mouse.get_pressed()

    

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
    