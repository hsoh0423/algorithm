input_total_num = int(input())
input_sequence_of_num = input()
sum = 0
for i in range(input_total_num):
    sum = int(sum) + int(input_sequence_of_num[i])
    
print(sum)