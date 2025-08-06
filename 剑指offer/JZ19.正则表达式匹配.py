# @nc app=nowcoder id=28970c15befb4ff3a264189087b99ad4 topic=13 question=11205 lang=Python3
# 2025-08-06 17:19:29
# https://www.nowcoder.com/practice/28970c15befb4ff3a264189087b99ad4?tpId=13&tqId=11205
# [JZ19] 正则表达式匹配

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @param pattern string字符串 
# @return bool布尔型
#
class Solution:
    def match(self , str: str, pattern: str) -> bool:
        # write code here
        n, m = len(str) + 1, len(pattern) + 1
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        for j in range(1, m):
            if pattern[j - 1] == '*':
                print(f'j:{j} j-2:{j-2}')
                dp[0][j] = dp[0][j - 2]
        for i in range(1,n):
            for j in range(1, m):
                print(f'str:{str[i - 1]} pattern:{pattern[j - 1]}')
                if pattern[j - 1] == '*':
                    print(f'\n dp:{dp}')
                    dp[i][j] = dp[i][j - 2]
                    if pattern[j - 2] == str[i - 1] or pattern[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    if str[i - 1] == pattern[j - 1] or pattern[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        if dp[n - 1][m - 1] == 1:
            return True
        return False
# @nc code=end
