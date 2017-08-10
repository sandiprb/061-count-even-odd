def solution(list_of_nums):
    output = {
        'ODD': 0,
        'EVEN': 0
    }
    for n in list_of_nums:
        if n % 2 == 0:
            output['EVEN'] = output['EVEN'] + 1
        else:
            output['ODD'] = output['ODD'] + 1

    return output
