# ip_addr = [128, 0, 255, 255]
# ip_addr = [1,0,0,0]
#print(f'ip_addr: {ip_addr}')

#将ipv4地址转换为32位整数
def to_32_bit(ip_addr):
    return ip_addr[0] << 24 | ip_addr[1] << 16 | ip_addr[2] << 8 | ip_addr[3]

#检查第一位是否在0-128，后三位是否在0-255之间
def check_valid(ip_addr):
    if ( 1 <= ip_addr[0] <= 128) and len(ip_addr) == 4:
        for num in ip_addr[1:]:
            if not (0 <= num <= 255):
                print(f'invalid IP')
                return False
    return True 

#检查任何一个数是否有前置0
def check_zero_ahead(str_list, num_list):
    len1 = len(str_list)
    len2 = len(num_list)
    if len1 != len2:
        print(f'invalid IP')
        return False
    for i in range(len1):
        if len(str_list[i]) != len(str(num_list[i])):
            print(f'invalid IP')
            return False
    return True

#检查是否都为数字
def check_is_num(str_list):
    for s in str_list:
        if not s.isdigit():
            print(f'invalid IP')
            return False
    return True

#读取输入
ip_addr_str = input().strip().split('#')
#print(f'split ip_addr: {ip_addr_str}')

#检查
if check_is_num(ip_addr_str):
    ip_addr = [int(x) for x in ip_addr_str]
    if check_zero_ahead(ip_addr_str, ip_addr) and check_valid(ip_addr):
        print(to_32_bit(ip_addr))
