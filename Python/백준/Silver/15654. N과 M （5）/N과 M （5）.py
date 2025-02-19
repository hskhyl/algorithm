import sys
from itertools import permutations

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    
    for permutation in permutations(num_list, M):
        print(*permutation)
    

if __name__ == "__main__":
    main()