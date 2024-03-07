def solution(clothes):
    length = len(clothes)
    clothes_num_dict = dict()
    for index in range(length):
        key = clothes[index][-1]
        clothes_num_dict.setdefault(key, 1)
        clothes_num_dict[key] += 1


    kind = list(clothes_num_dict.values())
    result = 1

    for i in kind:
        result *=i

    result = result - 1
    return(result)