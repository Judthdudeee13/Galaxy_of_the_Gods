#work on cool down currently game works 03/26/2025
#if abs(time.time()-attack_image()) <= reload_time and attack_image > 0:
#weapons(reload_time, ammo, damage, direction, range)
#monstersset_up(self, name, damage, health, speed, times, window, width, height, player_width, player_height)



import pygame, sys, random, time, pickle
import monster as mon
from pygame.locals import *
import inventory as inv
import weapons

keys = pygame.key.get_pressed()

#setup pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
inventorys = inv.inventory_class()

GAME_DEVELOPER_MACANICS = True

#set height and width
HEIGHT = 700
WIDTH = 1300

#set up window  
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('game')

#set up fonts
basic = pygame.font.SysFont(None, 75)
datas = pygame.font.SysFont(None, 25)
important = pygame.font.SysFont(None, 90)

#Colors
BG = "#ebab34"
RED = '#FF0000'
GREEN = '#00ff00'
BLACK = "#000000"
WHITE = "#FFFFFF"
BLUE = "#0000ff"

#set up starting variables
it1 = 2
q = False
inventory = {'sword': [0], 'range': [0]}
inventory_time = time.time()
keys = pygame.key.get_pressed()
bg = 1
yes = False
no = False
sx = -100
sy = -100
wait_time = time.time()
yes_or_no = 0
damage_taken = 0
hearts = 3
frame = 0
player_frame = 0
reload_time = time.time()
direction = "down"

#game developer settings
def game_developer():
   if GAME_DEVELOPER_MACANICS:
        playerx = str(p.centerx)
        playery = str(p.centery)
        px = datas.render(f"X: {playerx}", True, "#000000")
        px1 = px.get_rect()
        px1.centerx = 25
        px1.centery = 25
        window.blit(px, px1)
        py = datas.render(f"Y: {playery}", True, "#000000")
        py1 = py.get_rect()
        py1.centerx = 25
        py1.centery = 50
        window.blit(py, py1)

#mouse
def mouse_pos():
    global mouse_rect
    x, y = pygame.mouse.get_pos()
    mouse = pygame.image.load("mouse.png")
    mouse_rect = mouse.get_rect()
    mouse_rect.centerx = x
    mouse_rect.centery = y
    window.blit(mouse, mouse_rect)
    
def mouse_buttons():
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        return 0

#player
def player_image():
    global player_frame
    global player
    if frame%12 == 0 or frame == 0:
        player_frame += 1
    if player_frame == 9:
        player_frame = 1
    if player_frame == 1:
        player = pygame.image.load("normal_slime2.png")
    if player_frame == 2:
        player = pygame.image.load("normal_slime2.png")
    if player_frame == 3:
        player = pygame.image.load("normal_slime3.png")
    if player_frame == 4:
        player = pygame.image.load("normal_slime4.png")
    if player_frame == 5:
        player = pygame.image.load("normal_slime5.png")
    if player_frame == 6:
        player = pygame.image.load("normal_slime5.png")
    if player_frame == 7:
        player = pygame.image.load("normal_slime4.png")
    if player_frame == 8:
        player = pygame.image.load("normal_slime3.png")
    player = pygame.transform.scale(player, (50, 50))
    return player

player = player_image()
player = pygame.transform.scale(player, (50, 50))
p = player.get_rect()
p.centerx = 700
p.centery = 500

move_speed = 3
death = False

up = True
down = True
left = True
right = True
move_up = False
move_down = False
move_right = False
move_left = False
#moving the player
def move():
    global move_speed
    global move_up
    global move_down
    global move_left
    global move_right
    extraMove = False
    keys = pygame.key.get_pressed()
    move_up = False
    move_down = False
    move_right = False
    move_left = False
    if keys[pygame.K_LSHIFT]:
        move_speed = 3
        extraMove = True   
    if up:
        if keys[pygame.K_w]:
            p.centery -= move_speed
            move_up = True
            if p.colliderect(monsters_rect):
                p.centery += move_speed

    if down: 
        if keys[pygame.K_s]:
           p.centery += move_speed
           move_down = True
           if p.colliderect(monsters_rect):
                p.centery -= move_speed

    if left:
        if keys[pygame.K_a]:
            p.centerx -= move_speed
            move_left = True
            if p.colliderect(monsters_rect):
                p.centerx += move_speed
    if right:
        if keys[pygame.K_d]:
            p.centerx += move_speed
            move_right = True
            if p.colliderect(monsters_rect):
                p.centerx -= move_speed
    if extraMove == True:
        move_speed = 6

