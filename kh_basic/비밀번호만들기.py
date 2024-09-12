# 각 사이트 비밀번호 만들기
from jinja2.utils import urlize

url = input("사이트 : ")
my_str = url.replace() # 입력 받은 문자열에서   잘라내기
my_str = my_str[:my_str.index(".")]  # 0에서 부터 . 의 인덱스 미만까지 슬라이싱
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("ㅇ")) + str(my_str.count("k")) + "!" + "jks"
print("비밀번호 : " + pwd)

file_name = "password.txt"
f = open(file_name,  "wt")
while True:
    url = input("사이트 : ")
    if url = "exit" : break

    my_str = my_str[:my_str.index(".")]
    pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("ㅇ")) \
          + str(my_str.count("k")) + "!" + "jks"
    f.write(pwd + "\n")
 f.close()


