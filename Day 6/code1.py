import re
from typing import Iterable, Tuple, List


def get_data() -> Iterable[Tuple[int, int]]:
    with open('Day 6/input.txt', 'r') as f:
        time_str, dist_str = f.readlines()
        times, dists = get_ints(time_str), get_ints(dist_str)
        return zip(times, dists)


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
    product = 1
    for time, record in get_data():
        wins = get_wins(time, record)
        print(wins)
        product *= wins
    print(product)
         
    
if __name__ == '__main__':
    main()
