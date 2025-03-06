def sum_of_word(word):
    """
    计算给定单词中所有字母的ASCII值之和，减去96后的总和。

    参数:
    word (str): 输入的单词

    返回:
    int: 单词中所有字母的ASCII值之和减去96后的总和
    """
    # 初始化总和为0
    sum = 0
    # 遍历单词中的每个字符
    for char in word:
        # 将字符的ASCII值减去96后累加到总和中
        sum += ord(char) - 96
    # 返回计算得到的总和
    return sum

# 打开一个名为'results.txt'的文件，以写入模式打开，如果文件不存在则创建，如果存在则覆盖
with open('results.txt', 'w') as result:
    # 打开一个名为'./pytest/tsts.txt'的文件，以读取模式打开
    with open('./pytest/tsts.txt', 'r') as file:
        # 逐行读取文件内容
        for word in file.readlines():
            # 去除每行末尾的换行符，并计算该行单词的ASCII值之和
            if sum_of_word(word.strip()) == 100:
                # 将满足条件的单词写入'results.txt'文件
                result.write(word)
                # 打印满足条件的单词
                print(word)
                # 遍历满足条件的单词中的每个字符
                for c in word:
                    # 打印字符及其ASCII值减去96后的结果
                    print(c, ord(c)-96)
                # 找到满足条件的单词后，跳出循环
                break


open('sn.txt', 'w').write('sn')