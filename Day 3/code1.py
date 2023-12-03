import re
from typing import Iterable, List, Tuple


def get_data() -> List[str]:
    with open('Day 3/input.txt', 'r') as f:
        return f.readlines()
        
        
def get_lines(data: List[str]) -> Iterable[Tuple[str | None, str, str | None]]:
    for i, line in enumerate(data):
        yield (
            data[i - 1].strip() if i > 0 else None,
            line.strip(),
            data[i + 1].strip() if i < len(data) - 1 else None,
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


def eval_line(line: str | None, indexes: List[int]) -> bool:
    if not line:
        return False
    return any([eval_char(line[i]) for i in indexes])


def main():
    data = get_data()  
    
    total = 0
    for lower, line, upper in get_lines(data):
        for match in re.finditer(r'\d+', line):
            value = int(match.group())
            indexes = get_indexes(match)
            
            if eval_line(lower, indexes):
                total += value
                continue
                        
            if eval_line(line, indexes):
                total += value
                continue
                
            if eval_line(upper, indexes):
                total += value
                continue
            
    print(total)
             

if __name__ == '__main__':
    main()  