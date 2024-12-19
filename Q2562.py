max = 0
max_index = -1
for i in range(9):
    new_num = int(input())
    if max < new_num :
        max = new_num
        max_index = i + 1

print(max)
print(max_index)        