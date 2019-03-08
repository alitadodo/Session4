prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for i in prices.keys():
    print(i)
    print("Prices:", prices[i])
    print("Stock:", stock[i])
total = 0
for i in prices:
    total += stock[i] * prices[i]
    print(total)


