word_num = int(input())
word_list = []
for i in range(word_num):
    word_list.append(input())

word_list = list(set(word_list))
result_list = sorted(word_list, key= lambda x : (len(x), x))

for i in range(len(result_list)):
    print(result_list[i])
