
def get_data():
    m, n = list(map(int, input().strip().split()))
    map_ = list(map(int, input().strip().split()))
    mapp = []
    source = max(map_)
    idx = map_.index(source)
    source_idx = [idx//n, idx%n]
    for i in range(m):
        temp = map_[i * n : (i+1) * n]
        mapp.append(temp)
    print(f'map_:{map_},\nmapp:{mapp},\nsource_idx:{source_idx}')
    return m, n, mapp, source_idx

def print_map(m, mapp):
    for i in range(m):
        print("   |   ".join(map(str, mapp[i])),end = "\n")
    return

def get_coord(direction:int, m:int, n:int, curr_pos:list, mapp:list):
    y = curr_pos[0]
    x = curr_pos[1]
    if direction == 1: #up
        if y - 1 < 0 or mapp[y-1][x] == -1:
            return None
        curr_pos[0] -= 1
    elif direction == 2: #left
        if x - 1 < 0 or mapp[y][x-1] == -1:
            return None
        curr_pos[1] -= 1
    elif direction == -2: #right
        if x + 1 == n or mapp[y][x+1] == -1:
            return None
        curr_pos[1] += 1
    else:
        if y + 1 == m or mapp[y+1][x] == -1:
            return None
        curr_pos[0] += 1
    return curr_pos

def cal_neighbour(source_idx:list, mapp:list):
    value = mapp[source_idx[0]][source_idx[1]]
    if value <= 0:
        return mapp
    directions = [1, -1, 2, -2]
    for direc in directions:
        new_pos = get_coord(direc, m, n, source_idx.copy(), mapp)
        if new_pos is not None:
            y, x = new_pos
            if mapp[y][x] < value - 1:
                mapp[y][x] = value - 1
                cal_neighbour(new_pos, mapp)
    return mapp

#exp1
# m = 6
# n = 5
# i, j =[1, 4]
# mapp = [[0, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, 0, -1, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, -1], [0, 0, 0, 0, 0]]
# source_idx = [2, 3]

#exp2
# m = 6
# n = 5
# mapp = [[0, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, 0, -1, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# i, j = [2, 1]

m, n, mapp, source_idx = get_data()
# i, j = list(map(int, input().strip().split()))
print_map(m, mapp)

mapp = cal_neighbour(source_idx, mapp)

print(f'\n\n\nresult:')
print_map(m, mapp)
result = mapp[i][j]
print(f'\n\n\nresult:{result}')
