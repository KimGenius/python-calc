a = input("김동국의 국어 영어 수학 점수를 입력하세요: ")
a = a.split()
result = (int(a[0]) + int(a[1]) + int(a[2])) / 3
print('김동국의 평균 점수는 %0.2f 입니다.' % result)
