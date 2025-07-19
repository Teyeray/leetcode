'''
描述

对于给定的由小写字母和数字混合构成的字符串 s，你需要按每 8 个字符换一行的方式书写它，具体地：
- 书写前 8 个字符，换行；
- 书写接下来的 8 个字符，换行；
- ……
- 重复上述过程，直到字符串被完全书写。
特别地，如果最后一行不满 8 个字符，则需要在字符串末尾补充 0，直到长度为 8。

输入描述：

在一行上输入一个长度 1≦length(s)≦100，由小写字母和数字构成的字符串 s。

输出描述：

输出若干行，每行输出 8 个字符，代表按题意书写的结果。
'''
import sys

sentence = sys.stdin.readline()
sentence = sentence.strip()
sentence += ("0") * ((8 - len(sentence) % 8) % 8)
#print sentence in group of 8
for i in range(0, len(sentence), 8):
    print(f'{sentence[i:i+8]}')