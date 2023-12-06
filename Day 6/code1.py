import re
from typing import Iterable, Tuple, List


def get_data() -> Tuple[int, int]:
    with open('Day 6/input.txt', 'r') as f:
        time_str, dist_str = f.readlines()
        time = int(''.join([x for x in re.findall(r'\d+', time_str)]))
        dist = int(''.join([x for x in re.findall(r'\d+', dist_str)]))
        return time, dist


def get_ints(string: str) -> List[int]:
    return [int(x) for x in re.findall(r'\d+', string)]


def displacement(time: int, limit: int) -> float:
    return (limit - time) * time


def get_wins(limit: int, record: int) -> int:
    wins: int = 0
    for time in range(limit):
        if displacement(time, limit) > record:
            wins += 1
    return wins

    
def main():
    time, record = get_data()
    wins = get_wins(time, record)
    print(wins)
         
    
if __name__ == '__main__':
    main()