class load_heart:
    def __init__(self, part, x, y):
        self.part = part
        self.x = x
        self.y = y
        

    def blit(self):
        if self.part == "4":
            heart = pygame.image.load("full_heart.png")
        if self.part == "3":
            heart = pygame.image.load("3_quarter_heart.png")
        if self.part == "2":
            heart = pygame.image.load("half_heart.png")
        if self.part == "1":
            heart = pygame.image.load("quarter_heart.png")
        if self.part == "0":
            heart = pygame.image.load("emptey.png")
        heart_rect = heart.get_rect()
        heart_rect.x = self.x
        heart_rect.y = self.y
        window.blit(heart, heart_rect)

def life(hearts, damages):
    damage = int(damages)
    current_hearts = hearts - (damage/4)
    for x in range(hearts):
        if current_hearts >= 1:
            heart = load_heart("4", x*21, 0)
            heart.blit()
        if current_hearts == 0.75:
            heart = load_heart("3", x*21, 0)
            heart.blit()
        if current_hearts == 0.5:
            heart = load_heart("2", x*21, 0)
            heart.blit()
        if current_hearts == 0.25:
            heart = load_heart("1", x*21, 0)
            heart.blit()
        if current_hearts <= 0:
            heart = load_heart("0", x*21, 0)
            heart.blit()
        
        current_hearts -= 1


direction = False
hit_box_blit1 = False
hit_box_pos1 = False
def attack():
    global direction
    global attack_image
    global hit_box_blit1
    global hit_box_pos1
    global hit_box_sur1
    global damage_given
    global reload_time
    if move_up == True:
        direction = 'up'
    if move_down == True:
        direction = 'down'
    if move_left == True:
        direction = 'left'
    if move_right == True:
        direction = 'right'
    try:
        if keys[pygame.K_SPACE]:
            if inventory['sword'][1] == 'basic_sword':
                hit_box_sur10, hit_box_pos, damage_given, hit_box, reload_time1 = basic_sword.swing_blit()
                if abs(reload_time-time.time()) >= reload_time1:
                    attack_image = 10
                    hit_box_blit = hit_box
                    hit_box_pos2 = hit_box_pos
                    hit_box_sur = hit_box_sur10
                    reload_time2 = reload_time1
                    if direction == 'up':
                        hit_box_pos.x = p.x+12
                        hit_box_pos.y = p.y-15
                    if direction == 'down':
                        hit_box_pos.x = p.x+12
                        hit_box_pos.y = p.y+40
                    if direction == 'left' or direction == 'None':
                        hit_box_pos.x = p.x-12
                        hit_box_pos.y = p.y+12
                    if direction == 'right':
                        hit_box_pos.x = p.x+42
                        hit_box_pos.y = p.y+12
            
                    all_monsters_recive_damage(hit_box_sur, hit_box_pos1, damage_given)
                    reload_time = time.time()
    
    
        if attack_image > 0:
            attack_image -= 1
            try:
                hit_box_blit1 = hit_box_blit
                hit_box_pos1 = hit_box_pos2
                hit_box_sur1 = hit_box_sur
            except:
                hit_box_blit1 = hit_box_blit1
                hit_box_pos1 = hit_box_pos1
                hit_box_sur1 = hit_box_sur1

            if direction == 'up':
                hit_box_pos1.x = p.x+12
                hit_box_pos1.y = p.y-15
                hit_box_blit180 = pygame.transform.rotate(hit_box_blit1, 180)
                window.blit(hit_box_blit180, hit_box_pos1)
            if direction == 'down':
                hit_box_pos1.x = p.x+12
                hit_box_pos1.y = p.y+40
                hit_box_blit0 = pygame.transform.rotate(hit_box_blit1, 0)
                window.blit(hit_box_blit0, hit_box_pos1)
            if direction == 'left' or direction == 'None':
                hit_box_pos1.x = p.x-12
                hit_box_pos1.y = p.y+12
                hit_box_blit270 = pygame.transform.rotate(hit_box_blit1, 270)
                window.blit(hit_box_blit270, hit_box_pos1)
            if direction == 'right':
                hit_box_pos1.x = p.x+42
                hit_box_pos1.y = p.y+12
                hit_box_blit90 = pygame.transform.rotate(hit_box_blit1, 90)
                window.blit(hit_box_blit90, hit_box_pos1)





            
        
            
    except:
        pass
