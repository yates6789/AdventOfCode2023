from re import findall
from typing import Dict


VALID_NUMBERS: Dict[str, str] = {
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


def main():
    with open('Day 1/input.txt', 'r') as f:
        total = 0
        for line in f.readlines():
            pattern = '|'.join(VALID_NUMBERS.keys()) + '|' + r'[1-9]' 
            strings = findall(pattern, line)
            int1 = VALID_NUMBERS.get(strings[0], strings[0])
            int2 = VALID_NUMBERS.get(strings[-1], strings[-1])

            print(line.strip())
            print(strings)
            
            result = int1 + int2
            print(int1, int2, result)
            print()

            total += int(result)
        print(total)

if __name__ == '__main__':
    main()  