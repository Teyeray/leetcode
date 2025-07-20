#nums = input().strip().split(";")
#nums = ['2.3,3,5.6,7.6', '11,3,8.6,25,1', '0.3,9,5.3,66,7.8', '1,3,2,7,5', '340,670,80.6', '<=,<=,<=']
nums = ['2.36,3,6,7.1,6', '1,30,8.6,2.5,21', '0.3,69,5.3,6.6,7.8', '1,13,2,17,5', '340,67,300.6', '<=,>=,<=']
print(f'nums: {nums}')

def get_nums(nums):
    an = []
    xn = []
    bn = []
    symbols = nums[-1].split(",")
    n = len(symbols)
    for i in range(n):
        an.append(nums[i].split(","))
    xn = nums[-3].split(",")
    bn = nums[-2].split(",")
    return symbols, n, an, xn, bn

def symbols_code(input_symbol):
    if input_symbol == ">":
        return 0
    elif input_symbol == ">=":
        return 1
    elif input_symbol == "<":
        return 2
    elif input_symbol == "<=":
        return 3
    elif input_symbol == "=":
        return 4
    else:
        raise ValueError(f"Invalid symbol: {input_symbol}")

def convert_data(symbols, n, an, xn, bn, is_print=False):
    n = int(n)
    an = [list(map(float, a)) for a in an]
    xn = [int(x) for x in xn]
    bn = [float(b) for b in bn]
    symbols = [symbols_code(s) for s in symbols]


    if is_print:
        print(f'symbols: {symbols}')
        print(f'n: {n}')
        print(f'an: {an}')
        print(f'xn: {xn}')
        print(f'bn: {bn}')
    return symbols, n, an, xn, bn

def check_constraint_and_get_max(symbols, n, an, xn, bn):
    valid = True
    prev_max = int(-1e9)
    for i in range(n):
        res = 0
        n_curr = len(an[i])
        for j in range(n_curr):
            res = an[i][j]*xn[j] + res
            if j == n_curr - 1:
                res = res - bn[i]
                prev_max = max(prev_max, res)
                print(f'Constraint {i+1}: {an[i]} * {xn} - {bn[i]} = {res}')
                print(f'prev_max = max({prev_max}, {xn[j]}) = {prev_max}')
                if symbols[i] <= 1:
                        if res == 0 and symbols[i] == 0:
                            print(f'Constraint {i+1} is violated: {an[i]} * {xn} > {bn[i]}')
                            valid = False
                        elif res < 0:
                            print(f'Constraint {i+1} is violated: {an[i]} * {xn} > {bn[i]}')
                            valid = False
                elif symbols[i] <= 3:
                        if res == 0 and symbols[i] == 2:
                            print(f'Constraint {i+1} is violated: {an[i]} * {xn} < {bn[i]}')
                            valid = False
                        elif res > 0:
                            print(f'Constraint {i+1} is violated: {an[i]} * {xn} < {bn[i]}')
                            valid = False
                else:
                    if res != 0:
                        print(f'Constraint {i+1} is violated: {an[i]} * {xn} = {bn[i]}')
                        valid = False
    return valid, prev_max

symbols, n, an, xn, bn = convert_data(*get_nums(nums), is_print = True)
valid, max_xn = check_constraint_and_get_max(symbols, n, an, xn, bn)
if not valid:
    print(f'false,{int(max_xn)}')
else:
    print(f'true,{int(max_xn)}')