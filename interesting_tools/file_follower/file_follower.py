'''
Created on Jul 6, 2019

@author: liuyanan
'''

import os
import time
import sqlite3


class Persistence(object):
    '''
        Table Structure
            filename:  filename
            pos:       the position not yet read
            tm:        last db update tm
    '''

    def __init__(self, dbfile):
        self.dbfile = dbfile
        if not os.access(self.dbfile, os.F_OK):
            f = open(self.dbfile, 'w')
            f.close()

        self.conn = sqlite3.connect(self.dbfile)
        self._try_create_table()

    def _try_create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS "logtop_pos" (
                "filename" varchar(128) NOT NULL,
                "pos" integer NOT NULL,
                "tm" integer NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (filename)
            );
        """
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def save_position(self, filename, pos):
        sql = "replace into logtop_pos (filename, pos, tm) values (?,?,?)"
        c = self.conn.cursor()
        c.execute(sql, (filename, pos, int(time.time())))
        self.conn.commit()

    def get_position(self, filename):
        sql = "select pos from logtop_pos where filename=? limit 1;"
        c = self.conn.cursor()
        c.execute(sql, (filename, ))
        self.conn.commit()
        res = c.fetchone()
        if res:
            return res[0]
        else:
            return 0


class FileFollower(object):
    def __init__(self, filename, persistence=None, inspect_interval=1):
        self.filename = filename
        self.inspect_interval = inspect_interval
        self.callbacks = set()
        self.persistence = persistence

    def register_callback(self, cb):
        self.callbacks.add(cb)

    def follow_it(self):
        with open(self.filename) as f:
            start_pos = self.persistence.get_position(self.filename) if self.persistence else 0
            f.seek(start_pos, os.SEEK_SET)
            while True:
                cur_position = f.tell()
                line = f.readline()
                if not line:
                    f.seek(cur_position, os.SEEK_SET)
                    if self.persistence:
                        self.persistence.save_position(self.filename, cur_position)
                    time.sleep(self.inspect_interval)
                else:
                    for cb in self.callbacks:
                        cb(line)

    def _sanity_check(self):
        if not os.access(self.filename, os.F_OK):
            raise RuntimeError("%s not exist" % self.filename)
        if not os.access(self.filename, os.R_OK):
            raise RuntimeError("%s not readable" % self.filename)
        if not os.path.isfile(self.filename):
            raise RuntimeError("%s not a file" % self.filename)
