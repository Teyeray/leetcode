# @nc app=nowcoder id=e69148f8528c4039ad89bb2546fd4ff8 topic=13 question=11206 lang=Python3
# 2025-08-06 18:48:35
# https://www.nowcoder.com/practice/e69148f8528c4039ad89bb2546fd4ff8?tpId=13&tqId=11206
# [JZ20] 表示数值的字符串

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return bool布尔型
#
class Solution:
    def isNumeric(self , str ):
        str = str.strip().lower()
        def is_decimal(s: str) -> bool:
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            idx = s.find('.')
            if idx == -1:
                return False
            if s[:idx] and s[idx + 1:]:
                return s[:idx].isdigit() and s[idx + 1:].isdigit()
            else:
                return s[:idx].isdigit() or s[idx + 1:].isdigit()
        def is_int(s: str) -> bool:
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            return s.isdigit()
        def is_scientific(s: str) -> bool:
            if 'e' in s:
                base, exp = s.split('e', 1)
                return (is_int(base) or is_decimal(base)) and is_int(exp)
            else:
                return is_int(s) or is_decimal(s)
        return is_scientific(str)
# @nc code=end
