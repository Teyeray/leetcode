"""
描述：
    对于给定的整数 n，从小到大依次输出它的全部质因子。
    即找到一组质数 p₁, p₂, ⋯, pₖ，使得 n = p₁ × p₂ × ⋯ × pₖ。

输入描述：
    在一行上输入一个整数 n (2 ≤ n ≤ 2 × 10^9 + 14)，代表待分解的整数。

输出描述：
    在一行上从小到大输出若干个整数，代表 n 的质因子。
"""

import sys

num = int(sys.stdin.readline().strip())
ans = ""
def fun1(input_num,fun_ans):
    #print(f'now calculating:{input_num}')
    for i in range(2,int(input_num**0.5)+1):
        if input_num % i == 0:
            fun_ans += f'{i} '
            input_num //= i
            return fun1(input_num,fun_ans)
    fun_ans += f'{input_num}'
    return fun_ans
ans1 = fun1(num,ans)
print(ans1)