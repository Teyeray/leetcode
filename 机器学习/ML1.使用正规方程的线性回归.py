# @nc app=nowcoder id=c497c2c49ea843898731bb14accc04ac topic=379 question=11118311 lang=Python3
# 2025-07-25 11:10:06
# https://www.nowcoder.com/practice/c497c2c49ea843898731bb14accc04ac?tpId=379&tqId=11118311
# [ML1] 使用正规方程的线性回归

# @nc code=start

import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # 实现代码

if __name__ == "__main__":
    import ast
    x = np.array(ast.literal_eval(input()))
    y = np.array(ast.literal_eval(input())).reshape(-1, 1)

    # Perform linear regression
    coefficients = linear_regression_normal_equation(x, y)

    # Print the coefficients
    print(coefficients)


# @nc code=end
