# 문자열이란? 문자로 이루어진
# "", '', """ """, ''' '''
# 인덱싱 : 시퀀스(이스트, 튜플, 문자열, input()) 자료형에서 특정 위치의 요소를 선택하는 작업
# 인덱싱은 0 부터 시작
# 슬라이싱 : 시퀀스 자료형애서 일부 데이터를 추출하는 것
# jumin = input("주민등록번호 입력 : ")  # 990702-1234567
from dataclasses import replace

# # 인덱싱
# gender = jumin[7]
# if gender == "1" or gender == "3" :
#     print("남성 입니다.")
# else:
#     print("여성 입니다.")

# # 태어난 년도를 구하기 위해서 슬라이싱
# year = jumin[:2] # 0에서 2미만, 0에서 부터 시작 되는 경우는 생략 가능
# year = int(year)
# if gender == "1" or gender == "2" :
#     year += 1900
# else :
#     year += 2000
#
# print(f"태어난 년도 : {year}")

# # 생일 출력 : 0702 => 7월02일
# month = jumin[2:4] # 2에서 4미만
# day = jumin[4:6]
# month = int(month)
# day = int(day)
#
# print(f"생일 : {month}월 {day}일")
#
# #생년월일
# print("생년월일 : " + jumin[:6])   # 990702-1178918
# print("뒤 7자리 : " + jumin[7:])   # 7에서 끝까지
# print("뒤 7자리 : " + jumin[-7:])  # -1은 맨 뒤자리

# print(jumin[14])  #  string index out of range

# life = "life is too short, you need python"
# tmp = life[0] + life[1] + life[2] + life[3]
# print(tmp)

# 대소문자 바꾸기 : upper(), lower()
a = "Hello Python Program..."
print(a.upper())
print(a.lower())
# 대문자는 소문자로 소문자는 대문자로...(오후에)

# 문자열 변경 : replace("기존 문자열", "바꿀 문자열")
b = "Hello Python Program..."
n_b = b.replace(_old:"Hello", _new:"")

# 문자열에 포함된 문자 갯수 세기 및 문자열 길이 구하기
# count() : 문자열 내장 함수로 메소드로 문자열에 포함된 문자의 갯수을 반환
# __len__() : 문자열 길이를 반환
# len() : 문자열 길이를 반환
c = "Hello Python Program..."
print(c.count("l")) # 해당 문자열에서 매개변수로 전달한 문자/문자열 갯수를 반환
print(len(c)) # 문자열 길이 반환
print(c.__len__())

# 문자열 찾기 : find() , rfind() , index()
# find() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 -1
# index() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 ValueError 발생하고 종료 됨
# rfind() : 뒤에서 부터 문자열을 찾음, 찾은 문자열의 인덱스는 앞에서 부터 계산
phrase= "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 종은 선물은 용서"
print(phrase.rfind("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))

print(phrase.find("나에게"))
# print(phrase.index("나에게"))
new_phrase = phrase.replace(_old:"가장", _new:"나에게")
print(new_phrase)

# 문자열 연산자 : +, *
print("태양고" + "나희도")
print("!"*10)
list = [0] * 10
print(list)

# 문자열의 양엎의 공백제거 : strip()
d = """
    안녕하세요.
    문자여릐 공백을 제거 하겠습니다.
    네네넨...
"""
print(d.strip())


