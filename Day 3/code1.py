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


def eval_char(char: str) -> bool:
    if char.isdigit():
        return False
    if char == ".":
        return False
    return True


def main():
    data = get_data()  
    
    total = 0
    for lower, line, upper in get_lines(data):
        for match in re.finditer(r'\d+', line):
            value = int(match.group())
            indexes = get_indexes(match)
            
            if lower:
                if any([eval_char(lower[i]) for i in indexes]):
                    total += value
                    continue
                        
            if any([eval_char(line[i]) for i in indexes]):
                total += value
                continue
                
            if upper:
                if any([eval_char(upper[i]) for i in indexes]):
                    total += value
                    continue
            
    print(total)
             

if __name__ == '__main__':
    main()  