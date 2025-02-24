import sys
from itertools import permutations

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    
    combinations = permutations(num_list, M)
    previous = set()
    
    for combination in combinations:
        if combination not in previous:
            print(*combination)
            previous.add(combination)


if __name__ == "__main__":
    main()