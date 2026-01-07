import pyscroll, pytmx, pygame

class Background:
    def __init__(self, window, background_file, focus, aspect_ratio, width, height):
        self.aspect_ratio = aspect_ratio
        self.window = window
        self.width = width
        self.height = height
        self.tmx_data = pytmx.load_pygame(background_file)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.focus = focus
        self.render_surface = pygame.Surface((width, height)).convert_alpha()
        self.background = pyscroll.BufferedRenderer(self.map_data, (self.width, self.height),clamp_camera=True)
        self.background_group = pyscroll.PyscrollGroup(map_layer = self.background)
        self.background_group.add(focus)
        

    def load(self):
        cam_x, cam_y = self.focus.rect.center
        self.background_group.center((int(cam_x), int(cam_y)))
        self.background_group.draw(self.render_surface)
        self.scaled_surface = pygame.transform.scale(self.render_surface, (int(self.aspect_ratio[0]*self.width), int(self.aspect_ratio[1]*self.height)))
        self.window.blit(self.scaled_surface, (0,0))