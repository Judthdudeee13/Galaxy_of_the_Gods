from settings import *

from settings import * 

class Importer:
    def __init__(self):
        self.folders = {}
    def folder_importer(self, name, *path):
        surfs = {}
        for folder_path, _, file_names in walk(join(*path)):
            for file_name in file_names:
                full_path = join(folder_path, file_name)
                surfs[file_name.split('.')[0]] = pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(), SCALE)
        self.folders[name] = surfs

    def audio_importer(self, name, *path):
        audio_dict = {}
        for folder_path, _, file_names in walk(join(*path)):
            for file_name in file_names:
                audio_dict[file_name.split('.')[0]] = pygame.mixer.Sound(join(folder_path, file_name))
        self.folders[name] = audio_dict

