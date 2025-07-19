setting = input().strip().split()
n = int(setting[0])
m = int(setting[1])
outputs = []
#print(f'n: {n}, m: {m}')

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def check_setting(n, m):
    if 1 <= n and 0 <= m < 1000:
        return True
    else:
        print('Null')
        return False
    
def read_message(n,m):
    i = 0
    parent = list(range(n + 1))
    while i < m:
        message = input().strip().split(" ")
        a = int(message[0])
        b = int(message[1])
        c = int(message[2])
        if not (1 <= a <= n ) or not (1 <= b <= n) or not (0 <= c <= 1):
            outputs.append('da pian zi')
            break
        #print(f'message: {message}')
        if c == 0:
            root_a = find(a, parent)
            root_b = find(b, parent)
            if root_a != root_b:
                parent[root_b] = root_a
        elif c == 1:
            team = find(a, parent) == find(b, parent)
            if team:
                outputs.append('we are a team')
            else:
                outputs.append('we are not a team')
        i += 1
    #print(f'sets: {sets}')
    return

if check_setting(n,m):
    read_message(n,m)
    print("\n".join(outputs))