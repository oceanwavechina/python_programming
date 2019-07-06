'''
Created on Jul 6, 2019

@author: liuyanan
'''

import os
import time
import sqlite3


class Persistent(object):
    def __init__(self, dbfile):
        self.dbfile = dbfile
        if not os.access(self.dbfile, os.F_OK):
            f = open(self.dbfile, 'w')
            f.close()

        self.conn = sqlite3.connect(self.dbfile)

    def save_cur_position(self, callback, pos):
        pass


class FileTailer(object):
    def __init__(self, filename, inspect_interval=1):
        self.filename = filename
        self.inspect_interval = inspect_interval
        self.callbacks = set()

    def register_callback(self, cb):
        self.callbacks.add(cb)

    def tail_it(self):
        with open(self.filename) as f:
            f.seek(0, os.SEEK_SET)
            while True:
                cur_position = f.tell()
                line = f.readline()
                if not line:
                    f.seek(cur_position)
                    time.sleep(self.inspect_interval)
                else:
                    for cb in self.callbacks:
                        cb(line)
                    print cur_position
                    # write cur_position to DB

    def _sanity_check(self):
        if not os.access(self.filename, os.F_OK):
            raise RuntimeError("%s not exist" % self.filename)
        if not os.access(self.filename, os.R_OK):
            raise RuntimeError("%s not readable" % self.filename)
        if not os.path.isfile(self.filename):
            raise RuntimeError("%s not a file" % self.filename)


def println(line):
    print(line)


if __name__ == '__main__':
    tailer = FileTailer('test.txt')
    tailer.register_callback(println)
    tailer.tail_it()
