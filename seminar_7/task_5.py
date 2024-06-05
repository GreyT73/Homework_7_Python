from pathlib import Path
import os
from task_4 import gen_files


def extensions_in_directories(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, count in kwargs.items():
        gen_files(ext=ext, file_count=count)


if __name__ == '__main__':
    extensions_in_directories(r'C:\Users\Desktop\Learning\pythonProject1\seminar_7\task_4\new_dir', bin=2, jpg=3, txt=1)
