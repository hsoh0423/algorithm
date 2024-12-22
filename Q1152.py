input_word = input()

input_word_list = input_word.split(" ")
word_list_len = len(input_word_list)

if input_word_list[0] == '':
    word_list_len = word_list_len - 1
    
if input_word_list[-1] == '':
    word_list_len = word_list_len - 1

print(word_list_len)