lst = [1, 5, 4, 6, 7, 8, 3, 5]
number = 5


count = 0
i = 0
while i != len(lst):
    if number == lst[i]:
        count += 1
    i += 1

print(count)
