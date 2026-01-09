#pyscroll -- autoscroller
#pytmx -- loads tmx files
#pygame -- image module runs everything
import pyscroll, pytmx, pygame

#class for the backgrounds
class Background:
    #set up background
    def __init__(self, window, background_file, focus, aspect_ratio, width, height):
        #window = window for game
        #background file = file to pull images and setup from
        #focus = what the camra centers on
        #aspect_ratio = the aspect ratio of the computer for full screen
        #width = inital width of window(not scaled yet)
        #height = inital height of window(not scalled yet)
        self.aspect_ratio = aspect_ratio
        self.window = window
        self.width = width
        self.height = height
        self.focus = focus
        #tmx data for background
        self.tmx_data = pytmx.load_pygame(background_file)
        #turns it into a pyscroll window
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        #surface everything is rendered on befpre scalled to window
        self.render_surface = pygame.Surface((width, height)).convert_alpha()
        #puts pyscroll info on surface
        self.background = pyscroll.BufferedRenderer(self.map_data, (self.width, self.height),clamp_camera=True)
        #group that pyscoll uses
        self.background_group = pyscroll.PyscrollGroup(map_layer = self.background)
        #adding focus to the group
        self.background_group.add(focus)
        

    #loads background to window
    def load(self):
        #the camera x and y focues off of the focus
        cam_x, cam_y = self.focus.rect.center
        self.background_group.center((int(cam_x), int(cam_y)))
        #loads group on surface
        self.background_group.draw(self.render_surface)
        self.scaled_surface = pygame.transform.scale(self.render_surface, (int(self.aspect_ratio[0]*self.width), int(self.aspect_ratio[1]*self.height)))
        #loads pyscroll group/surface onto window
        self.window.blit(self.scaled_surface, (0,0))
        