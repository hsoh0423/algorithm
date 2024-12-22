num1 = int(input())
num2 = int(input())
num3 = int(input())

total_num_mul = str(num1 * num2 * num3)

for i in range(10):
    count_num = total_num_mul.count(str(i))
    print(count_num)