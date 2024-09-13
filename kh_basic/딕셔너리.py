# 딕셔너리? 키를 통해 각 요소를 접근 할 수 있도록 만들어진 데이터 타입
# {} 중괄호로 딕셔너리 선언
# 각 요소는 , (쉼표)로 구분
# 키와 값은 한쌍으로 구성되고 이 둘은 콜론(:)으로 구분
coffe_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte": 4000, "Moca": 4500}
food_menu = {"Cake": 5000, "Bakery": 6000}

print(coffe_menu)
print(coffe_menu["Espresso"]) #키로 값을 찾음
print(coffe_menu.get("Moca")) # get(키)함수로 값을 가져 옴

# 값 추가, 삭제, 키 존재 여부 확인
food_menu["IceCream"] = 5000 # 새로운 키와 값 추가
del coffe_menu["Latte"]      # 해당 명령으로 아이템 삭제
if "Bakery" in food_menu:
    print(f"Bakery price : {food_menu["Bakery"]}")
else: print("해당 메뉴가 없습니다.")

# update() 함수 : 딕셔너리 데이터를 한꺼번에 변경할 때 사용
coffe_menu.update({"Americano" : 2800, "Espresso" : 2700, "Latte": 4400, "Moca": 4920})
print(coffe_menu)

# 정보 얻기 : keys(), values(), items()
dict_lang = {"자바": 99, "자바스크립트": 80, "파이썬": 92, "C++": 89}
print(dict_lang.keys())
print(dict_lang.values())
print(dict_lang.items())


