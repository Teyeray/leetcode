'''
描述：
给定一个由可见字符和空格组成的字符串，对其中的字母按以下规则排序，其他字符保持原位：
	1.	按字母表顺序排序（不区分大小写）；
	2.	同一字母的大小写同时存在时，保持它们在原字符串中的相对次序；
	3.	非字母字符不参与排序，且在结果中保留它们的原始位置。

输入：
	•	一个长度不超过 10⁵ 的字符串；
	•	字符范围为 ASCII 码 32 到 126（包含空格和可打印字符）。

输出：
	•	按上述规则排好序后的字符串
'''
A =['BabA'] #output: aABb
B = ['Hello Nowcoder!'] #output: CdeeH llNooorw!
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