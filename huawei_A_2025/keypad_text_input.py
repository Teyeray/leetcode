'''
123#222235/56 input
123adjjm output
'''
def read_num(input_str: str) -> str:
    while "/" in input_str:
        i = input_str.index("/")
        input_str = input_str[:i] + input_str[i+1:]
    return input_str

def add_alphabet(input_str: str, count: int) -> str:
    str_map = [[], [',','.'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r','s'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z'], [' ']]
    idx = int(input_str)
    n = len(str_map[idx])
    return str_map[idx][count % n]

def read_alphabet(input_str: str) -> str:
    count = 0
    output = ''
    n = len(input_str)
    for i in range(1, n):
        curr = input_str[i]
        prev = input_str[i-1]
        #print(f'reading: {curr}')
        if prev == "/" and i != len(input_str) - 1:
            continue
        elif curr == "/" or curr != prev:
            if i-1 != -1:
                output += add_alphabet(prev, count)
                count = 0
                if i == n-1:
                    output += add_alphabet(curr, count)
        else:
            count +=1
            if i == n - 1:
                output += add_alphabet(curr, count)
    return output


def read_ins(input_list:list) -> list:
    output = []
    mode = -1
    for chrs in input_list:
        mode = -mode
        if mode == 1:
            output.append(read_num(chrs))
        if mode == -1:
            output.append(read_alphabet(chrs))
    return output

instruction = input().strip().split("#")

#exp1
#instruction = ['123', '222235/56']

output = read_ins(instruction)
print("".join(output))