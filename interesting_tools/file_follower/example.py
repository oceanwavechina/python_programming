'''
Created on Jul 7, 2019

@author: liuyanan
'''

import os
import pickle
from file_follower import Persistence, FileFollower
from filters import kw_log_line_to_dict


class SingerScore(object):
    def __init__(self, user_pickle=False):
        self.score_per_singer = {}
        self.user_pickle = user_pickle
        if self.user_pickle:
            self.pickle = 'score.pickle'
            if os.access(self.pickle, os.F_OK):
                try:
                    with open(self.pickle, 'r') as f:
                        self.score_per_singer = pickle.load(f)
                        print 'from pickle:', self.score_per_singer
                except Exception as _:
                    pass

    def incre(self, uid, score):
        if uid not in self.score_per_singer:
            self.score_per_singer[uid] = 0
        self.score_per_singer[uid] += score
        print self.score_per_singer
        if self.user_pickle:
            with open(self.pickle, 'w') as f:
                pickle.dump(self.score_per_singer, f)


scores = SingerScore()


def filter_onstop(line):
    """
        cmd:cs19_pk_singeronstop|teamid:1|singerid:2|round:3|score:4|rand:64740832|tm:1562492382
    """
    value_dict = kw_log_line_to_dict(line)
    if value_dict.get('cmd', None) != 'cs19_pk_singeronstop':
        return

    if 'singerid' in value_dict and 'score' in value_dict:
        singerid = long(value_dict['singerid'])
        score = long(value_dict['score'])
        scores.incre(singerid, score)


def filter_onstart(line):
    value_dict = kw_log_line_to_dict(line)
    if value_dict.get('cmd', None) != 'cs19_pk_singeronstart':
        return
    # print value_dict


def filter_println(line):
    print line


if __name__ == '__main__':
    # persistence && pickle file should set or unset together
    '''
    persistence = Persistence('logtop.sqlite3')
    tailer = FileFollower('test.txt', persistence)
    '''
    persistence = None
    tailer = FileFollower('test.txt')
    tailer.register_callback(filter_onstop)
    tailer.register_callback(filter_onstart)
    tailer.follow_it()
