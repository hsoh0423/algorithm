num_list = list(map(int, input().split()))

for i in range(7):
    num_difference = num_list[i] - num_list[i+1]
    if num_difference >= 2 or num_difference <= -2:
        print("mixed")
        break

if num_difference == 1:
    print("descending")
    
if num_difference == -1:
    print("ascending")
    
    