data = input("압축할 문자열을 입력하세요: ")

temp = ""
tempCnt = 1

for i in range(0, len(data)):
    if temp != data[i]:
        if temp != "":
            print(temp + str(tempCnt), end='')
        tempCnt = 1
        temp = data[i]
    else:
        tempCnt += 1
    if i == len(data) - 1:
        print(temp + str(tempCnt), end='')

print()


for i in range(len("aaa") - 1):
    print(i)