import re
from typing import Dict, List


VALID_NUMBERS: Dict[str, str] = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}


def get_lines() -> List[str]:
    with open('Day 1/input.txt', 'r') as f:
        return f.readlines()


def main():
    total = 0
    for line in get_lines():
        pattern = re.compile(f'(?=([0-9]|{"|".join(VALID_NUMBERS.keys())}))')         
        strings = re.findall(pattern, line)
        int1 = VALID_NUMBERS.get(strings[0], strings[0])
        int2 = VALID_NUMBERS.get(strings[-1], strings[-1])
        result = int1 + int2
        total += int(result)
    print(total)



if __name__ == '__main__':
    main()  