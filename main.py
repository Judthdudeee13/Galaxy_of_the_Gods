import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (10, 10, 40)
GOLD = (255, 215, 0)
LIGHT_BLUE = (135, 206, 235)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaxy of the Gods")

clock = pygame.time.Clock()

try:
    logo = pygame.image.load("game_logo.png")
    logo = pygame.transform.scale(logo, (200, 200))
except Exception:
    logo = None

title_font = pygame.font.SysFont("arial", 48, bold=True)
subtitle_font = pygame.font.SysFont("arial", 24)
info_font = pygame.font.SysFont("arial", 18)

stars = []
import random
for _ in range(150):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    size = random.randint(1, 3)
    brightness = random.randint(150, 255)
    stars.append((x, y, size, brightness))

running = True
tick = 0

while running:
    clock.tick(FPS)
    tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(DARK_BLUE)

    for (x, y, size, brightness) in stars:
        twinkle = brightness + int(30 * pygame.math.Vector2(1, 0).rotate(tick * 2).x)
        twinkle = max(100, min(255, twinkle))
        pygame.draw.circle(screen, (twinkle, twinkle, twinkle), (x, y), size)

    if logo:
        logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, 160))
        screen.blit(logo, logo_rect)
    else:
        title_text = title_font.render("Galaxy of the Gods", True, GOLD)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 160))
        screen.blit(title_text, title_rect)

    title_text = title_font.render("Galaxy of the Gods", True, GOLD)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 380))
    screen.blit(title_text, title_rect)

    subtitle_text = subtitle_font.render("A Pygame Adventure", True, LIGHT_BLUE)
    subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 440))
    screen.blit(subtitle_text, subtitle_rect)

    info_text = info_font.render("Press ESC to quit", True, WHITE)
    info_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, 560))
    screen.blit(info_text, info_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
