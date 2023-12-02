import re
from typing import Iterable, List

RED_MAX   = 12
GREEN_MAX = 13
BLUE_MAX  = 14


class Game:
    
    def __init__(self, initial: str, ref: int, red: int, green: int, blue: int):
        self.initial = initial
        self.ref     = ref
        self.red     = red
        self.green   = green
        self.blue    = blue


def get_data() -> List[str]:
    with open('Day 2/input.txt', 'r') as f:
        return f.readlines()
        

def get_ref(game: str) -> int:
    pattern = re.compile(r'Game \d+:')
    ref = re.findall(pattern, game)
    return int(re.findall(r'\d+', ref[0])[0])


def count_colour(game: str, colour: str) -> int:
    pattern = r'\d+(?= ' + colour + ')'
    numbers = re.findall(pattern, game)
    return max([int(num) for num in numbers])
     
        
def process_data(data: List[str]) -> Iterable[Game]:
    for game in data:
        yield Game(
            initial = game.strip(),
            ref     = get_ref(game),
            red     = count_colour(game, 'red'),
            green   = count_colour(game, 'green'),
            blue    = count_colour(game, 'blue'),
        ) 


def main():
    data = get_data()  
    total = 0  
    for game in process_data(data):
        if game.red > RED_MAX or game.green > GREEN_MAX or game.blue > BLUE_MAX:
            continue
        total += game.ref  
    print(total)
        

if __name__ == '__main__':
    main()  