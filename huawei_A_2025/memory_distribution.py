#exp 1
# memory_pool = ['64:2', '128:1', '32:4', '1:128']
# request_list = [50, 36, 64, 128, 127]
def allocate_memory(memory_pool, request):
    i = 0
    while i < len(memory_pool):
        if memory_pool[i][0] >= request and memory_pool[i][1] > 0:
            memory_pool[i][1] -= 1
            return True
        i += 1
    return False

memory_pool = input().strip().split(",")
request_list = input().strip().split(",")
request_list = [int(x) for x in request_list]
enumerated_memory = [tuple(map(int, item.split(':'))) for item in memory_pool]
memory_pool = sorted([[size, count] for size, count in enumerated_memory], key=lambda x: x[0])


output = []
for request in request_list:
    output.append(allocate_memory(memory_pool, request))


print(",".join(map(str, output)).lower())
