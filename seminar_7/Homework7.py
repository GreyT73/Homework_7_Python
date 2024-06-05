import os
from pathlib import Path
from task_5 import extensions_in_directories
from task_7 import sort_files
def rename_files(path=Path.cwd(), new_name: str = None, digits: int = 2, ext: str = None,
                 new_ext: str = None,
                 cut: list = None):
    if isinstance(path, str):
        path = Path(path)
    os.chdir(path)
    sub_digit = 1
    for file in path.iterdir():
        if file.is_file() and not ext:
            Path(file).rename(
                f'{'' if not cut else str(file.stem)[cut[0]:cut[1]]}{file.stem if not new_name else new_name}'
                f'{sub_digit:0{digits}}{file.suffix if not new_ext else f".{new_ext}"}')
            sub_digit += 1
        elif file.is_file() and file.suffix[1:] == ext:
            Path(file).rename(
                f'{'' if not cut else str(file.stem)[cut[0]:cut[1]]}{file.stem if not new_name else new_name}'
                f'{sub_digit:0{digits}}{file.suffix if not new_ext else f".{new_ext}"}')
            sub_digit += 1




if __name__ == '__main__':
    extensions_in_directories(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7', bin=2, jpg=3, txt=1)
    extensions_in_directories(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7', bin=2, jpg=3, txt=1, mp3=5,
                              avi=2, mkv=3)
    sort_files(Path(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7'))
    rename_files(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task7', "po",3, 'txt', 'text',[0,2])
