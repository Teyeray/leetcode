import sys
def read_sentance(sentance: str):
    stack = []
    pairs = []
    for i , char in enumerate(sentance):
        #print(f'i:{i}, char:{char}')
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                left = stack.pop()
                pairs.append((left, i))
    return pairs

def cal_op(input_pairs:tuple, sentance:str):
    s = sentance[input_pairs[0]+1:input_pairs[1]].strip().split()
    op = s.pop(0)
    s = [int(x) for x in s]
    print(f'\ninput_pairs:{input_pairs}, s:{s}')
    if op == "add":
        res = s[0] + s[1]
    elif op == "sub":
        res = s[0] - s[1]
    elif op == "mul":
        res = s[0] * s[1]
    elif op == "div":
        if s[1] == 0:
            print(f'error')
            sys.exit()
        else:
            res = s[0] // s[1]
    else:
        print(f'error, wrong op:{op}')
    print(f'res:{res}')
    new_sentance = sentance[0:input_pairs[0]] + str(res) + sentance[input_pairs[1]+1:]
    return new_sentance

#read
sentance = input().strip()
#sentance = '(sub (mul 2 4) (div 9 3))'
print(f'-----------input:{sentance}--------------')
#cal pairs
pairs = read_sentance(sentance)

#do calculation
while len(pairs):
    pairs = read_sentance(sentance)
    new_sentance = cal_op(pairs.pop(0), sentance)
    sentance = new_sentance

print(f'{sentance}')