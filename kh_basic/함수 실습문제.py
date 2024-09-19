# 입력 받은 수 미만의 소수의 합 구하기
# 1과 자기자신을 제외하고 나누어 지지 않는 수
# 입력 : 12 (2 + 3 + 5 + 7 + 11) = 28

def prime_func(n):
    is_prime = True
    for i in range(2, n) : # 1과 자기 자신읋 제외
        if n % i == 0 : is_prime = False
    if is_prime : return n
    else : return 0

num = int(input("정수 입력 : "))
prime_sum = 0
for i in range(2,num) :
    prime_sum += prime_func(i)
print(prime_sum)

