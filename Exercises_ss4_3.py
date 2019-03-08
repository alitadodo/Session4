
choice = {
1 : 35,
2 : 36,
3 : 40,
4 : 44
}
for key, value in choice.items():
    print(key, value, sep=".")
print("If x = 8, then what is the value of 4(x + 3)?")
n = int(input("Your choice: "))
count = 0
if n == 4:
    print("bingo")
    count += 1
else:
    print(":(")