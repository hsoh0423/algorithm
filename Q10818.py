total_num = int(input())
num_list = list(map(int, input().split()) )

max = -1000000
min = 1000000

for i in range(total_num):
    
    if num_list[i] <= min:
        min = num_list[i]
        
    if num_list[i] >= max:
        max = num_list[i]

print(min, max)