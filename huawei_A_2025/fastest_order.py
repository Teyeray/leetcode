def split_data(input):
    dates = []
    times = []
    for elem in input:
        elem = elem.split()
        #处理日期
        date = int("".join(elem[0].split("-")))

        #处理时间
        time = elem[1].split(":")
        second = time.pop()
        time.extend(second.split("."))
        time = [int(t) for t in time]  # 转换为整数列表

        #存储到列表
        dates.append(date)
        times.append(time)
    return dates, times

#处理输入
# n = int(input().strip())
# inputs = [input().strip() for _ in range(n)]

# #示例1
# n = 5
# inputs = ['2019-01-01 00:00:00.004', '2019-01-01 00:00:00.004', '2019-01-01 00:00:01.006', '2019-01-01 00:00:01.006', '2019-01-01 00:00:01.005']

# #示例2
n = 6
inputs = [ '2019-01-01 08:59:00.123', '2019-01-01 08:59:00.124', '2019-01-01 08:59:00.123', '2019-01-01 08:59:00.123', '2018-12-28 10:08:00.999', '2020-01-01 08:59:00.123']

print(f'inputs:{inputs}')
dates, times = split_data(inputs)
print(f'dates:{dates}, times:{times}')

result = sorted(range(n), key=lambda i: (dates[i], times[i][0], times[i][1], times[i][2], times[i][3]))

# 输出结果
print(f'result:{result}')

output = []
output.append(result[0])  # 添加第一个顾客的索引
# 遍历结果列表，从第二个元素开始
is_first = True
for i in range(1,len(result)):
    time_now = times[result[i]][:-1]  # 获取当前顾客的时间（不包括毫秒）
    if time_now != times[result[i-1]][:-1]:
        output.append(result[i])
        is_first = True
    elif dates[result[i]] != dates[result[i-1]]:
        output.append(result[i])
        is_first = True
    elif is_first:
        if time_now == times[result[i-1]][:-1] and dates[result[i]] == dates[result[i-1]]:
            output.append(result[i])
            if times[i+1][:-1] == times[i][:-1] and dates[i+1] == dates[i]:
                is_first = True
            else:
                is_first = False


print(f'output:{output}')
print(f'{len(output)}')
