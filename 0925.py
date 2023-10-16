A = 1, 2, 3
aA = list(A)
aA.append(4)
print(tuple(aA))

A = 1, 2, 3, 4, 5, 6
print(A[3:])

student = {
    "name": "김영재",
    "num": "2021113083",
    "email": "geniuks1047@naver.com",
    "subject": ["프밍", "ㅁㄴㅇㄹ"]
}

print(student.keys())
print(student.values())

if 'address' not in student:
    student["address"] = "서울"

print(student)

name1 = input("이름을 입력하세요: ")
phone1 = input("전화번호를 입력하세요: ")
dic = {
    name1: phone1
}
name1 = input("이름을 입력하세요: ")
phone1 = input("전화번호를 입력하세요: ")
dic[name1] = phone1

print(dic)
