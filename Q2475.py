total = 0
input_num_list = input().split(" ")
for i in input_num_list:
    total = total + int(i) ** 2
    
print(total % 10) 