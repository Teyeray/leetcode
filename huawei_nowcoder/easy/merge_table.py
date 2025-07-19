'''
题目描述：
给定一个数据表，第一行是一个整数 n (1 ≤ n ≤ 500)，代表数据记录数。
接下来的 n 行，每行包含两个整数 xi 和 yi：
  - xi：记录的索引，0 ≤ xi ≤ 11111111
  - yi：记录的数值，1 ≤ yi ≤ 10^5
要求：
  - 对于具有相同索引 xi 的多条记录，需将其 yi 数值相加合并为一条。
  - 输出合并后的记录，要求按 xi 升序排列。
  - 每行输出两个整数：索引 和 合并后的数值。

  
示例输入：
5
0 1
0 2
1 4
1 3
3 5
示例输出：
0 3
1 7
3 5
'''

import sys
lines = []
del_index = []
for line in sys.stdin:
    a = list(map(int, line.strip().split()))
    lines.append(a)
lines_len = int(lines.pop(0)[0])
lines.sort(key=lambda x: (x[0],x[1]))
prev = -1
for i in range(len(lines)):
    if prev != -1:
        if lines[i][0] == lines[prev][0]:
            lines[i][1] = int(lines[prev][1]) + int(lines[i][1])
            del_index.append(prev)
    prev = i
for i in sorted(del_index,reverse=True):
    del lines[i]
for line in lines:
    print(int(line[0]),int(line[1]),sep=' ')

