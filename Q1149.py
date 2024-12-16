from sys import stdin

def cal_house_price(house1, house2, last_index):
    
    min_price = 999999
    temp_last_index = -1
    
    for i in range(3):
        if last_index == i:
            continue
        else : 
            sum_price1 = house1[i] + house2[(4+i) % 3]
            sum_price2 = house1[i] + house2[(5+i) % 3]
            #print(sum_price1, sum_price2)
            if sum_price1 <= sum_price2 and sum_price1 <= min_price:
                min_price = sum_price1
                temp_last_index = (4+i) % 3
                
            if sum_price2 < sum_price1 and sum_price2 < min_price:
                min_price = sum_price2
                temp_last_index = (5+i) % 3
            
    return min_price, temp_last_index
    


def function():
    num_of_house = int(input())

    i = 0
    last_index = 4
    total_minimum_price = 0

    while i < num_of_house - 1:
        house_rgb_1 = list(map(int, stdin.readline().split()))
        house_rgb_2 = list(map(int, stdin.readline().split()))
        i = i + 2
        sum_of_two_house_price, last_index = cal_house_price(house_rgb_1, house_rgb_2, last_index)
        total_minimum_price = total_minimum_price + sum_of_two_house_price
        #print(total_minimum_price)
        
    # 집의 개수가 홀수 일 경우 마지막 집 입력
    if(num_of_house % 2 == 1):
        last_house = list(map(int, stdin.readline().split()))
        last_house_price1 = last_house[(4+last_index) % 3]
        last_house_price2 = last_house[(5+last_index) % 3]
        
        temp_min_num = 0
        
        if last_house_price1 < last_house_price2:
            temp_min_num = last_house_price1
        else : 
            temp_min_num = last_house_price2
        
        total_minimum_price = total_minimum_price + temp_min_num
    return total_minimum_price

if __name__ == "__main__":
    print(function())