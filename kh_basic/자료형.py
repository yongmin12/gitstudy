# 문자열(문자 타입은 존재하지 않음), 숫자(정수형과 실수형), Boolean(참과 거짓)
# 변수란? 자료형을 이용해 실제 데이터를 저장할 공간을 할당 받는 것
# 변수에 값을 대입하는 연산자 =
from fontTools.varLib.interpolatableHelpers import PerContourPen

a = b = c = 1
a, b, c = 1, True,  "곰돌이"

# 변수의 타입 확인 : type()
print(type(a))
print(type(b))
print(type(c))
