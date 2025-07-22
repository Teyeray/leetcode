def get_data():
    number = int(input().strip())
    days = int(input().strip())
    item = []
    item.extend(list(map(int, input().strip().split())))
    price = []
    i = 0
    while i < number:
        price.append(list(map(int, input().strip().split())))
        i += 1
    print(f'number:{number}, days:{days}, item:{item}, price:{price}')
    return number, days, item, price

def get_profit(price):
    n = len(price)
    i = 1
    profit = 0
    while i < n:
        profit += max(0, price[i]-price[i-1])
        i += 1
    return profit

number, days, item, price = get_data()
#exp1
# number = 3
# days = 3
# item = [4, 5, 6]
# price = [[1, 2, 3], [4, 3, 2], [1, 5, 2]]

money = 0
profit = []
for i in range(number):
    profit.append(get_profit(price[i]))
    money += item[i] * profit[i]
print(f'profit:{profit}')

print(f'{money}')

