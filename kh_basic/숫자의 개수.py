# 자연수 A,B,C
# A = 150, B = 266, C = 427 이라면 A x B x C = 150 x 266 x 427  = 17037300
# 등장하는 숫자(0~9)의 개수를 세는 문제 :
# 범위 기반 for문 사용, count("찾고자 하는 문자")

a, b, c = map(int,input("정수 입력 : ").split()) # 숫자를 공백 기준으로 입력 받음
print(a * b * c)
ls = str(a * b * c)
for i in range(10): # 0~9
    print((ls.count(str(i))),end = " ")

# 실습 2번 : 문자열 반전,문자열을 입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA
in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1, -1, -1):
    print(in_str[i], end="")
# reverse_str = in_str[::-1]
# print(reverse_str)
