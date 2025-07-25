# @nc app=nowcoder id=0e26e5551f2b489b9f58bc83aa4b6c68 topic=13 question=11155 lang=Python3
# 2025-07-25 16:39:30
# https://www.nowcoder.com/practice/0e26e5551f2b489b9f58bc83aa4b6c68?tpId=13&tqId=11155
# [JZ5] 替换空格

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def replaceSpace(self , s: str) -> str:
        # write code here
        res = ""
        ans = list(s)
        print(ans)
        for chr in ans:
            if chr != " ":
                res += chr
            else:
                res += "%20"
        return (res)

# @nc code=end
