import sys
def get_area_power(lines, settings):
    area = []
    output = []
    if settings[2] == 1:
        return lines[:]
    for j in range(settings[0]):
        for i in range(settings[1] - settings[2] + 1):
            curr_vol = 0
            for k in range(settings[2]):
                curr_vol += lines[j * settings[1] + i + k]
            if k == settings[2] - 1:
                area.append(curr_vol)
    new_horizontal = settings[1] - settings[2] + 1
    for i in range(new_horizontal):
        for j in range(settings[0]- settings[2] + 1):
            curr_vol = 0
            for k in range(settings[2]):
                curr_vol += area[(j+k) * new_horizontal + i]
            if k == settings[2] - 1:
                output.append(curr_vol)     
    return output


lines = []
#settings = input().strip().split(" ")
#settings = [2,5,2,6]
settings = [2,5,2,6]
# for line in sys.stdin:
#     print(f'input_line:{line}')
#     line = line.strip().split(" ")
#     print(f'line:{line}')
#     line = [int(x) for x in line]
#     print(f'line_int:{line}')
#     lines.extend(line)

lines = [1, 3, 4, 5, 8, 2, 3, 6, 7, 1]

output = get_area_power(lines, settings)
count = 0
for num in output:
    if num >= settings[3]:
        count += 1

print(f'lines:{lines}')
print(f'output:{output}')
print(f'count:{count}')