'''
5
8
2
10
5
7
'''

# n = int(input().strip())
# pizza = [int(input().strip()) for _ in range(n)]


def get_max(n, pizza):
    #初始化
    dp = [[-1] * n for _ in range(n)]
    #print(f'dp_size:{len(dp)}x{len(dp[0])}')
    for i in range(n):
        dp[i][i] = pizza[i]
    #print(f'dp after init:{dp}')

    #从小到大计算
    for l in range(2, n + 1):
        for L in range(n - l + 1):
            candidates = []
            R = (L + l - 1)
            #取了左边
            if pizza[(L + 1)] > pizza[R]:
                next_L = (L + 2)
                next_R = R
            else:
                next_L = (L + 1)
                next_R = (R - 1)
            left = dp[next_L][next_R]
            if left != -1:
                candidates.append(pizza[L] + left)

            #取了右边
            if pizza[L] > pizza[(R - 1)]:
                next_L = (L + 1)
                next_R = (R - 1)
            else:
                next_L = L
                next_R = (R - 2)
            right = dp[next_L][next_R]
            if right != -1:
                candidates.append(pizza[R] + right)
            #print(f'L:{L}, R:{R}')
            dp[L][R] = max(candidates) if candidates else -1
    return dp[0][n-1]


# exp1
n = 5
pizza = [8, 2, 10, 5, 7]
print(f'pizza:{pizza}')

# exp2
# n = 7
# pizza = [2, 4, 6, 8, 10, 12, 14]
# print(f'pizza:{pizza}')


ans = 0
for i in range(n):
    pizza_curr = pizza[i:] + pizza[:i]
    ans = max(ans, get_max(n, pizza_curr))
print(f'max pizza:{ans}')