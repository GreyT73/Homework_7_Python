from pathlib import Path
from typing import TextIO

def read_or_start(fd: TextIO):
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def sum_files(f1: Path, f2: Path, results: Path)-> None:
    with open(f1, 'r', encoding='utf-8') as f1, \
        open(f2, 'r', encoding='utf-8') as f2, \
        open(results, 'a', encoding='utf-8') as results:
        len_f1 = sum(1 for _ in f1)
        len_f2 = sum(1 for _ in f2)
        for _ in range(max(len_f1, len_f2)):
            name = read_or_start(f1)
            numbers = read_or_start(f2).split(' | ')
            mult = int(numbers[0]) * float(numbers[1])
            results.write(f'{name.lower()} {-mult}\n') if mult < 0 else results.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    sum_files(Path('names.txt'), Path('numbers.txt'), Path("res.txt") )