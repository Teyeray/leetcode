#n = int(input().strip())
i = 0
lines = []
# while i < 2 * n:
#     line = input().strip().split()
#     lines.append(line)
#     i += 1

#exp1
n = 5
lines = [['head', 'add', '1'], ['tail', 'add', '2'], ['remove'], 
        ['head', 'add', '3'], ['tail', 'add', '4'], ['head', 'add', '5'], 
        ['remove'], ['remove'], ['remove'], ['remove']]

def remove(lis:list, is_order, sort_num):
    if len(lis) == 0:
        return lis, is_order, sort_num
    if not is_order:
        sort_num += 1
        is_order = True
    lis.pop()
    return lis, is_order, sort_num

def get_instruction(x:list, lis:list, is_order, sort_num):
    print(f'get instruction:{x},current_lis:{lis}')
    if len(x) == 3:
        print(f'x[0]:{x[0]}')
        if x[0] == 'head':
            if len(lis) != 0 and is_order:
                is_order = False
            lis.insert(0, int(x[2]))
        elif x[0] == 'tail':
            lis.append(int(x[2]))
    else:
        lis, is_order, sort_num = remove(lis, is_order, sort_num)
    return lis, is_order, sort_num

sort_num = 0
lis = []
is_order = True
print(f'lines:{lines}')
for line in lines:
    print(f'line:{line}')
    lis, is_order, sort_num = get_instruction(line, lis, is_order, sort_num)

print(f'lis:{lis}, sort_num:{sort_num}')