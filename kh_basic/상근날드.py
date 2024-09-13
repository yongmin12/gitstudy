# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트 메뉴 가격 = 햄버거 3개 중 제일 싼거 + 음료 2개 중 싼거 - 50
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

ls = list(map(int,input("입력 : ").split()))
# min_berger = min(ls[:3])
# min_drink = min(ls[3:5])
# print(f"{min_berger + min_drink -50}")
min_berger = ls[0] # 기준값 정하기
min_drink = ls[3]
for i in range(len(ls)):
    if i < 3 and min_berger > ls[i]:
        min_berger = ls[i]
    if i > 2 and min_drink > ls[i]:
        min_drink = ls[i]

print(f"{min_berger + min_drink -50}")








