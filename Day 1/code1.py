from re import findall

def main():
    with open('Day 1/input.txt', 'r') as f:   
        total = 0 
        for line in f.readlines():
            ints = findall(r'[1-9]', line)
            total += int(ints[0] + ints[-1])            
        print(total)        


if __name__ == '__main__':
    main()  