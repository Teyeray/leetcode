def get_extreme_after_i(idx, mode, input_list):
    n = len(input_list)
    max_v = max(input_list)
    if mode == 1:
        high = 0
        for i in range(idx,n):
            curr = input_list[i]
            if curr < high:
                return high, i-1
            else:
                high = curr
                continue
        return high, i
    else:
        low = max_v + 1
        for i in range(idx, n):
            curr = input_list[i]
            if curr > low:
                return low, i-1
            else:
                low = curr
                continue
        return low, i
    
def get_data():
    number = int(input().strip())
    days = int(input().strip())
    item = []
    item.extend(list(map(int, input().strip().split())))
    price = []
    i = 0
    while i < number:
        price.append(list(map(int, input().strip().split())))
        i += 1
    print(f'number:{number}, days:{days}, item:{item}, price:{price}')
    return number, days, item, price

def get_pair(price):
    mode = 1
    result = []
    n = len(price)
    idx = 0
    profit = 0
    while idx < n-1:
        mode = -mode
        value, idx = get_extreme_after_i(idx, mode, price)
        if idx != number - 1:
            result.append((value,idx))
            mode = -mode
            value1 = value
            value, idx = get_extreme_after_i(idx, mode, price)
            result.append((value, idx))
            profit += value - value1
    return result, profit

number, days, item, price = get_data()

#exp1
# number = 3
# days = 3
# item = [4, 5, 6]
# price = [[1, 2, 3], [4, 3, 2], [1, 5, 2]]

result = [[] for _ in range(number)]
money = 0
for i in range(number):
    result[i], profit = get_pair(price[i])
    print(f'profit[{i}]:{profit}')
    money += profit * item[i]
print(f'result{result}\n')
print(f'{money}')