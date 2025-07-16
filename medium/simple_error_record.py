"""
描述

在本题中，我们需要处理文件报错信息，其由出错文件的文件路径和错误行号组成。

文件路径的前三个字母为大写字母 A-Z、冒号 “:” 和反斜杠 “\”，代表盘符；随后是若干由小写字母构成的字符串，代表文件夹名，彼此使用单个反斜杠间隔。路径的最后一个反斜杠后是文件名。  
我们只在乎文件名（即去掉除了文件名以外的全部信息），且至多保留文件名的最后 16 个字符。

随后，我们需要统计相同的报错信息：  
∙ 如果两条报错信息保留后 16 个字符后的文件名相同，且行号相同，则视为同一个报错；  
∙ 相同的报错信息以第一次出现的时间为准，至多输出最后 8 条记录。

输入描述：

本题将会给出 1≦T≦100 条报错信息，确切数字未知，您需要一直读入直到文件结尾；您也可以参考 牛客网在线判题系统使用帮助 获得更多的使用帮助。  
每条报错信息描述如下：

在一行上先输入一个长度为 1≦length(x)≦100 的字符串 x，代表文件路径；随后，在同一行输入一个整数 y (1≦y≦1000) 代表行号。  
文件路径的格式如题干所述，保证文件名不为空。

输出描述：

至多八行，每行先输出一个长度为 1≦length(s)≦16 的字符串 s，代表文件名；随后，在同一行输出错误行号、报错次数。

示例1

输入：
D:\oblemsinnowcoder 12
D:\nowcoderproblemsinnowcoder 12
D:\nowcoder\problemsinnowcoder 13
D:\oj\problemsinnowcoder 13

输出：
oblemsinnowcoder 12 2
oblemsinnowcoder 13 2

说明：
在这个样例中，这四条报错信息去除文件路径后，由于文件名长度均超过 16 个字符，故我们只保留最后 16 个字符，得到的文件名均为 "oblemsinnowcoder"。所以，我们将它们看作同一个文件，按照报错行号划分即可。
"""

import sys
input =[
    r'A:\aa 1',
    r'B:\b 1',
    r'C:\c 1',
    r'D:\d 1',
    r'E:\e 1',
    r'F:\f 1',
    r'G:\g 1',
    r'H:\h 1',
    r'I:\i 1',
    r'A:\aa 1',
]
#for line in sys.stdin:
words = []
output = []
deduplicated_name = {}
#for word in input:
for word in sys.stdin:
    words = word.strip().split(sep=' ')
    file = words[0].split('\\')
    if len(file[-1]) >= 16:
        file_name = file[-1][-16:]
    else:
        file_name = file[-1]
    stop = False
    for group in output:
        if group[0] == file_name:
            if group[1] == words[1]:
                group[2] += 1
                stop = True
                break
    if stop == False:
        output.append([file_name, words[1], int(1)])
#print(f' {deduplicated_name}')
for group in output[-8:]:
    if group[1] != '0':
        print(*group,end='\n')
#print(f' {output}')

