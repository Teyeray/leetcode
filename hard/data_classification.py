
'''
描述
信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、QQ 用户、手机号码、银行帐号等信息及活动记录。采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

对于给定的分类规则集 R={R₁,R₂,…,Rₘ}，先对其进行规范化：
	1.	将 R 中的整数按从小到大的顺序重新排序；
	2.	去除 R 中的重复元素；
得到规范化后的规则集 r={r₁,r₂,…,rₖ}。

然后，对收集到的整数数据集 I={I₀,I₁,…,Iₙ₋₁}，使用规则集 r 进行分类：
	•	对于每条规则 rᵢ，如果 I 中存在将 rᵢ 作为连续子串的数字，则该规则有效；
	•	统计所有符合该规则的数据条数 p；
	•	记录每条符合的记录在 I 中的下标 id（从 0 开始）及其值 I_id；
	•	如果某条规则无效，则跳过。

“连续子串”指将整数视为字符串后，连续选取一段字符。如 “123” 是 “47912398” 的连续子串，但 “139” 不是。

输入描述
第一行：整数 n (1≤n≤100)，后接 n 个整数 I₀, I₁, …, Iₙ₋₁ (0≤Iᵢ<2³¹)，表示数据集 I。
第二行：整数 m (1≤m≤100)，后接 m 个整数 R₁, R₂, …, Rₘ (0≤Rᵢ<2³¹)，表示原始规则集 R。

输出描述
在一行内输出以下数字，总数记作 k：
	1.	首先输出 k，本题中即后续所有数字的总数量；
	2.	对于规范化后的每条有效规则 rᵢ，依次输出：
	•	规则值 rᵢ
	•	符合该规则的数据条数 p
	•	p 对二元组 id I_id（共 2p 个数字），分别表示符合规则的数据在 I 中的位置 id 及该位置上的数值 I_id。
无效规则不产生任何输出。

示例输入
15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123
5 6 3 6 3 0

示例输出
30 3 6 0 123 3 453 7 3 9 453456 13 453 14 123 6 7 1 456 2 786 4 46 8 665 9 453456 11 456 12 786

说明
原始数据集 I={123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123}，原始规则集 R={6,3,0}。
规范化后 r={0,3,6}。
	•	规则 0：在 I 中无任何数字包含子串 “0”，跳过。
	•	规则 3：符合子串 “3” 的记录有
I₀=123, I₃=453, I₇=3, I₉=453456, I₁₃=453, I₁₄=123 共 6 条，
输出 “3 6 0 123 3 453 7 3 9 453456 13 453 14 123”。
	•	规则 6：符合子串 “6” 的记录有
I₁=456, I₂=786, I₄=46, I₈=665, I₉=453456, I₁₁=456, I₁₂=786 共 7 条，
输出 “6 7 1 456 2 786 4 46 8 665 9 453456 11 456 12 786”。

共计输出数字 30 个，因此最开始输出 “30”。
'''
import sys
lines = []
deduplicated = {}
result = []

#input data:
for line in sys.stdin:
    a = line.strip().split()
    lines.append(a)
I = lines[0]
length = int(I.pop(0))
R = [int(x) for x in lines[1]]
length_R = R.pop(0)
unique_R = list(set(R))
unique_R.sort()
#print(f'i:{I},\nR:{unique_R}')

#is num legal:
def is_legal(num,check):
    if str(check) in num:
        return True
    return False

for check in unique_R:
    pos = len(result)
    result.append(check)
    have_nums = False
    count = 0
    for i in range(len(I)):
        if is_legal(I[i],check):
            result += [i,int(I[i])]
            count += 1
            have_nums = True
    if count != 0:
        result.insert(pos+1, count)
    if not have_nums:
        result.pop(-1)

result.insert(0,len(result))
for res in result:
    print(res,end=' ')

