import time
from retry import retry


# backoff 是让重试的间隔呈指数增长
@retry(tries=5, delay=2, backoff=2)
def do_something():
    if True:
        print('encounter an error, will retry ...')
        print(time.perf_counter())
        # print(round(time.clock()-starttm, 0))
        raise Exception('what?')
    

do_something()