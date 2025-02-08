import sys
import heapq

def main():
    N = int(sys.stdin.readline().rstrip())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    n_set = set(n_list)
    
    n_list_sorted = []
    n_dict = dict()
    
    for n in n_set:
        heapq.heappush(n_list_sorted, n)
        
    for i in range(0, len(n_set)):
        x = heapq.heappop(n_list_sorted)
        n_dict[x] = f"{i}"
    
    target = []
    
    for n in n_list:
        target.append(n_dict[n])
    
    answer = " ".join(target)
    
    print(answer)

if __name__ == "__main__":
    main()
        
        
        
        
        
    