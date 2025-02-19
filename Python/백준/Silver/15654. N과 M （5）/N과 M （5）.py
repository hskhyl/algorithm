import sys
from copy import deepcopy
from itertools import combinations

def generate_combination(N:int, M:int, num_list:list[int]):  
    visited = [False] * N
    result = [] 
        
    def back_track(depth):
        if depth == M:
            print(*result)
            return
    
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                result.append(num_list[i])
                back_track(depth + 1)
                result.pop()
                visited[i] = False
    
    back_track(0)
        
            

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    generate_combination(N, M, num_list)
    


if __name__ == "__main__":
    main()