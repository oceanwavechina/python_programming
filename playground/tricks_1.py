
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
    print('')

    '''
        找到出现频率最高的前n个元素
    '''
    a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
    from collections import Counter
    cnt = Counter(a)
    print('Counter return:', cnt)
    #print('dir(Counter):', dir(cnt))
    print('top 2 common element:', cnt.most_common(2))
    print('')

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
    print('')

    '''
        字符串 和 数字 翻转
    '''
    a = 'abcdefghigklmnopqrstuvwxyz'
    print('reverse str \'%s\' using list slicing: \'%s\''%( a, a[::-1]))

    reversed_a = ''
    for char in reversed(a):
        reversed_a += char
    print('reverse str \'%s\' using reversed iterator: \'%s\''%( a, reversed_a))

    a = 123456789
    print('reverse number \'%d\' using list slicing: \'%d\''%( a, int(str(a)[::-1])))
    print('')


    '''
        链式比较
    '''
    b = 6
    print('chain comparison 4 < b < 7, result: %d' % (4 < b < 7))
    # 只要有一个不满足就是false
    print('chain comparison 1 == b < 7, result: %d' % (1 == b < 7))
    print('')

    '''
        根据不同的条件调用不同的函数(参数是一样的)
    '''
    def product(a, b):
        return a*b
    def add(a, b):
        return a+b
    b = True
    print('dynamic call function by conditions: %d'%( (product if b else add)(5, 7) ))
    print('')


    '''
        list copying
    '''
    
    print('list copying')

    print('\tname bingding')
    a = [1, 2, 3, 4]
    print('\t\ta = ', a, 'a.id = ', id(a))
    b = a
    print('\t\t(after b = a) b =', b, 'b.id = ', id(b))
    b[0] = 10
    print('\t\t(after b[0] = 10) a =', a, 'b = ', b)
    print('')

    #  阴影拷贝对于嵌套的可变元素，没有迭代创建新的元素
    print('\tcopy by slicing -- (Shallow copies)')
    a = [1, 2, 3, 4]
    print('\t\ta = ', a, 'a.id = ', id(a))
    b = a[:]
    print('\t\t(after b = a[:]) b =', b, 'b.id = ', id(b))
    print('')
    a = [[1, 2], (3, (4, 5)), 6]
    print('\t\ta = ', a, 'a.id = ', id(a))
    b = a[:]
    print('\t\t(after b = a[:]) b =', b, 'b.id = ', id(b))
    b[0][0] = 10
    print('\t\t(after b[0][0] = 10) a =', a, 'b = ', b)
    print('')

    print('\tcopy using copy method -- (Shallow copies)')
    import copy
    a = [1, [2, 3], 4]
    print('\t\ta = ', a, 'a.id = ', id(a))
    b = copy.copy(a)
    print('\t\t(after copy.copy(a)) b =', b, 'b.id = ', id(b))
    a[1][0] = 10
    print('\t\t(after a[0]=10) a =', a, 'b = ', b)
    print('')
    
    print('\tcopy using deepcopy method -- (Deep copies)')
    a = [1, [2, 3], 4]
    print('\t\ta = ', a, 'a.id = ', id(a))
    b = copy.deepcopy(a)
    print('\t\t(after copy.deepcopy(a)) b =', b, 'b.id = ', id(b))
    a[1][0] = 10
    print('\t\t(after a[0]=10) a =', a, 'b = ', b)
    print('')


    '''
        字典根据 值 排序
    '''
    d = {'apple':10, 'orange':20, 'banana':5, 'tomato': 1}
    print('original dictionary: ', d)
    print('sort-by-value using lambda: ', sorted(d.items(), key=lambda x: x[1]))
    from operator import itemgetter
    print('sort-by-value using itemgetter: ', sorted(d.items(), key=itemgetter(1)))
    print('sort-by-value return values only: ', sorted(d, key=d.get))
    print('')

    '''
        for-else语法, 如果for循环结束没有遇到break就会执行else的语句
    '''
    a = [1, 2, 3, 4, 5]
    for el in a:
        if el == 0:
            print('el==0')
            break
        # elif el == 5:
        #     print('got el == 5')
        #     break
    else:
        print('did not encounter break')
    print('')


    '''
        字典合并
    '''
    d1 = {'a':1}
    d2 = {'b':2}
    print('dict merge using {**d1, **d2}: ', {**d1, **d2})
    print('dict merge using dict( d1.items() | d2.items() ): ', dict( d1.items() | d2.items() ))
    d1.update(d2)
    print('dict merge using d1.update(d2): ', d1)

    print('')


    '''
        list 去重
    '''
    items = [2, 2, 3, 3, 1]
    print('original list: ', items)
    print('remove list duplicates without preserve previous order: ', list(set(items)))

    from collections import OrderedDict
    print('remove list duplicates and preserve previous order: ', OrderedDict.fromkeys(items).keys())
    


if __name__ == "__main__":
    part_1()