from pathlib import Path
from random import choice, randint

MIN_VALUE = 4
MAX_VALUE = 7

vowels = 'eyuioa'
consonants = 'qwrtpsdfghjklzxcvbnm'


def gen_names(str_counts: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(str_counts):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                name += choice(consonants) if flag == 1 else choice(vowels)
                flag *= -1
            f.write(name.title() + '\n')


if __name__ == '__main__':
    gen_names(10, 'names.txt')
