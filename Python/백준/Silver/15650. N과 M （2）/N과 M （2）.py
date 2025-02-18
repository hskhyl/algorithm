import sys
from itertools import combinations

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    results = None
    results = combinations(range(1, n + 1), m)
    
    for combination in results:
        print(' '.join(map(str, combination)))
    


if __name__ == "__main__":
    main()