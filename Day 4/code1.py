import re
from typing import Iterable, List


class Card:
    
    def __init__(self, initial: str, ref: int, nums: List[int], wins: List[int]):
        self.initial = initial
        self.ref     = ref
        self.nums    = nums
        self.wins    = wins

    def total_wins(self) -> int:
        total_wins = 0
        for num in self.nums:
            if num not in self.wins:
                continue
            if total_wins == 0:
                total_wins = 1
            else:
                total_wins *= 2            
        return total_wins
        

def get_data() -> List[str]:
    with open('Day 4/input.txt', 'r') as f:
        return f.readlines()
    

def process_data(data: List[str]) -> Iterable[Card]:
    for card in data:
        card = card.strip()
        ref = get_ref(card)
        card = card.replace(f'{ref}:', '')
        wins_str, nums_str = card.split('|')
        yield Card(
            initial = card,
            ref     = ref,
            nums    = get_ints(nums_str),
            wins    = get_ints(wins_str)
        ) 
        

def get_ref(card: str) -> int:
    pattern = re.compile(r'\d+:')
    ref = re.findall(pattern, card)
    return int(re.findall(r'\d+', ref[0])[0])


def get_ints(string: str) -> List[int]:
    pattern = re.compile(r'\d+')
    return [int(num) for num in re.findall(pattern, string)]
    
    
def main():
    data = get_data()  
    total = 0
    for card in process_data(data):
        total += card.total_wins()
    print(total)
             

if __name__ == '__main__':
    main()  