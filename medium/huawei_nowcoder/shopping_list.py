"""
描述

王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件。
∙ 主件可以没有附件，至多有 2 个附件。附件不再有从属于自己的附件。
∙ 若要购买某附件，必须先购买该附件所属的主件，且每件物品只能购买一次。

王强查到了 m 件物品的价格，而他只有 n 元的预算。为了先购买重要的物品，他给每件物品规定了一个重要度，用整数 1~5 表示。他希望在不超过预算的前提下，使满意度最大。

满意度定义为所购每件物品价格与重要度乘积之和。具体地说，记第 i 件物品的价格为 v_i,重要度为 w_i;若共选中 k 件物品，编号为 j₁, j₂, …, j_k,则满意度计算为:

  ∑_{t=1}^k (v_{j_t} x w_{j_t})
  
请你帮助王强计算可获得的最大的满意度。

输入描述：

第一行输入两个整数 n, m (1 ≤ n ≤ 3x10⁴; 1 ≤ m ≤ 60)  
n, m 分别代表预算和查询到的物品总数。  
此后 m 行，第 i 行输入三个整数 v_i, w_i, q_i  
(1 ≤ v_i ≤ 10⁴; 1 ≤ w_i ≤ 5; 0 ≤ q_i ≤ m)  
分别代表第 i 件物品的价格、重要度、主件编号。特别地,q_i = 0 代表该物品为主件，否则表示该附件从属于主件 q_i。编号即输入顺序,从 1 开始。  
保证所有物品的价格 v_i 均为 10 的倍数；且每个主件的附件数不超过 2 个。

输出描述：

在一行上输出一个整数，代表王强可获得的最大满意度。

示例 1:

输入：
50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0

输出：
130

说明：

在这个样例中，第三、四、五件物品为主件，第一、二件物品为第五件物品的附件。这就意味着，如果购买了第一件物品或第二件物品，则必须购买第五件物品；但若同时购买第一件和第二件附件，也只需购买一次第五件主件。最佳方案是购买第 1、2、5 件商品，满意度为：

20 x 3 + 20 x 3 + 10 x 1 = 130
"""

import sys
main = []
accessories = []
first = 0

for line in sys.stdin:
    if first == 0:
        first_line = list(map(int,line.strip().split()))
        first = 1
        continue
    else:
        a = line.split()
        a = list(map(int, a))
        a[0] = a[0]//10
        a.append(first)
        first +=1
        if a[2] == 0:
            main.append(a)
        else:
            accessories.append(a)
budget = first_line[0]//10
count = first_line[1]
print(f'budget: {budget},count:{count},first:{first} main: {main}, accessories: {accessories}')
total = 0
satisfaction = [0]*(budget+1)
result = []
if count == first-1:
    for i in range(len(main)):
        for j in range(budget,main[i][0]-1,-1):
            satisfaction[j] = max(satisfaction[j],satisfaction[j-main[i][0]]+(main[i][0]*main[i][1]))

            current_main_id = main[i][3]
            matches = filter(lambda x: x[2] == current_main_id, accessories)
            pick_first = next(matches, None)
            pick_second = next(matches, None)
            if pick_first and j >= main[i][0] + pick_first[0]:
                satisfaction[j] = max(satisfaction[j], satisfaction[j-main[i][0]-pick_first[0]] + main[i][0]*main[i][1] + pick_first[0]*pick_first[1])
            if pick_second and j >= main[i][0] + pick_second[0]:
                satisfaction[j] = max(satisfaction[j], satisfaction[j-main[i][0]-pick_second[0]] + main[i][0]*main[i][1] + pick_second[0]*pick_second[1])
            if pick_first and pick_second and j >= main[i][0] + pick_first[0] + pick_second[0]:
                satisfaction[j] = max(satisfaction[j], satisfaction[j-main[i][0]-pick_first[0]-pick_second[0]] + main[i][0]*main[i][1] + pick_first[0]*pick_first[1] + pick_second[0]*pick_second[1])
    print(f'satisfaction: {satisfaction}')
    result.append(max(satisfaction))
else:
     print("invalid, count does not match the number")
print(max(satisfaction)*10)
