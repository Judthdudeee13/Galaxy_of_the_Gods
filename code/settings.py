# module imports
import pygame
from os.path import join
from os import walk
import math
import random
import pytmx

TILE_SIZE = 32

# finding aspect ratio
pygame.init()

ASPECT_WIDTH, ASPECT_HEIGHT = 320, 180


ASPECT_RATIO = ASPECT_WIDTH / ASPECT_HEIGHT  # 16x9


# window size
SIZE = pygame.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = SIZE.current_w+1, SIZE.current_h+1


# scale
def get_closest_16_9_resolution(screen_width, screen_height, base_width, base_height):
    # Compute aspect ratio 16:9
    aspect_ratio = 16 / 9

    # Calculate the width/height that would fit the 16:9 ratio while being under screen dimensions
    if screen_width / screen_height > aspect_ratio:
        # Screen is wider, adjust height
        target_height = screen_height
        target_width = int(target_height * aspect_ratio)
        scale = target_width / base_width
        return scale
    else:
        # Screen is taller, adjust width
        target_width = screen_width
        target_height = int(target_width / aspect_ratio)
        scale = target_height / base_height
        return scale


SCALE = int(get_closest_16_9_resolution(
    WINDOW_WIDTH, WINDOW_HEIGHT, ASPECT_WIDTH, ASPECT_HEIGHT)
)

pygame.quit()
