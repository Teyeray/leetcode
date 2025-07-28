# @nc app=nowcoder id=6e5207314b5241fb83f2329e89fdecc8 topic=13 question=11219 lang=Python3
# 2025-07-28 09:28:41
# https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219
# [JZ13] 机器人的运动范围

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param threshold int整型 
# @param rows int整型 
# @param cols int整型 
# @return int整型
#
class Solution:
    def movingCount(self , threshold: int, rows: int, cols: int) -> int:
        # write code here
        count = 0
        visited = set()
        def add_by_digit(num1, num2):
            list1 = list(map(int, list(str(num1))))
            list2 = list(map(int, list(str(num2))))
            return sum(list1) + sum(list2)
        def move(row, col):
            nonlocal count
            if (row, col) in visited or row >= rows or col >= cols:
                return 
            if add_by_digit(row, col) > threshold:
                return 
            print(f'row:{row}, col:{col},count:{count + 1}')
            count += 1
            visited.add((row,col))
            move(row + 1, col)
            move(row, col + 1)
        move(0, 0)
        return count

# @nc code=end
