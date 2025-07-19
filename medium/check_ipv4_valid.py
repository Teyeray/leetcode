# ip_addr = [128, 0, 255, 255]
# ip_addr = [1,0,0,0]
#print(f'ip_addr: {ip_addr}')


def to_32_bit(ip_addr):
    return ip_addr[0] << 24 | ip_addr[1] << 16 | ip_addr[2] << 8 | ip_addr[3]

def check_valid(ip_addr):
    if not ( 1 <= ip_addr[0] <= 128):
        print(f'invalid IP')
        return False
    if len(ip_addr) != 4:
        print(f'invalid IP')
        return False
    for num in ip_addr[1:]:
        if not (0 <= num <= 255):
            print(f'invalid IP')
            return False
    return True

def check_zero_ahead(str_list, num_list):
    len1 = len(str_list)
    len2 = len(num_list)
    if len1 == len2:
        for i in range(len1):
            if len(str_list[i]) != len(str(num_list[i])):
                print(f'invalid IP')
                return False
        return True
    print(f'invalid IP')
    return False

def check_is_num(str_list):
    for s in str_list:
        if not s.isdigit():
            print(f'invalid IP')
            return False
    return True

ip_addr_str = input().strip().split('#')

#print(f'split ip_addr: {ip_addr_str}')
if check_is_num(ip_addr_str):
    ip_addr = [int(x) for x in ip_addr_str]
    if check_zero_ahead(ip_addr_str, ip_addr):
        if check_valid(ip_addr):
            print(to_32_bit(ip_addr))
