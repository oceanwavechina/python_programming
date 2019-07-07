'''
Created on Jul 7, 2019

@author: liuyanan
'''


def kw_log_line_to_dict(line):
    value_dict = {}
    pairs = line.split('|')
    for pair in pairs:
        pair = pair.strip()
        kv_list = pair.split(':')
        if len(kv_list) == 2:
            k, v = kv_list
            value_dict[k] = v
    return value_dict
