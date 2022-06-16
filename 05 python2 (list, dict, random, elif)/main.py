
# print("Hello World!")
# print("123")


# name = input("이름을 입력해주세요 : ")
# print(name + "님")


# changing type 
# food1 = input("내가 먹은 음식의 가격 : ")
# food2 = input("친구가 먹은 음식의 가격 : ")

# food1 = int(food1)
# food2 = int(food2)

# print(food1 + food2)


# # plus minus times divide
# 월세 = int(input("월세를 입력해주세요 : "))
# 관리비 = int(input("관리비를 입력해주세요 : "))

# print(월세 + 관리비)
# print(월세 - 관리비)
# print((월세 + 관리비) * 12)
# print(월세 / 관리비)


# # list
# number = [1,2,3]
# print(number)


# # append
# orders = ["짜장", "짬뽕", "탕수육"]

# orders.append("냉면")
# print(orders)


# # insert 
# orders = ["짜장", "짬뽕", "탕수육"]

# orders.insert(2,"냉면")
# print(orders)


# # delete 
# orders = ["짜장", "짬뽕", "탕수육"]
# del orders[0]
# print(orders)


# # remove 
# orders = ["짜장", "짬뽕", "탕수육"]
# orders.remove("짜장")
# print(orders)


# len
# orders = ["짜장", "짬뽕", "탕수육"]
# print(len(orders))

# name = "안녕하세요 코드라이언입니다."
# print(len(name))


# add 
# num = [20, 40, 50, 10, 30]

# add = num[0] + num[1] + num[2] + num[3] + num[4]
# print(add)


# # sum
# num = [20, 40, 50, 10, 30, 100, 200]

# add = sum(num)
# print(add)


# average
# num = [20, 40, 50, 10, 30]

# print(sum(num) / 5)

# num = [20, 40, 50, 10, 30]

# print(sum(num) / len(num))


# # max min
# num = [20, 40, 50, 10, 30]

# print(max(num))
# print(min(num))


# dictionary
# menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

# print(menu)



# dictionary : name["a"] = b
# menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

# menu["냉면"] = 6000

# print(menu)


# # dictionary, example 
# menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

# menu["냉면"] = 6000

# print(menu["짬뽕"])

# menu["탕수육"] = 8500

# del menu["짜장"]

# print(menu)


# # = < > 
# myGrade = 10
# yourGrade = 15

# print(myGrade != yourGrade)


# myGrade = int(input("학번을 입력하세요 : "))
# yourGrade = int(input("학번을 입력하세요 : "))

# print(myGrade != yourGrade)


# # 
# myGrade = int(input("학번을 입력하세요 : "))
# yourGrade = int(input("학번을 입력하세요 : "))

# if myGrade == yourGrade :
#     print("앗 동기네요!")
#     print("반갑습니다.")
# print("누구세요?")


# 
# myGrade = int(input("학번을 입력하세요 : "))
# yourGrade = int(input("학번을 입력하세요 : "))

# if myGrade == yourGrade :
#     print("앗 동기네요!")
# else :
#     print("앗 동기가 아니네요!")


#
# myGrade = int(input("학번을 입력하세요 : "))
# yourGrade = int(input("학번을 입력하세요 : "))

# if myGrade == yourGrade :
#     print("안녕하세요 동기님!")
# elif myGrade > yourGrade :
#     print("안녕하세요 선배님!")
# elif myGrade < yourGrade :
#     print("안녕하세요 후배님!")
# else :
#     print("누구세요?")



# list
# orders = ["짜장", "짬뽕", "탕수육"]

# food = input("먹고싶은 메뉴를 입력해주세요 : ")

# if food in orders :
#     print("주문할 수 있습니다.")
# else :
#     print("주문할 수 없습니다")


# 
# menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

# food = input("먹고싶은 메뉴를 입력해주세요 : ")

# if food in menu :
#     print("주문 가능")
# else :
#     print("주문 불가")



# menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

# food = input("먹고싶은 메뉴를 입력해주세요 : ")

# if food in menu :
#     print(menu[food], "원 입니다.")
# else :
#     print("주문 불가")



# if 10 < 90 :
#     print("True")


# 
# i = 0

# while i < 6 :
#     print(i)
#     i = i + 1



# i = 5

# while i >= 0 :
#     print(i)
#     i = i - 1


# 
# i = 0
# while True :
#     print(i)
#     i = i + 1

#     if i >= 3 :
#         print("if문 동작")
#         break

# print("반복문 종료!")


# #
# i = 0
# while i < 10 :
#     i = i + 1

#     if i % 2 == 0 :
#         continue
#     print(i)

# print("반복 종료!")



# for x in [10, 20, 30] :
#     print("안녕하세요")



# for x in range(100) :
#     print("안녕하세요")



# for x in range(10) :
#     print(x)

# for x in range(10, 20) :
#     print(x)


# for x in range(3, 31, 3) :
#     print(x)


# result = 1

# for x in range(1, 11) :
#     result = result + 1 

# print(result)


# result = 0

# for x in range(1, 101) :
#     result = result + x

# print(result)



# result = 1

# for x in range(1, 5) :
#     result = result * x

# print(result)


# for x in range(5) :
#     print("*")

# for x in range(5) :
#     print("*", end="1")


# x = int(input("숫자를 입력해주세요 : "))

# for i in range(x) :
#     print(i+1)



# 
# import random

# randomNumber = random.sample(range(1, 100), 10)
# print(randomNumber)


# stars
# for x in range(5) :
#     print("*" * 5)


# for x in range(5) :
#     print("*" * (x + 1))


# product. count down 
# x = int(input("숫자를 입력하세요 : "))

# for i in range(x, 0, -1) :
#     print(i)

# 
# x = int(input("숫자를 입력하세요 : "))

# for i in range(x) :
#     if i % 10 == 0 :
#         print()
#     print(i+1, end="\t")


# 
# import random

# count = int(input("로또를 몇개 구매하시겠습니까? "))

# for i in range(count) :
#     lotto = random.sample(range(1, 46), 6)
#     lotto.sort()
#     print(lotto)

# print("로또 종료")

# print(int(20) + int(30))



# #dict의 다양한 기능을 활용해 봅시다.
# name = {"길동" : 20, "철수" : 25, "영희" : 27}
# print(name)

# #첫째. name dict에서 길동을 삭제하는 코드를 아래에 작성해주세요.
# del name["길동"]
# print(name)

# # #둘째. 철수의 나이 25를 27로 수정하는 코드를 아래에 작성해주세요.
# name["철수"] = 27
# print(name)

# # #셋째. name dict 전체를 출력하는 코드를 아래에 작성해주세요.
# print(name)