'''
Created on Jul 6, 2019

@author: liuyanan
'''

import time
import random


def gen_data():
    while 1:
        time.sleep(1)
        output_stop = "cmd:cs19_pk_singeronstart|singerid:2|round:3|rand:%d|tm:%d\n"
        output_start = "cmd:cs19_pk_singeronstop|teamid:1|singerid:2|round:3|score:%d|tm:%d\n"
        output_mess = "cadfafasdfaasaf ||||||||::::::1|singerid:2|round:3|subround:4|rand:%d|tm:%d\n"
        with open("test.txt", 'a') as f:
            f.write(output_stop % (random.randint(0, 10), int(time.time())))
            f.write(output_start % (random.randint(0, 100000000), int(time.time())))
            f.write(output_mess % (random.randint(0, 100000000), int(time.time())))
            f.flush()


if __name__ == '__main__':
    gen_data()
