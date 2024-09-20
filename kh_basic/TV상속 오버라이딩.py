# 다형성이란 부모가 물려준 특성을 재정의 사용하는 것을 의미
# 오버로딩 : 파이썬에서 지원하지 않음 (메서드 이름은 동일하고 매개변수의 갯수나 타입으로 구분
# 오버라이딩 : 부모가 물려준 특성을 재정의 하는 것
class PrototypeTv:  # 상속 주기 위한 부모 클래스
    def __init__(self, is_on, channel, volume):
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        if 1 <= cnl <= 1000:
            self.channel = cnl
            print(f"채널을 {self.channel}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

class ProductTv(PrototypeTv):
    def set_channel(self, cnl): # 오버라이딩
       if 0 < cnl <= 2000:
           self.channel = cnl
           print(f"채널을 {self.channel}로 변경 하였습니다.")
       else:
           print(f"채널 설정 범위가 아닙니다.")


lg_tv = ProductTv(False,20,20)
lg_tv.set_channel(1500)