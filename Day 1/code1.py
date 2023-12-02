import re
from typing import List


def get_lines() -> List[str]:
    with open('Day 1/input.txt', 'r') as f:
        return f.readlines()


def main():
    total = 0 
    for line in get_lines():
        ints = re.findall(r'[1-9]', line)
        total += int(ints[0] + ints[-1])            
    print(total)        


if __name__ == '__main__':
    main()  