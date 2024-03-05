def solution(nums):
    select_num = int(len(nums)/2)
    print('select_num', select_num)
    spicy_num = len(set(nums))
    print('spicy_num', spicy_num)
    if spicy_num <= select_num:
        return spicy_num
    else:
        return select_num