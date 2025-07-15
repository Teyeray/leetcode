"""
描述

我们定义一个无限大的二维网格，上面有一个小人，小人初始位置为 (0,0) 点。小人可以读取指令上下左右移动。一个合法的指令由三至四个符号组成：
∙ 第一个符号为 "A/D/W/S" 中的一个，分别代表向左、向右、向上、向下移动；  
  记某个时刻小人的坐标为 (x,y)，向左移动一格即抵达 (x−1,y)，向右移动一格即抵达 (x+1,y)，向上移动一格即抵达 (x,y+1)，向下移动一格即抵达 (x,y−1)。  
∙ 中间为一个大于0且小于100的数字，代表小人移动的距离。特别地，如果这个数字小于10，那么它可能包含一个前导零，此时也视为合法。  
∙ 最后一个符号为 ';'，代表指令的结束，该符号固定存在。

遇到不合法的指令时则直接忽略；例如，"A100;" 不合法（数字100超出范围），"Y10;" 不合法（Y不是 A/D/W/S 中的方向）。

输入描述：

在一行上输入一个长度 1≤length(s)≤10⁴，由大写字母、数字和分号 (';') 构成的字符串 s，代表输入的指令序列。  
保证字符串中至少存在一个 ';'，且末尾一定为 ';'。

输出描述：

在一行上输出两个整数，代表小人最终位置的横纵坐标，使用英文逗号分隔。

示例 1

输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;

输出：
10,-10

说明：
- "A10;" 合法，向左10格，达到 (-10,0)  
- "S20;" 合法，向下20格，达到 (-10,-20)  
- "W10;" 合法，向上10格，达到 (-10,-10)  
- "D30;" 合法，向右30格，达到 (20,-10)  
- "X;"      不合法，忽略  
- "A1A;"    不合法，忽略  
- "B10A11;" 不合法，忽略  
- ";"       不合法，忽略  
- "A10;"    合法，向左10格，达到 (10,-10)

示例 2

输入：
ABC;AKL;DA1;D001;W023;A100;S00;

输出：
0,0

说明：全部指令均不合法，小人未移动。

示例 3

输入：
A00;S01;W2;

输出：
0,1

说明：
- "A00;" 合法（移动0格），位置仍为 (0,0)  
- "S01;" 合法，向下1格，达到 (0,-1)  
- "W2;"  合法，向上2格，达到 (0,1)
"""


position = [0, 0]
orders = input().strip().split(sep=';')
#print(orders)
for order in orders:
    if len(order) >=2 and order[0] in 'WASD':
        direction = order[0]
        distance = (order[1:])
        try:
            if distance[0] == '0':
                if len(distance) == 2 and distance[1] != '0':
                    distance = int(distance)
                else:
                    continue
            elif len(distance) == 1:
                distance = int(distance)
            elif len(distance) == 2:
                distance = int(distance)
            else:
                continue
        except ValueError:
            continue
        if direction == 'W':
            position[1] += distance
        elif direction == 'A':
            position[0] -= distance
        elif direction == 'S':
            position[1] -= distance
        elif direction == 'D':
            position[0] += distance
print(f'{position[0]},{position[1]}')