def all_monsters_recive_damage(box, pos, damage):
    monsters.recive_damage(box, pos, damage)

#Inventory


#backgrounds
def load_background1():
    keys = pygame.key.get_pressed()
    global background1
    global background
    global back1
    global q
    global up
    global left
    global down
    global right
    global bg
    global it1
    keys = pygame.key.get_pressed()
    background = pygame.image.load("background1.PNG")
    background1 = pygame.transform.scale(background,(1300,700))
    back1 = background1.get_rect()
    back1.centerx = 650
    back1.centery = 350
    chest = pygame.image.load("chest.PNG")
    chest = pygame.transform.scale(chest,(150,100))
    chest_rect = chest.get_rect()
    chest_rect.centerx = 650
    chest_rect.centery = 100
    window.blit(background1, back1)
    window.blit(chest, chest_rect)
    up = True
    down = True
    left = True
    right = True
    if p.centerx >= 600 and p.centerx <= 700 and p.centery <= 150 and keys[pygame.K_e]:
        inventory['sword'].append('basic_sword')
        q = True
        inventorys.load_inventory_background()
        inventorys.load_inventory(inventory)
        bg = 0
    if p.centery <= 94 and p.centerx >= 611 and p.centerx <= 700:
        left = False
    if p.centery <= 94 and p.centerx >= 610 and p.centerx <= 699:
        right = False
    if p.centerx <= 85:
        left = False
    if p.centerx >= 1200:
        right = False
    if p.centery <= 75:
        up = False
    if p.centery >= 600:
        down = False
    if p.centery <= 95 and p.centerx >= 610 and p.centerx <= 700:
        up = False
    if p.centerx >= 215 and p.centerx <= 235 and p.centery <= 75 and keys[K_w] and abs(it1-time.time()) > 1:
        bg = 2
        it1 = time.time()

def load_background2():
    global q
    global up
    global left
    global down
    global right
    global bg
    global it1
    keys = pygame.key.get_pressed()
    background = pygame.image.load("background2.PNG")
    background1 = pygame.transform.scale(background,(1300,700))
    back1 = background1.get_rect()
    back1.centerx = 650
    back1.centery = 350
    up = True
    down = True
    left = True
    right = True
    if p.centerx <= 85:
        left = False
    if p.centerx >= 1200:
        right = False
    if p.centery <= 75:
        up = False
    if p.centery >= 600:
        down = False
    window.blit(background1, back1)
    if p.centerx >= 215 and p.centerx <= 235 and p.centery <= 75 and keys[K_w] and abs(it1-time.time()) > 1:
        bg = 1
        it1 = time.time()
    if p.centery >= 440 and p.centery <= 480 and p.centerx >= 1050 and abs(it1-time.time()) > 1 and keys[K_d]:    
        bg = 3
        p.centerx = 90
        p.centery = 390
        it1 = time.time()
        

