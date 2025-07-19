input = [[0,1,4,5,6,7],[1]]

array = input[0]
num = input[1]
print(f'array: {array}, num: {num},len(array): {len(array)}')

array_1 = []
array_2 = []
for i in range(len(array)):
    #print(f'array[{i}]: {array[i]}')
    if array[i] < 4:
        array_1.append(array[i])
    else:
        array_2.append(array[i])

def get_score(num, array):
    print(f'get_score -----num: {num}, array: {array}')
    score = 0
    result = []
    if len(array) == 0:
        return score, result
    
    if num == 1:
        if len(array) == 1:
            score = 4
        elif len(array) == 2:
            score = 3
        elif len(array) == 3:
            score = 2
        elif len(array) == 4:
            score = 1
        result = [[arr] for arr in array]
        return score, result
    elif num == 2:
        if len(array) == 2:
            score = 4
            result = [[array[0], array[1]]]
            return score, result
        elif len(array) == 4:
            score = 3
        elif len(array) == 3:
            score = 2
        elif len(array) == 1:
            return score, result
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                result.append([array[i], array[j]])
        return score, result
    elif num == 4:
        if len(array) == 4:
            score = 4
            result = [arr for arr in array]
            return score, result
    elif num == 8:
        score = -1
    else:
        print(f'num: {num} is not in [1,2,4,8]')
    return score, result

get_score_1, result_1 = get_score(num[0], array_1)
if get_score_1 != -1:
    get_score_2, result_2 = get_score(num[0], array_2)
    if get_score_1 > get_score_2:
        print(result_1)
    elif get_score_1 < get_score_2:
        print(result_2)
    else:
        print(result_1 + result_2)
else:
    if len(array_1) + len(array_2) == 8:
        print([[1, 2, 3, 4, 5, 6, 7, 8]])
print(f'array_1: {array_1},\n array_2: {array_2}')
