def is_palindrome(num):
    
    temp_num = str(num)
    answer = True
    for i in range(int(len(temp_num)/2)):
        if temp_num[i] != temp_num[(len(temp_num) - 1) - i]:
            answer = False
    
    return answer

while(True):
    input_num = int(input())
    
    if input_num == 0:
        break
    else:
            
        if is_palindrome(input_num):
            print("yes")
        else:
            print("no")