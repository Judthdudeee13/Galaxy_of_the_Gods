from settings import *
from settings import * 

#loads single images
def image_loader(*path):
    return pygame.transform.scale_by(pygame.image.load(join(*path)), SCALE).convert_alpha()

#loads folders
def folder_importer(name, *path):
    surfs = []
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
            full_path = join(folder_path, file_name)
            surfs.append(pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(), SCALE))
    return surfs

#loads audio
def audio_importer(name, *path):
    audio_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            audio_dict[file_name.split('.')[0]] = pygame.mixer.Sound(join(folder_path, file_name))
    return audio_dict

#loads animation folders
def folder_loader(*path):
    files = {}
    for folder_path, folders, _ in walk(join(*path)):
        for folder in folders:
            files[folder] = folder_importer(folder, folder_path, folder)

    return files

def tile_importer(cols, *path):
    attack_frames = []
    full_path = join(*path)
    surf = pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(), SCALE)
    cutout_width = surf.get_width() / cols
    for col in range(cols):
        cutout_surf = pygame.Surface((cutout_width, surf.get_height()), pygame.SRCALPHA)
        cutout_rect = pygame.FRect(cutout_width* col, 0, cutout_width, cutout_surf.get_height())
        cutout_surf.blit(surf, (0, 0), cutout_rect)
        attack_frames.append(cutout_surf)
    return attack_frames
