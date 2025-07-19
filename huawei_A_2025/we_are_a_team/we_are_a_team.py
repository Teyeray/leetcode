setting = input().strip().split()
n = int(setting[0])
m = int(setting[1])

print(f'n: {n}, m: {m}')

def check_setting(n, m):
    if 1 <= n and 0 <= m < 1000:
        return True
    else:
        print('Null')
        return False
    
def read_message(n,m):
    i = 0
    sets = []
    while i < m:
        message = input().strip().split(" ")
        a = int(message[0])
        b = int(message[1])
        c = int(message[2])
        if not (1 <= a <= n ) or not (1 <= b <= n) or not (0 <= c <= 1):
            print('da pian zi')
            break
        #print(f'message: {message}')
        if c == 0:
            if i == 0:
                set_curr = {a,b}
                sets.append(set_curr)
            else:
                new_set = {a,b}
                for set_curr in sets:
                    if new_set.intersection(set_curr) != set():
                        set_curr.update(new_set)
                        break
                    #如果和所有集合都没有交集，再append:
                    elif set_curr == sets[-1]:
                        sets.append(new_set)
                        break
        elif c == 1:
            team = False
            for set_curr in sets:
                if a in set_curr and b in set_curr:
                    print('we are a team')
                    team = True
                    break
            if not team:
                print('we are not a team')
        i += 1
    print(f'sets: {sets}')
    return




if check_setting(n,m):
    read_message(n,m)