'''
题目描述：
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但必须归还）。
小张手上有 n 个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。

输入规范：

输入包含 1 ≤ T ≤ 10 组测试数据
每组数据为一个整数 n (0 ≤ n ≤ 100) 表示空瓶数量
当 n = 0 时表示输入结束，无需处理该情况
输出规范：
对每组测试数据输出一个整数，表示最多可喝的汽水瓶数

测试用例：
输入：
3
10
81
0

输出：
1
5
40

样例解释：

第一组（n=3）：
3空瓶 → 兑换1瓶 → 喝完剩1空瓶 → 结束
总计：1瓶
第二组（n=10）：
第1轮：10空瓶 → 兑换3瓶 → 喝完剩4空瓶（10-3*3+3=4）
第2轮：4空瓶 → 兑换1瓶 → 喝完剩2空瓶（4-3+1=2）
第3轮：借1空瓶 → 3空瓶 → 兑换1瓶 → 喝完归还借的1空瓶 → 剩0空瓶
总计：3+1+1=5瓶
第三组（n=81）：
（计算过程略）
最终可得40瓶
'''
import sys

def check(input):
    if input < 3:
        if input == 2:
            return 1
        return 0
    remain = input % 3
    bottles = (input - remain) // 3
    #print(f'input:{input}, remain: {remain},bottles: {bottles}')
    return bottles + check(bottles + remain)


for line in sys.stdin:
    if int(line.strip()) == 0:
        break
    print(check(int(line.strip())))
