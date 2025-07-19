A =['BabA']
B = ['Hello Nowcoder!']
data = [[] for _ in range(26)]
#line = [input().strip()]

line = A
for i in range(len(line[0])):
    if line[0][i].isupper():
        data[ord(line[0][i]) - ord('A')].append(1)
    elif line[0][i].islower():
        data[ord(line[0][i]) - ord('a')].append(0)
line = [x.lower() for x in line[0]]
#print(f'\nlower_line:{line}')
def filter(x): 
    return not ('A' <= x <= 'Z') and not ('a' <= x <= 'z')

line_symbol = [[i,x] for i,x in enumerate(line) if filter(x)]

#print(f'\nline_symbol:{line_symbol}')
for i in line_symbol:
    line.remove(i[1])
#print(f'\nremove_symbol_line: {line}')
line.sort()
#print(f'\nsorted line: {line}')
#print(f'\ndata: {data}')
count = 0
prev = ''
for i in range(len(line)):
    #print(f'line[i]: {line[i]}, prev: {prev}, count: {count}')
    if line[i] == prev:
        count += 1
        #print(f'ord(line[i]-ord(a)): {ord(line[i]) - ord("a")}')
    else:
        prev = line[i]
        count = 0
    if data[ord(line[i])-ord('a')][count] == 1:
        line[i] = line[i].upper()
    #print(f'-----{line[i]}')
for i in line_symbol:
    line.insert(i[0],i[1])
for chr in line:
    print(chr, end='')
#print(f'after {line}')