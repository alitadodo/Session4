
choice2 = {
    1 : "About 55",
    2 : "About 65",
    3 : "About 75",
    4 : "About 85"
}
for key, value in choice2.items():
    print(key, value, sep=".")

print('Estimate this answer (exact calculation not needed):')
print('Jack scored these marks in 5 math test: 49, 81, 72, 66 and 52. What is the mean?')


print("If x = 8, then what is the value of 4(x + 3)?")
n = int(input("Your choice: "))
count = 0
if n == 2:
    print("bingo")
    count += 1
else:
    print(":(")
