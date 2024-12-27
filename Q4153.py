isnt_end = True
result_list = []

while(isnt_end):
    num_list = list(map(int, input().split()))
    if num_list[0] == 0 and num_list[1] == 0 and num_list[2] == 0:
        isnt_end = False
    else:
        num_list.sort()
        sum_two_line = num_list[0] ** 2 + num_list[1] ** 2
        remain_line = num_list[2] ** 2
        
        if sum_two_line == remain_line:
            result_list.append("right")
            
        else:
            result_list.append("wrong")

for i in range(len(result_list)):
    print(result_list[i])