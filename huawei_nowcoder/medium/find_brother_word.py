'''
定义一个字符串 s 的“兄弟单词”
为：将 
s 重新排序后得到的与原字符串不同的新字符串。
现在，对于给定的 n 个字符串和另一个单独的字符串 x，你需要解决两个问题：
∙统计这n 个字符串中，有多少个是 x 的“兄弟单词”（注意，这 n 个字符串可能有重复，重复字符串分别计数）；
∙将这 n 个字符串中 x 的“兄弟单词”按字典序从小到大排序，输出排序后的第 k 个兄弟单词（从 1 开始计数）。
特别地，如果不存在，则不输出任何内容。
【名词解释】
从字符串的第一个字符开始逐个比较，直至发现第一个不同的位置，比较这个位置字符的字母表顺序，字母序较小的字符串字典序也较小；如果比较到其中一个字符串的结尾时依旧全部相同，则较短的字符串字典序更小。
'''

A = ['3','abc','abc','bca','cab','abc','1'] #output: 2 bca



def find_brother_word():
    return