def load_background3():
    global q
    global up
    global left
    global down
    global right
    global bg
    global it1
    global damage_taken
    keys = pygame.key.get_pressed()
    background = pygame.image.load("background3.PNG")
    background1 = pygame.transform.scale(background,(1300,700))
    back1 = background1.get_rect()
    back1.centerx = 650
    back1.centery = 350
    up = True
    down = True
    left = True
    right = True
    left = False
    if p.centerx >= 1200:
        right = False
    if p.centery <= 75:
        up = False
    if p.centery >= 600:
        down = False
         

    window.blit(background1, back1)
    monsters.targeting(p)
    monsters.blit()
    try:
        damage_taken += monsters.damage_givin(p)
    except:
        pass
    if p.centery >= 370 and p.centery <= 410 and p.centerx <= 90 and abs(it1-time.time()) > 1 and keys[K_a]:    
        bg = 2
        p.centerx = 1200
        p.centery = 460
        it1 = time.time()

    if p.centery >= 370 and p.centery <= 410 and p.centerx <= 90 and abs(it1-time.time()) > 1 and keys[K_a]:    
        bg = 2
        p.centerx = 1200
        p.centery = 460
        it1 = time.time()

    

def load_background4():
    global q
    global up
    global left
    global down
    global right
    global bg
    global it1
    global damage_taken
    keys = pygame.key.get_pressed()
    background = pygame.image.load("background4.PNG")
    background1 = pygame.transform.scale(background,(1300,700))
    back1 = background1.get_rect()
    back1.centerx = 650
    back1.centery = 350
    up = True
    down = True
    left = True
    right = True
    if p.centerx <= 85:
        left = False
    if p.centerx >= 1200:
        right = False
    if p.centery <= 75:
        up = False
    if p.centery >= 600:
        down = False
         
    if p.centery >= 370 and p.centery <= 410 and p.centerx <= 90 and abs(it1-time.time()) > 1 and keys[K_a]:    
        bg = 2
        p.centerx = 1200
        p.centery = 460
        it1 = time.time()



#game data
def clear_data():
    global data
    data = {'bg': 1, 'inventory': inventory, 'x': '700', 'y': '500', "hearts": 3, 'damage': damage_taken}

def dump_data():
    global data
    data = {'bg': bg, 'inventory': inventory, 'x': p.centerx, 'y':p.centery, 'hearts': hearts, 'damage': damage_taken}
    with open('gotg.pickle', 'wb') as file:
        pickle.dump(data, file)

def open_data():
    global data
    with open('gotg.pickle', 'rb') as file:
        data = pickle.load(file)

def reset():
    global bg
    global inventory
    global new_music
    global hearts
    bg = data['bg']
    inventory = data['inventory']
    p.centerx = int(data['x'])
    p.centery = int(data['y'])
    hearts = int(data['hearts'])
    new_music = 1

def yes_no(text):
    global yes
    global no
    global yes_or_no
    window.fill(BG)
    yes = pygame.draw.rect(window, RED, (700, 400, 125, 75))
    no = pygame.draw.rect(window, GREEN, (500, 400, 125, 75))
    no_text = important.render('NO', True, BLACK)
    no_rect = no_text.get_rect()
    no_rect.center = no.center
    yes_text = important.render('YES', True, BLACK)
    yes_rect = yes_text.get_rect()
    yes_rect.center = yes.center
    window.blit(no_text, no_rect)
    window.blit(yes_text, yes_rect)
    texts = important.render(text, True, BLACK)
    t = texts.get_rect()
    t.centerx = 650
    t.centery = 300 
    window.blit(texts, t)
    mouse_pos()
    if mouse_buttons() == 0 and abs(wait_time - time.time()) > 1:
        if mouse_rect.colliderect(yes_rect):
            yes_or_no = "yes"
        if mouse_rect.colliderect(no_rect):
            yes_or_no = "no"
    
    
