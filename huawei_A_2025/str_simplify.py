def get_str(strs:list):
    start = 0
    output = []
    equal = []
    for chr in strs[0]:
        if chr == "(" and start == 0:
            curr = []
            start = 1
            continue
        elif start == 0:
            output.append(chr)
            continue
        elif start == 1:
            if chr == ")":
                if len(curr) > 1:
                    equal.append(curr)
                    start -=1
                    continue
                else:
                    start -=1
                    continue
            else:
                curr.append(chr)
                continue
    n = len(equal)
    i = n - 2 
    while i >= 0:
        set_1 = set(equal[i])
        set_2 = set(equal[i+1])
        if set_1.intersection(set_2) is not None:
            equal[i] = [j for j in set_1 | set_2]
            equal[i].sort(key = lambda x: ord(x))
            del equal[i+1]
        i -= 1
    return output, equal

def change_word(input_list: list, settings: list) -> list:
    for i in range(len(input_list)):
        for equ in settings:
            if input_list[i] in equ:
                input_list[i] = equ[0]
    return input_list



strs = input().strip().split()

#exp1
# strs = ['never(dont)give(run)up(f)()']
output = change_word(*get_str(strs))
if len(output) != 0:
    print(f'{"".join(output)}')
else:
    print('0')