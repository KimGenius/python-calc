def gugudan(dan):
    for i in range(1, 10):
        print("%d * %d = %d" % (dan, i, dan * i))


gugudan(int(input("단을 입력하세요: ")))
