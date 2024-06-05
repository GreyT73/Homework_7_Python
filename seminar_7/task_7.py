import os
from pathlib import Path

from task_5 import extensions_in_directories

check_dict = {'video': ['mkv', 'avi', 'mp4'], 'audio': ['mp3', 'wav', 'ogg'], 'pictures': ['jpeg', 'bmp', 'jpg', 'png']}


def sort_files(path: Path, groups: dict = None):
    if not groups:
        groups = {Path('video'): ['mkv', 'avi', 'mp4'], Path('audio'): ['mp3', 'wav', 'ogg'],
                  Path('pictures'): ['jpeg', 'bmp', 'jpg', 'png']}
    os.chdir(path)
    reverse_groups = {}
    for directory, ext in groups.items():
        if not directory.is_dir():
            directory.mkdir()
        for ex in ext:
            reverse_groups[f'.{ex}'] = directory
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace((reverse_groups[file.suffix] / file.name))


if __name__ == '__main__':
    extensions_in_directories(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7', bin=2, jpg=3, txt=1, mp3=5,
                              avi=2, mkv=3)
    sort_files(Path(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7'))
