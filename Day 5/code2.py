import re
from typing import List, Set


class Route: 
    
    def __init__(self, dst_start: int, src_start: int, length: int):
        self.dst_start = dst_start
        self.src_start = src_start
        self.length    = length
        

class Map:
    
    def __init__(self, initial: str, routes: List[Route]):
        self.initial = initial
        self.routes  = routes

    def search(self, start: int) -> int:
        for route in self.routes:
            delta = start - route.src_start
            if delta in range(route.length):
                return route.dst_start + delta
        return start


def get_data() -> List[str]:
    with open('Day 5/input.txt', 'r') as f:
        return f.read().split('\n\n')


def process_data(data: List[str]) -> List[Map]:
    maps: List[Map] = []
    for map_str in data:
        routes: List[Route] = []
        for route_str in map_str.split('\n')[1:]:
            dst_start, src_start, length = get_ints(route_str)
            routes.append(Route(dst_start, src_start, length))
        maps.append(Map(map_str, routes))
    return maps


def get_ints(string: str) -> List[int]:
    return [int(x) for x in re.findall(r'\d+', string)]
    

def get_seeds(seeds_str: str) -> Set[int]:
    seed_data = get_ints(seeds_str)
    seeds: Set[int] = set()
    for i in range(0, len(seed_data), 2):
        start, length = seed_data[i], seed_data[i + 1]
        seeds.update(range(start, start + length))
    return seeds


def main():
    seeds_str, *data = get_data()
    maps = process_data(data)
    seeds = get_seeds(seeds_str)
    
    print(f'{len(seeds)}: have mercy on my soul')
    
    results: List[int] = []
    for seed in set(seeds):
        result = seed
        for _map in maps:
            result = _map.search(result)
        results.append(result)
    result = min(results)
    
    print(result)
     
    
if __name__ == '__main__':
    main()
