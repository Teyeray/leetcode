'''
描述

对于给定的由大小写字母、数字和空格混合构成的字符串 s，给定字符 c，按要求统计： 
∙ 若 c 为大写或者小写字母，统计其大小写形态出现的次数和；
∙ 若 c 为数字，统计其出现的次数。

保证字符 c 要么为字母、要么为数字。 输入描述：

第一行输入一个长度 1≦length(s)≦10^3，由大小写字母、数字和空格构成的字符串 s。保证首尾不为空格。 
第二行输入一个字符 c，保证 c 为大小写字母或数字。 

输出描述：
在一行上输出一个整数，代表统计结果。
'''
import sys

words=[]
count=0
for line in sys.stdin:
    line = line.strip()
    words.extend(line.split())
last_char = words[-1].lower()
#print(f'lines: {words}]\n')
for line in words[:-1]:
    #print(f'\nline:{line}\n')
    #print(f'line.split: {line.split()}\n')
    for word in line.split():
        #print(f'{word}\n')
        for character in word:
            if character.lower()==last_char.lower():
                count +=1
print(count)
