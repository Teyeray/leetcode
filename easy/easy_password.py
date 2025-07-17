'''
密码变换规则描述：

小写字母变换规则：
参考九键手机键盘，将小写字母映射为对应数字：
abc → 2
def → 3
ghi → 4
jkl → 5
mno → 6
pqrs → 7
tuv → 8
wxyz → 9
大写字母变换规则：
先转换为小写字母，然后向后移动一位：
A → b
B → c
...
Y → z
Z → a
数字变换规则：
保持不变
输入要求：
长度为 1 ≤ length(s) ≤ 100 的字符串

输出要求：
变换后的字符串

测试用例：
输入：NowCoder123
输出：o69d6337123
'''
words = input().strip()
password = [[97,98,99],[100,101,102],[103,104,105],[106,107,108],
            [109,110,111],[112,113,114,115],[116,117,118],[119,120,121,122],
        ]
output = []
for word in words:
    word = ord(word)
    #是否为正常字符
    if 33 <= word <= 126:
        #判断是否在密码中
        is_printed = False
        for i in range(len(password)):
            if word in password[i]:
                #print(f'Character {word} is in password {i}')
                output.append(i+2)
                is_printed = True
        if not is_printed:
            if 65 <= word <= 90:
                if word == 90:
                    word = 97
                else:
                    word += 33
                output.append(chr(word))
                #print(f'Character{chr(word-33)} now is {chr(word)}')
            elif 48 <= word <= 57:
                output.append(chr(word))
                #print(f'Character {chr(word)} is a digit')
            #else:
                #print(f'Character {chr(word)} is illegal')
#print(f'output:{output}')
for chrs in output:
    print(chrs,end='')