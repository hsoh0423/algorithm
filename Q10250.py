input_test_num = int(input())
result_list = []

for i in range(input_test_num):
    h_w_n = list(map(int, input().split()))
    
    temp_h = h_w_n[2] % h_w_n[0]
    temp_w = int((h_w_n[2] / h_w_n[0]) + 1)
    
    if temp_h == 0:
        temp_w = temp_w - 1
        temp_h = h_w_n[0]
    1 
    if temp_w < 10:
        result_list.append(str(temp_h) + "0" + str(temp_w))
    else:
        result_list.append(str(temp_h) + str(temp_w))

for i in range(input_test_num):
    print(result_list[i])