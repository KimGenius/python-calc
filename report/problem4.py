de = int(input("정수를 입력하세요: "))
print(de, end= ' : ')
if de % 2 is 0 and de % 3 is 0:
    print("2와 3 모두의 배수 입니다.")
elif de % 2 is 0:
    print("2의 배수 입니다.")
elif de % 3 is 0:
    print("3의 배수 입니다.")
else:
    print("2와 3 모두의 배수가 아닙니다.")
