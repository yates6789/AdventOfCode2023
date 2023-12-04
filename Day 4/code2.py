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
            total_wins += 1
        return total_wins
        

def get_data() -> List[str]:
    with open('Day 4/input.txt', 'r') as f:
        return f.readlines()
    

def process_data(data: List[str]) -> List[Card]:
    cards: List[Card] = []
    for card in data:
        card = card.strip()
        ref = get_ref(card)
        card = card.replace(f'{ref}:', '')
        wins_str, nums_str = card.split('|')
        cards.append(
            Card(
                initial = card,
                ref     = ref,
                nums    = get_ints(nums_str),
                wins    = get_ints(wins_str)
            )
        )
    return cards
        

def get_ref(card: str) -> int:
    pattern = re.compile(r'\d+:')
    ref = re.findall(pattern, card)
    return int(re.findall(r'\d+', ref[0])[0])


def get_ints(string: str) -> List[int]:
    pattern = re.compile(r'\d+')
    return [int(num) for num in re.findall(pattern, string)]
    
    
def main():
    data = get_data() 
    cards = process_data(data) 

    copies: List[int] = [1 for _ in cards]
    for i, card in enumerate(cards):
        for j in range(card.total_wins()):
            copies[i + j + 1] += copies[i]   
    print(sum(copies))


if __name__ == '__main__':
    main()  