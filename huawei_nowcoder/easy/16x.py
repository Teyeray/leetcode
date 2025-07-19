'''
描述：
将一个十六进制数转换为十进制数
输入：
一个十六进制数，字符串形式，长度不超过1000
输出：  
一个十进制数，整数形式
''' 

import sys

ans = 0
data16 = '0123456789ABCDEF'
num = sys.stdin.readline().strip()
for i in range(0,len(num)-2):
    for j in range(0,len(data16)):
        if data16[j] == num[-i-1]:
            #print(f'\nnum:{num[-i]}\ndata16{data16[j]}\nans:{(j+1)*16**(i)}')
            ans += j*16**(i)
print(ans)