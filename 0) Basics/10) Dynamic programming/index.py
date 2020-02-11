backpack = 4  # 4 kg

items = dict()

items['guitar'] = {
    'price': 1500,
    'weight': 1
}

items['stereo'] = {
    'price': 3000,
    'weight': 4
}

items['notebook'] = {
    'price': 2000,
    'weight': 3
}

items['smartphone'] = {
    'price': 2000,
    'weight': 1
}

indexed_keys = list(items)

table = [[0 for _ in range(0, backpack)] for _ in range(0, len(items))]

for i in range(0, len(table)):  # rows
    for j in range(0, len(table[i])):  # cells
        index = indexed_keys[i]
        item = items[index]
        price = item['price']
        weight = item['weight']

        if j + 1 >= weight:
            remainder = j - weight
            if remainder >= 0:  # if there is free space
                table[i][j] = price + table[i - 1][remainder]  # curr item price + remainder max price(previous row)
            else:
                table[i][j] = price
        else:
            table[i][j] = table[i - 1][j]

maximum = table[len(table) - 1][backpack - 1]

print("Table: ", table)
print("Maximum profit: ", maximum)
