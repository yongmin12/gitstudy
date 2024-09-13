# 내장 함수 : 원래 제공되는 것, import 필요 없음


# 매개변수로 전달된 값 중 가장 큰 값을 반환
# print(max(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split()))
# print((max(score)))
# print(max([1,2,3,4,5,6,7,8]))

# print(min(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split()))
# print((min(score)))
# print(max([1,2,3,4,5,6,7,8]))

# # 시퀀스 자료형의 값을 모두 더 해줌
# print(sum([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4,]) / 5)
#
# # 몫과 나머지를 반환, 튜플 형태로 반환(unpacking)
# print(divmod(sum([1, 2, 3, 4, 5]), 5))
#
# # 정렬
# my_list = [1,5,77,99,23,345,23,555]
# print(sorted(my_list)) # 오름 차순 정렬
# print(sorted(my_list, reverse=True)) # 내림 차순
# print(len(my_list)) # 요소의 개수

# 실습
score = list(map(int, input("정수 입력 : ").split()))
# 입력 받은 값에서 제일 큰 값
print(f"최대값 : {max(score)}")
# 입력 박은 값에서 제일 작은 값
print(f"최소값 : {min(score)}")
# 총점
print(f"총점 : {sum(score)}")
# 평균
print(f"평균 : {sum(score) / len(score)}")
# 해당 리스트(n)를 5로 나눈 몫과 나머지
print(f"몫과 나머지 : {divmod(sum(score), 5)}")



