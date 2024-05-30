def solution(arr):
    answer = [arr[0]]
    for number in arr:
        if answer[-1] != number:
            answer.append(number)
    return answer