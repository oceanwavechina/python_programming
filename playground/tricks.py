
'''
    https://hackernoon.com/python-tricks-101-2836251922e0
'''

def part_1():
    '''
        交换两个元素比较容易理解，交换多个的容易出问题，比如下边的
    '''
    a, b, c = 1, 2, 3
    print('origin data: a=%d, b=%d, c=%d'%(a, b, c))
    c, a, b = a, a, c
    print('after swap: a=%d, b=%d, c=%d'%(a, b, c))

    '''
        找到出现频率最高的前n个元素
    '''
    a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
    from collections import Counter
    cnt = Counter(a)
    print('Counter return:', cnt)
    print('dir(Counter):', dir(cnt))
    print(cnt.most_common(2))

    '''
        判断两个单词是否仅仅是字母颠倒
            这个可以是一个面试题: 如何纠正用户输入单词的错误(仅仅是顺序颠倒的错误)
            思路：1. 预先对每个单词处理，分析出单词中每个字母出现的次数，
                 2. 然后根据tuple(char_1:cnt, char_2:cnt)的形式保存起来，
                    （ 其中char_1, char_2, 是按顺序放在tuple中的 ）
                 3. 对每个tuple 求 hash值， 得到的hash值作为key
                 4. 把所有key相同的单词，组成一个set， 这个set作为key的value，也就是key -> set(word1, word2...)
                 5. 当我们获取到用户的输入的时候， 我们通过2，3步的计算的到 key_input, 
                    如果key_input 在我们之前处理的key中，并且输入的单词word_input不在我们预先处理的set中
                    那这个单词就需要我们给用户提示
    '''
    str_a = 'hard'
    str_b = 'hrad'
    if Counter(str_a) == Counter(str_b):
        print('\'%s\' and \'%s\' are anagrams'%(str_a, str_b))


    '''
        字符串 和 数字 翻转
    '''
    a = 'abcdefghigklmnopqrstuvwxyz'


if __name__ == "__main__":
    part_1()