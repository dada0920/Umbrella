from tqdm import tqdm
from time import sleep

for i in tqdm(range(1, 600)):
    sleep(0.1) # 무언가 시간이 많이 소요되는 연산군
