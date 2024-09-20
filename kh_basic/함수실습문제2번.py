# 두번쨔 수 찾기
# 입력 : 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾을수 : 3
# 해당 수의 위치를 반환 : 인덱스가 아님, 9번째
# 찾지 못하면 -1을 반환

def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i+1
            else: cnt += 1
    return -1
# 정수값에 대한 리스트 입력 생성
ls = list(map(int, input("리스트 입력 : ").split()))
# 찾을 수 입력 받기
n = int(input("찾는 숫자 : "))
# 결과 출력 하기
print(second_num(ls, n))

