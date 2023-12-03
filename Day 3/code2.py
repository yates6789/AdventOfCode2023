import re
from typing import Iterable, List, Tuple


def get_data() -> List[str]:
    with open('Day 3/input.txt', 'r') as f:
        return f.readlines()


def get_lines(data: List[str]) -> Iterable[Tuple[str | None, str, str | None]]:
    for index, line in enumerate(data):
        yield (
            data[index - 1].strip() if index > 0 else None,
            line.strip(),
            data[index + 1].strip() if index < len(data) - 1 else None,
        )


def get_indexes(match: re.Match[str]) -> List[int]:
    indexes = list(range(*match.span()))

    if indexes[0] != 0:
        indexes.insert(0, indexes[0] - 1)
        
    if indexes[-1] != len(match.string) - 1:
        indexes.append(indexes[-1] + 1)
        
    return indexes


def get_values(line: str | None, indexes_g: List[int]) -> List[int]:
    if not line:
        return []
    
    values: List[int] = []
    for match_p in re.finditer(r'\d+', line):
        indexes_p = get_indexes(match_p)
        if indexes_p[0] < indexes_g[-1] and indexes_p[-1] > indexes_g[0]:
            values.append(int(match_p.group()))
    return values


def main():
    data = get_data()  
    total = 0
    
    for lower, line, upper in get_lines(data):
        for match_g in re.finditer(r'\*', line):
            indexes_g = get_indexes(match_g)
                
            lower_values = get_values(lower, indexes_g)
            line_values = get_values(line, indexes_g)
            upper_values = get_values(upper, indexes_g)     

            values = [*lower_values, *line_values, *upper_values]
            for i, x in enumerate(values):
                for y in values[i+1:]:
                    total += x * y
        
    print(total)


if __name__ == '__main__':
    main()