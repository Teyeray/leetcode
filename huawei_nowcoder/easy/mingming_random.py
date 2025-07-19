'''
描述

对于明明生成的 n 个 1 到 500 之间的随机整数，你需要帮助他完成以下任务：
- 删去重复的数字，即相同的数字只保留一个，把其余相同的数去掉；
- 然后再把这些数从小到大排序，按照排好的顺序输出。
你只需要输出最终的排序结果。

输入描述：

第一行输入一个整数 n (1≦n≦1000)，代表明明生成的数字个数。
此后 n 行，第 i 行输入一个整数 a_i (1≦a_i≦500)，代表明明生成的随机整数。

输出描述：

输出若干行，每行输出一个整数，代表输入数据排序后的结果。第一行输出最小的数字。
'''
import sys

numbers = [int(line.strip()) for line in sys.stdin]
# print(f'\nnumbers: {numbers}')
size = numbers.pop(0)
# print(f'size: {size}\n len: {len(numbers)}\n')
if size == len(numbers):
    #print("\n\n\n-----\n")
    sorted_number = sorted(numbers)
    print(sorted_number[0])
    prev = sorted_number[0]
    for i in sorted_number[1:]:
        if prev is not None:
            if i == prev:
                continue
            else:
                print(i)
        prev = i
