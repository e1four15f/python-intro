input_file = open('input.txt', 'r')

word_count_dict = {}

for line in input_file:
    words = line.split()

    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
            print(word_count_dict[word], end=' ')
        else:
            word_count_dict[word] = 0
            print(word_count_dict[word], end=' ')
