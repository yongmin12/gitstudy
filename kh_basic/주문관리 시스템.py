import decimal


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = decimal.Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self, products=None, total=0):
        if products is None:
            products = []
        self.products = products
        self.total = decimal.Decimal(total)

    def add_item(self,product:Product):
        # for e in self.products:
        #     if product.get_name() == e.get_name():
        #         return
        self.products.append(product)
        self.total += product.price
    def get_item(self,name: str):
        for e in self.products:
            if name == e.get_name():
                return e
        return  None
    def remove_item(self,name:str):
        for e in self.products:
            if name == e.get_name():
                self.products.remove(e)
                return True
        return False
    def calculate_final_price(self, tax_rate: decimal.Decimal):
        return round(self.total * (1 + tax_rate),2)


if __name__ == "__main__":
    # Order 객체 생성
    my_order = Order()

    # Product 객체 추가
    my_order.add_item(Product("Apples", "3.16"))
    my_order.add_item(Product("Bananas", "1.06"))

    # 최종 가격 계산 (판매세 6% 적용)
    final_price = my_order.calculate_final_price(decimal.Decimal("0.06"))

    # 최종 가격 출력
    print(f"최종 가격 (세금 포함): {final_price}")  # 예상 출력: 4.47


while True:
    print("제품 선택 : ")
    sel = input("[1]제품 추가 [2]제품 제거 [3]제품 목록 보기 [4]제품 상세 보기 [5]최종 가격 계산(세금 포함) [6]프로그램 종료 :")
    if sel == "1" :
       name = input("제품 추가 : ")
       my_order.add_item(name)
    elif sel == "2":
        name = input("제거할 제품 : ")
        my_order.remove_item(name)
    elif sel == "3":
        for e in my_order.products:
            print(f"{e.get_name()}  :  {e.get_price()}")
    elif sel == "4":
        name = input("제품 상세 보기 : ")
        product = my_order.get_item(name)
        print(f"{product.get_name()}  :  {product.get_price()}")
    elif sel == "5":
        final_price = my_order.calculate_final_price(decimal.Decimal("0.06"))

        # 최종 가격 출력
        print(f"최종 가격 (세금 포함): {final_price}")  # 예상 출력: 4.47
    elif sel == "6": break
    else :
        print("잘못된 입력 입니다.")
