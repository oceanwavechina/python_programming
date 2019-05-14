from time import sleep
from tqdm import tqdm

for i in tqdm([1,2,3,4,5]):
    sleep(1)
    print('hello')