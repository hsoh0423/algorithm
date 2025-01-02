input_num = int(input())

count = 0
i = 0

while(True):
    temp_num = str(666+i)
    
    if "666" in temp_num:
        count = count + 1
        
    i = i + 1
    
    if count == input_num:
        print(temp_num)
        break