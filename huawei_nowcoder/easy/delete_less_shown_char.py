'''
对于给定的仅由小写字母构成的字符串，删除字符串中出现次数最少的字符。
输出删除后的字符串，字符串中其它字符保持原来的顺序。 
特别地，若有多个字符出现的次数都最少，则把这些字符都删除。
input:
abcccd
output:
ccc
'''
words = input().strip()
deduplicated = {}
for word in words:
    if word not in deduplicated:
        deduplicated[word] = 1
    else:
        deduplicated[word] += 1
min_value = min(deduplicated.values())
#print(f'deduplicated: {deduplicated}')
min_keys = [k for k, v in deduplicated.items() if v == min_value]
#delete min_keys from words
for word in words:
    #print(f'word {word} in min_keys: {word in min_keys}')
    if word not in min_keys:
        print(word, end="")
