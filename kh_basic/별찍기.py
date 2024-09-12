# 입력 : 5
# 2중 for문 사용해서 풀기
# *
# **
# ***
# ****
# *****
n = int(input("입력 : "))
for i in range(n): # 행의 개수
    for j in range(i+1):
        print("*", end="")
    print()