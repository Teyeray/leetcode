def get_clock_in(n, second):
    i = 0
    first_date = {}
    count = [0 for _ in range(n)]
    while i < len(second):
        new_input = input().strip().split(" ")
        print(f'date:{i + 1}, new_input: {new_input}')
        for id in new_input:
            id = int(id)
            count[id] += 1
            if id not in first_date:
                first_date[id] = i + 1
        i += 1
    print(f'first_date: {first_date}')
    print(f'count: {count}')
    return first_date, count

def get_top_5(first_date, count):
    # sort by count first, and get id, then sort by first_date,then by id itself
    sorted_ids = sorted(range(len(count)), key=lambda x:(-count[x], first_date.get(x, float('inf')), x))
    return sorted_ids[:5]

n = int(input().strip())
second = input().strip().split(" ")
print(f'second: {second}')

#print(f'n: {n}, second: {second}')
first_date, count = get_clock_in(n, second)


#TEST data

# first_date = {0: 1, 1: 1, 7: 1, 10: 1, 6: 2}
# count = [2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 30]

#first_date = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
#count = [30, 30, 30, 30, 30, 30, 0]

print(f'first_date: {first_date}, count: {count}')
# Get top 5 ids based on count and first_date
top_5 = get_top_5(first_date, count)
print(f'top_5: {top_5}')
