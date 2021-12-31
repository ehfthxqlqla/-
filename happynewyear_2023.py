import datetime
import time
import sys
import os
import random

nowtime = time.strftime("2023년까지 : %Y년 %m월 %d일 / %p %I시 %M분 %S초")
time_list = list(nowtime)

# 16:17
# 0:3

while True:
    time_list = list(nowtime)
    if time_list[16:17] == "PM":
        nowtime = time.strftime("2023년까지 : %Y년 %m월 %d일 / 오후 %I시 %M분 %S초")
    else:
        nowtime = time.strftime("2023년까지 : %Y년 %m월 %d일 / 오후 %I시 %M분 %S초")

    if time_list[14] == "3":
        break
    else:
        pass
    
    print(nowtime, end='\r', flush=True)


os.system('cls')

print("""어느덧 시간이 흘러 2023년이 되었습니다.
시간은 정말 빠르게 갔고
그동안 행복했습니다.
아무튼 새해복 많이 받으세요 ㅇㅇ""")

os.system("pause")
sys.exit()
