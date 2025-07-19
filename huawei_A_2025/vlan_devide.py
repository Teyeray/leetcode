#line = input().strip()

#line = '20-21,15,18,30,5-10'
line = '1-5'
vlan = '2'

#print(f'line: {line},line_type: {type(line)}')

#处理输入行，分割成单个数字
def parse_ranges(input_line):
    ranges = input_line.split(',')
    result = []
    print(f'ranges: {ranges}\n')
    for item in ranges:
        if '-' in item:
            nums = item.split('-')
            start = int(nums[0])
            end = int(nums[1])
            result.extend(range(start, end + 1))
        else:
            result.extend([int(item)])
    return sorted(result)

#重新用逗号和‘-‘连接
def re_format(input_lines):
    result = []
    i = 0
    while i < len(input_lines) - 1:
        curr = input_lines[i]
        if input_lines[i] + 1 == input_lines[i + 1]:
            while i < len(input_lines) - 1 and input_lines[i] + 1 == input_lines[i + 1]:
                curr_end = input_lines[i + 1]
                i += 1
            result.append(f'{curr}-{curr_end}')
        else:
            result.append(str(curr))
        i += 1
    print(f're_format result: {result}\n')
    return ','.join(result)

result = parse_ranges(line)
remove_num = int(vlan)
if remove_num in result:
    result.remove(remove_num)
else:
    print(f'num {remove_num} not in result: {result}\n')

print(f'result: {result}\n')

result = re_format(result)

print(f'answer: {result}\n')