#words = input().strip().split()
#words = ['abc', 'efghicbaiii']
words = ['abc', 'efghiccaiii']
print(words)
str1 = words[0]
str2 = words[1]
print(f'str1: {str1}, str2: {str2}')

def find_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        return -1
    for i in range(len2 - len1 + 1):
        print(f'Checking substring starting at index {i}: str2:{str2[i:i + len1]}, str1: {str1}')
        if set(str2[i:i + len1]) == set(str1):
            return i
    return -1

index = find_substring(str1, str2)
print(index)