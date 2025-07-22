n = int(input().strip())
grid = list(map(int, input().strip().split()))
k = int(input().strip())

'''
n:10, 
scores:[6, -6, -10, 7, 14, -99, 15, -80, -69, 4], 
k:4
46
'''
#exp1
# n = 6
# grid = [1, -1, -6, 7, -17, 7]
# k = 3

# #exp2
# n = 10
# grid = [6, -6, -10, 7, 14, -99, 15, -80, -69, 4] 
# k = 4

dp = grid[:]
#print(f'dp:{dp}')
for i in range(1, n):
    dp[i] = dp[i] + dp[i - 1]

for i in range(2, k+1):
    for j in range(1, n):
        #print(f'i:{i}, j:{j}')
        if j-i >= 0:
            dp[j] = max(dp[j-i : j]) + grid[j]
        else:
            dp[j] = max(dp[0 : j]) + grid[j]
        #print(f'\ni:{i}, j:{j},dp:{dp}\n')

#print(f'n:{n}, grid:{grid}, k:{k}, dp:{dp}')
print(dp[-1])