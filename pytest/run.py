def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('results.txt', 'w') as result:
    with open('./pytest/tsts.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                result.write(word)
                print(word)
                for c in word:
                    print(c, ord(c)-96)
                break