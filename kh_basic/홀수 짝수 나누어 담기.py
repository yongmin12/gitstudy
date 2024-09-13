# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제
number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x: x % 2 == 1, number))
even = list(filter(lambda x: x % 2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")

# even = []
# odd = []
# 
# for i in number:
#     if i % 2 == 0: even.append(i)
#     else: odd. append(i)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")





