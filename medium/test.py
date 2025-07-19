import sys

lines = []
# for line in sys.stdin:
#     line = line.strip().split()
#     lines.append(line)
lines = [['31'], ['32', '01', '00', 'AE', '90', '02', '00', '01', '02', '30', '03', '00', 'AB', '32', '31', '31', '02', '00', '32', '33', '33', '01', '00', 'CC']]

tag = lines.pop(0)[0]
lines = [x for x in lines[0]]

print(f'tag: {tag}, lines: {lines}')

def read_word(input_lines, input_tag):
    count = 0
    mode = 0
    find = False
    value = []
    is_count = False
    for word in input_lines:
        if mode == 2:
            if count != length:
                if find:
                    value.append(word)
                count += 1
                continue
            else:
                if find:
                    return value
                mode = 0
                count = 0
        if mode == 1:
            if not is_count:
                length2 = word
                is_count = True
                continue
            else:
                length1 = word
                is_count = False
                length = int((length1 + length2), 16)
                print(f'length_16: {length1 + length2} ,length: {length}')
                mode = 2
                continue
        if mode == 0:
            tag_now = word
            mode = 1
            if tag_now == input_tag:
                find = True
            continue

value = read_word(lines,tag)
print(f'value: {value}')
        
            

