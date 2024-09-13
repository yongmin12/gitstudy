# 외장함수는 import 해서 사용하는 함수, 파이썬 기본적으로 제공하는 것,
# 랜덤 함수 : 지정한 범위내에서 임의의 숫자를 만들어 내는 것
import random
from random import randrange
from turtledemo.penrose import start

# for i in range(30):
#  rand = random.randrange(start:1, stop:11)
#  print(rand, end="")
# print()
#
# # 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# # 리스트를 사용하고, 리스트내에 임의로 생성한 번호가 있으면, 추가 하면 안됨

print("로또 번호 자동 생성 : ", end ="")
# 중복 숫자 제거
lotto = []
while True :
    rand = random.randint(1,45) # 1 ~ 45
    if rand not in lotto:
        lotto.append(rand)
    if len(lotto) == 6: break
print(lotto)

lotto = set()
while len(lotto) <= 6:
    rand = rand





