import random

result = random.randint(1, 100)
while True:
    cho = int(input("정답을 입력하세요: "))
    if cho < result:
        print("정답은 %d보다 큽니다." % cho)
    elif cho > result:
        print("정답은 %d보다 작습니다." % cho)
    else:
        print("정답입니다.")
        break
