'''
我们定义五类 IP 地址：

∙A 类：
"1.0.0.0"~"127.255.255.255";
∙B 类：
"128.0.0.0"~"191.255.255.255";
∙C 类：
"192.0.0.0"~"223.255.255.255";
∙D 类：
"224.0.0.0"~"239.255.255.255";
∙E 类：
"240.0.0.0"~"255.255.255.255"。
我们定义私有 IP 地址：
"10.0.0.0"~"10.255.255.255";
"172.16.0.0"~"172.31.255.255"; 
"192.168.0.0"~"192.168.255.255"。
每行输入一个 
"*.*.*.*"形式的 IP 地址和一个  "*.*.*.*"形式的子网掩码
中间用波浪线（～）分隔。保证'*'要么为空,要么是一个0到255间的整数。
input:
10.70.44.68~1.1.1.5
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0

output:
1 0 1 0 0 2 1
∙第一条地址信息:掩码非法； 
∙第二条地址信息:IP 格式和掩码均合法,属于 A 类； 
∙第三条地址信息:IP 格式和掩码均合法,属于 C 类私有地址； 
∙第四条地址信息:IP 格式非法。 
统计得到 
1 个 A 类,0 个 B 类,1 个 C 类,0 个 D 类,0 个 E 类,2 个错误条目,1 个私有地址。
'''
import sys
lines = []
out_list = [0,0,0,0,0,0,0] #A B C D E error private
for line in sys.stdin:
    line = line.strip()
    line = line.split('~')
    #lines.append(line)
    ip_address = line[0].split('.')
    mask = line[1].split('.')
    if len(ip_address) == 4 and len(mask) == 4:
        if ip_address[0] == '0':
            continue
        elif ip_address[0] == '127':
            continue
        ip = ip_address[:]+mask[:]
        print(f'ip:{ip}')
        if all(num.isdigit() and 0 <= int(num) <=255 for num in ip):
            bi_nums = []
            for num in mask:
                bi_num = bin(int(num))
                #print(bi_num)
                bi_nums.extend(bi_num[2:].zfill(8))
            print(f'{bi_nums},len:{len(bi_nums)}')
            illegal = False
            for i, bit in enumerate(bi_nums):
                if i == len(bi_nums) -1:
                    if bit == '1':
                        out_list[-2] += 1
                        illegal = True
                    break
                if bit == '0' and bi_nums[i+1] == '1':
                    print('wrong mask')
                    illegal = True
                    out_list[-2] += 1
                    break
            if not illegal:
                print(f'\nip_address[0]:{ip_address[0]}')
                if 1 <= int(ip_address[0]) <=127:
                    out_list[0] += 1
                    if ip_address[0] == '10':
                        out_list[-1] += 1
                elif 128 <= int(ip_address[0]) <=191:
                    out_list[1] += 1
                    if ip_address[0] == '172':
                        if 16 <= int(ip_address[1]) <= 31:
                            out_list[-1] += 1
                elif 192 <= int(ip_address[0]) <=223:
                    out_list[2] += 1
                    if ip_address[0] == '192':
                        print('it is 192')
                        if ip_address[1] == '168':
                            print('it is 192.168')
                            out_list[-1] += 1
                elif 224 <= int(ip_address[0]) <=239:
                    out_list[3] += 1
                elif 240 <= int(ip_address[0]) <=255:
                    out_list[4] += 1
                else:
                    out_list[-2] += 1
                    print('wrong ip')
        else:
             print('not 0~255')
             out_list[-2] += 1
    else:
        print('not 4')
        out_list[-2] += 1
    print(f'out_list:{out_list}')
for result in out_list:
    print(result,end = ' ')
    #print(f'out {ip_address}')
    #print(line)