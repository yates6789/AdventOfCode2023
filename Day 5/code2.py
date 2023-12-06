import re
from typing import List, Tuple


class Map:
    def __init__(self, initial: str, routes: List[Tuple[int, int, int]]):
        self.initial: str = initial
        self.routes: List[Tuple[int, int, int]] = routes

    def search(self, ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Optimised search that removes overlapping ranges. - this hurt me :'("""
        new_ranges: List[Tuple[int, int]] = []
        for dest, src, sz in self.routes:
            src_end: int = src + sz
            non_overlapping_ranges: List[Tuple[int, int]] = []
            while ranges:
                start, end = ranges.pop()
                before = (start, min(end, src))
                inter = (max(start, src), min(src_end, end))
                after = (max(src_end, start), end)
                if before[1] > before[0]:
                    non_overlapping_ranges.append(before)
                if inter[1] > inter[0]:
                    new_ranges.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    non_overlapping_ranges.append(after)
            ranges = non_overlapping_ranges
        return new_ranges + ranges


def get_data() -> List[str]:
    with open('Day 5/input.txt', 'r') as f:
        return f.read().split('\n\n')


def process_data(data: List[str]) -> List[Map]:
    maps: List[Map] = []
    for map_str in data:
        routes: List[Tuple[int, int, int]] = []
        for route_str in map_str.split('\n')[1:]:
            if route_str == '':
                continue
            dest, src, sz = get_ints(route_str)
            routes.append((dest, src, sz))
        maps.append(Map(map_str, routes))
    return maps


def get_ints(string: str) -> List[int]:
    return [int(x) for x in re.findall(r'\d+', string)]


def main() -> None:
    seeds_str, *data = get_data()
    maps = process_data(data)

    seeds = get_ints(seeds_str)
    result: List[int] = []
    for st, sz in zip(seeds[::2], seeds[1::2]):
        ranges: List[Tuple[int, int]] = [(st, st + sz)]
        for _map in maps:
            ranges = _map.search(ranges)
        result.append(min(ranges)[0])

    print(min(result))


if __name__ == "__main__":
    main()
