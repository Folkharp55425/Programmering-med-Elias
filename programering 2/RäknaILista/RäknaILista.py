startlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

jämn = 0

udda = 0

for num in startlist:
    if num % 2 == 0:
        jämn += num
    else:
        udda += num

print(jämn)
print(udda)


