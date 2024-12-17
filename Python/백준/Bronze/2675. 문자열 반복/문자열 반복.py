import sys
num = int(input())

for _ in range(num):
    line = sys.stdin.readline().strip().split()
    number = int(line[0])
    string = line[1]
    answer = ""
    for s in string:
        answer += s*number
    print(answer)
    
