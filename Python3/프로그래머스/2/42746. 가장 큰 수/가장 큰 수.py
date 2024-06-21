def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(str_numbers)))
    