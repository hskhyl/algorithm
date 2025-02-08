import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # set을 사용하여 중복 제거 후 sorted()로 정렬
    sorted_unique_n_list = sorted(set(n_list))
    
    # 숫자에 대해 순위를 매기는 딕셔너리 생성
    n_dict = {n: str(i) for i, n in enumerate(sorted_unique_n_list)}
    
    # 원본 리스트에 대해 순위를 매기고 출력
    answer = " ".join(n_dict[n] for n in n_list)  # 여기서 n은 숫자, n_dict[n]은 숫자에 해당하는 순위
    
    print(answer)

if __name__ == "__main__":
    main()
