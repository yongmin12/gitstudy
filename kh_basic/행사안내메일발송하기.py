#행사 안내 메일 내용 자동 작성 하기

# - 이름 : 조용민
# - 행사내용 : 현대 자동차 신차 발표회
# - 일시 : 20240911 (연속해서 입력)

name = input("이름 : ")
event = input("제목 :")
date = input("날짜 : ") # 20220301
time = input("시간 : ") # 24시간제 입력

# 입력 받은 date에서 월 정보 추출
month = date[4:6]
greeting = ""
if month == "01"
   greeting = "한파의 연속인 1월 입니다"
elif month = "봄을 기다리는 2월 입니다"
elif month == "12"
    greeting = "올 한해의 마무리 12월 입니다"
else:
    print("월 정보가 잘못 입력 되었습니다")
    print(f"{name}")
    print(greeting)
    print(f"""아래의 일정으로 {event}를 진행하고 하오니
    자리를 빛내 주시기 바랍니다.
    """)
    print("="*7, "행사 안내", "="*7)
    print("내용 : " + event )
    print(f"날짜 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
    time = int(time)
    if time > 12:
        print(f"시간 : 오후 {time}시")
    else:
        print(f"시간 : 오전 {time}시")


















