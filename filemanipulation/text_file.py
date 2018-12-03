import random
import string
import sys
from tqdm import tqdm


def text_file():
    num_lines = 1000000
    rand_low = 30
    rand_high = 60
    chars = string.ascii_letters + ' '
    filename = 'text_file.txt'
    f = open(filename, 'w')
    if len(sys.argv) != 1:
        num_lines = int(sys.argv[1])
    for i in tqdm(range(num_lines)):
        rand_text = ''.join(random.choices(chars, k=random.randint(rand_low, rand_high)))
        f.write(f'{i+1}: ' + rand_text + ' |\n')
    f.close()


if __name__ == '__main__':
    text_file()
