from random import choices, randint, randbytes
from string import ascii_lowercase, digits
from pathlib import Path

def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
              max_size: int = 4096, file_count: int = 42

              ):
    for _ in range(file_count):
        while True:
            name = f'{''.join((choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name))))}.{ext}'
            if not Path(name).is_file():
                with open(name, 'bw') as f:
                    f.write(randbytes(randint(min_size, max_size)))
                break


if __name__ == '__main__':
    gen_files('txt', file_count=5)
