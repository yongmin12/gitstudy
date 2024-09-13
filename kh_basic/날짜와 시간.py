# 날짜와 시간 관련 함수
from datetime import datetime #

print(datetime.today())
print(datetime.today().month)
print(datetime.today().date())
print(datetime.today().time())
print(datetime.today().hour)

import calender
print(calender.calender(2024))

# math 모듈 : 수학 관련 기능을 처리 할 때 사용
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.0000000001)) # 소수점 이하가 잇으면 무조건 올림
print(math.floor(1.999999999)) # 소수점 이하는 무조건 날림
