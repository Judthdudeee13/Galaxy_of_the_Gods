from settings import *

from settings import * 


def folder_importer(name, *path):
    surfs = []
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
            full_path = join(folder_path, file_name)
            surfs.append(pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(), SCALE))
    return surfs

def audio_importer(name, *path):
    audio_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            audio_dict[file_name.split('.')[0]] = pygame.mixer.Sound(join(folder_path, file_name))
    return audio_dict

def folder_loader(*path):
    files = {}
    for folder_path, folders, _ in walk(join(*path)):
        for folder in folders:
            files[folder] = folder_importer(folder, folder_path, folder)

    return files
