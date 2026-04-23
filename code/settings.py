# module imports
import pygame
from os.path import join
from os import walk
import random
import pytmx

TILE_SIZE = 63

# finding aspect ratio
pygame.init()

ASPECT_WIDTH, ASPECT_HEIGHT = 854, 480


ASPECT_RATIO = ASPECT_WIDTH / ASPECT_HEIGHT  # 16x9


# window size
SIZE = pygame.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = SIZE.current_w, SIZE.current_h


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


SCALE = get_closest_16_9_resolution(
    WINDOW_WIDTH, WINDOW_HEIGHT, ASPECT_WIDTH, ASPECT_HEIGHT
)

pygame.quit()
