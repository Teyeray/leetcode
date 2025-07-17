'''
你需要书写一个程序验证给定的密码是否合格。

合格的密码要求：

长度不少于8位
必须包含大写字母、小写字母、数字、特殊字符中的至少三种
不能分割出两个独立的、长度大于2的连续子串，使得这两个子串完全相同；更具体地，如果存在两个长度大于2的独立子串s1,s2，使得s1=s2，那么密码不合法。
说明：

子串为从原字符串中，连续的选择一段字符（可以全选、可以不选）得到的新字符串。
可见字符集为ASCII码在33到126范围内的可见字符（不包含空格、换行）。

021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
021Abc1111

output:

OK
NG
NG
OK
OK
'''
import sys
result = []
words = []
for line in sys.stdin:
    line = line.strip()
    #print(line.strip())
    words = []
    for word in line:
        #print(word)
        words.append(ord(word))
    #33-126, len>=8
    if (not 33 <= min(words) <= max(words) <=126) or (len(words) < 8):
        result.append('NG')
        print(f'words:{words},result:{result}')
        continue
    illegal = True
    count = [0,0,0,0]
    for word in words:
        print(f'sum:{sum(count)}')
        if sum(count) == 3:
            illegal = False
            break
        else:
            #数字
            if 47 <= word <= 57:
                count[1] = 1
            #大写字母
            elif 65 <= word <= 90:
                count[2] = 1
            #小写字母
            elif 97 <= word <= 122:
                count[3] = 1
            #符号
            else:
                count[0] = 1
    for j in range(len(words)-6):
        for i in range(j+3,len(words)-3):
            if words[j] == words[i]:
                if words[j+1] == words[i+1]:
                    if words[j+2] == words[i+2]:
                        print(f'{words[j:j+3]} == {words[i:i+3]}')
                        print("repeat")
                        illegal = True
                        break
    if illegal:
        result.append('NG')
    else:
        result.append('OK')
    print(f'words:{words},result:{result}')
for res in result:
    print(res)