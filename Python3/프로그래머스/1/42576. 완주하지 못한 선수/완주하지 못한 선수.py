def solution(participant, completion):
    # result = list(set(participant) - set(completion))
    # if result:
    #     return result[0]
    # else:
    #     return min(set(participant), key = completion.count)
    """이래서는 동명이인을 제대로 처리할 수 없음"""
    participant.sort()
    completion.sort()
    for num in range(len(completion)):
        if participant[num] != completion[num]:
            return participant[num]
    return participant[-1]
    