def menu():
    global game
    global bg
    global wait_time
    background = pygame.image.load("menu image.PNG")
    back1 = background.get_rect()
    back1.centerx = 650
    back1.centery = 350
    window.blit(background, back1)
    new_game = pygame.draw.rect(window, BLUE, (700, 400, 125, 75))
    resume = pygame.draw.rect(window, BLUE, (500, 400, 125, 75))
    resume_text = datas.render('RESUME', True, WHITE)
    resume_rect = resume_text.get_rect()
    resume_rect.center = resume.center
    new_game_text = datas.render('NEW_GAME', True, WHITE)
    new_game_rect = new_game_text.get_rect()
    new_game_rect.center = new_game.center
    window.blit(resume_text, resume_rect)
    window.blit(new_game_text, new_game_rect)
    mouse_pos()
    if mouse_buttons() == 0 and abs(wait_time -  time.time()) > 1:
        if mouse_rect.colliderect(new_game_rect):
            bg = -1
            wait_time = time.time()
        if mouse_rect.colliderect(resume_rect):
            open_data()
            game = True



        


 
    


#start of main game code
clear_data()
#dump_data()


def load_weapons():
    global basic_sword
    basic_sword = weapons.melee()
    basic_sword.set_up(0.5, 0, 1, direction, 25)

def load_monsters():
    global monsters
    global monsters_mask
    global monsters_rect
    monsters = mon.monster_class()
    monsters.set_up(1, 1, 3, 2, 1, window, 32, 32, 50, 50)
    monsters_rect, monsters_mask = monsters.load_moster()

game = 0
obg = bg
bg = 0
load_weapons()
load_monsters()
while game == 0:
    if bg != -1:
        menu()
    if bg == -1:
        while yes_or_no == 0:
            yes_no('''Are You Sure You Want To Restart''')
            for event in pygame.event.get():
                if event.type == QUIT:
                    if bg == 0:
                        bg = obg
                    dump_data()
                    pygame.quit()
                    sys.exit()

            #update screen
            pygame.display.update()

            #frame rate 60
            clock.tick(60)
        if yes_or_no == "yes":
            clear_data()
            reset()
            dump_data()
            open_data()
            game = True
            yes_or_no = 0
        else:
            bg = 0
            wait_time = time.time()
            yes_or_no = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            if bg == 0:
                bg = obg
            dump_data()
            pygame.quit()
            sys.exit()

    #update screen
    pygame.display.update()

    #frame rate 60
    clock.tick(60)

open_data()
bg = data['bg']
inventory = data['inventory']
p.centerx = int(data['x'])
p.centery = int(data['y'])
new_music = 0
hearts = int(data['hearts'])
damage_taken = int(data['damage'])

while game == True:
    keys = pygame.key.get_pressed()
    #open inventory
    if keys[K_q] and bg != 0 and time.time() -  inventory_time > .5:
        obg = bg
        bg = 0
        inventory_time = time.time()
    elif bg == 0 and keys[K_q] and time.time() -  inventory_time > .5:
        bg = obg
        inventory_time = time.time()

    if keys[K_e]:
        inventory_time = time.time()

    #saving game
    if keys[K_r]:
        if bg == 0:
            bg = obg
        dump_data()
  
    #load backgrounds
    if bg == 1:
        load_background1()
    if bg == 2:
       load_background2()
    if bg == 3:
       load_background3()

       #load player
    player = player_image()
    window.blit(player, p)
    life(hearts, damage_taken)

       #make sure background is ontop of player
    #Show developer machanics
    game_developer()

    if bg == 0:
        inventorys.load_inventory_background()
        inventorys.load_inventory(inventory)

    #move player
    if bg != 0:
        move()
        attack()
    else:
        pass

    #music
    if new_music == 1:
         new_music = 0
         pygame.mixer.music.load("Chill Beat (1).mp3")
         pygame.mixer.music.set_volume(0.7)
         pygame.mixer.music.play()

    #make sure window can close
    for event in pygame.event.get():
        if event.type == QUIT:
            if bg == 0:
                bg = obg
            dump_data()
            pygame.quit()
            sys.exit()

    #update screen
    pygame.display.update()

    #frame rate 60
    clock.tick(60)
    frame += 1
    if frame == 60:
        frame = 0