remain_num_list = []

for i in range(10):
    input_num = int(input())
    remain_num = input_num % 42
    if remain_num not in remain_num_list:
        remain_num_list.append(remain_num)
        
print(len(remain_num_list))