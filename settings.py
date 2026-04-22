import pygame
from os.path import join
from os import walk
import random

pygame.init()

ASPECT_WIDTH, ASPECT_HEIGHT = 640, 360
TILE_SIZE = 32

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
    else:
        # Screen is taller, adjust width
        target_width = screen_width
        target_height = int(target_width / aspect_ratio)

    # Return the closest 16:9 resolution under the current screen size
    return target_width, target_height


SCALED_WIDTH, SCALED_HEIGHT = get_closest_16_9_resolution(
    WINDOW_WIDTH, WINDOW_HEIGHT, ASPECT_WIDTH, ASPECT_HEIGHT
)
print(SCALED_WIDTH / SCALED_HEIGHT)
print(SCALED_WIDTH, SCALED_HEIGHT)
print(WINDOW_WIDTH,WINDOW_HEIGHT)

pygame.quit()
