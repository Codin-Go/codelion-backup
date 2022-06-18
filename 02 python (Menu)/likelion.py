# Product1. 오늘 뭐 드실?

# import random
# import time

# for x in range(30):
#     print(random.choice(["된장찌개","제육볶음","치킨","떡볶이","라면"]))
#     print("this")

# while True:
#     break
#     print(random.choice(["된장찌개","제육볶음","치킨","떡볶이","라면"]))
#     print("this")
#     time.sleep(1)


# breakfast = random.choice(["된장찌개","제육볶음"])
# dinner = random.choice(["치킨","떡볶이","라면"])
# breakfast = "과일"

# print(breakfast)

# checked
# info = {"계절: 여름", "시간: 14pm"}
# print(info)
# print(info.get("계절"))

# information = {"특기":"피아노", "사는곳":"서울"}
# print(information.get("특기"))
# print(information.get("사"))

# information = {"특기":"피아노", "사는곳":"서울"}
# information["취미"] = "놀이터"
# print(information)
# del information["사는곳"]
# print(information)
# print(len(information))

# checked - append()
# information2 = ["사과", "바나나", "수박"]
# # print(information2[0])
# information2.append["참외"]
# # print(information2)

# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# foods = ["된장찌개", "피자", "제육볶음"]
# print(information.get("취미"))
# information["특기"] = "피아노"
# information["사는곳"] = "서울"
# del information["좋아하는 음식"]
# print(information)
# print(len(information))
# information.clear()
# print(information)
# print(foods[-2])
# foods.append("김밥")
# del foods
# print(foods)

# for x in range(10): 
#     print(x)

# chkd: ["a","b"]
# food = [l, i, s, t]
# for x in range(4):
#     print(food[x])

# foods = ["된장찌개", "피자", "제육볶음"]
# for x in range(3):
#     print(foods[x])

# food = ["l", "i", "s", "t"]
# # for x in range(4):
# #     print(food[x])
# for x in food:
#     print(x)

# chkd with items, paranthesis
# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# for x,y in information:
#     print(x,y)

# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# for x, y in information.items():
#     print(x)
#     print(y)

# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# for x, y in information.items():
#     print(x)
#     print(y)

# foods = ["apple", "banana", "carrot"]
# foods_set1 = set(foods)
# foods_set2 = set(["apple", "banana", "carrot"])
# print(foods_set1)
# print(foods_set2)

# foods = ["apple", "banana", "carrot", "carrot"]
# foods_set1 = set(foods)
# print(foods)
# print(foods_set1)

# # chkd: not list, but set 
# foods1 = ["apple", "banana", "carrot", "carrot"]
# foods2 = ["lemon"]
# foods = foods1 | foods2 
# # print(foods1)
# # print(foods)

# foods1 = set(["apple", "banana", "carrot", "carrot"])
# foods2 = set(["lemon", "carrot"])
# foods_add = foods1 | foods2 
# foods_same = foods1 & foods2 
# foods_not = foods1 - foods2 
# print(foods_add)
# print(foods_same)
# print(foods_not)


# # chkd: grammar 
# foods = ["apple", "banana", "carrot", "carrot"]
# selected = random.choice(foods)

# if selected == "apple"
#     print("give me two apple")
# else 
#     print("give me one")


# import random

# food = random.choice(["된장찌개","피자","제육볶음"])

# print(food)
# if(food == "제육볶음"):
#     print("곱배기 주세요")
# else:
#     print("그냥 주세요")
# print("종료")


# import random 

# foods = ["apple", "banana", "carrot", "carrot"]
# selected = random.choice(foods)

# if(selected == "apple"):
#     print("give me two apple")
# else:
#     print("give me one")
# print("done")

# # how to make loop? 
# lunch = ["apple", "banana"]
# item = input("enter: ")
# lunch.append(item)
# print(lunch)


# while True: # "q" # break # ctrl C # == 
# lunch = ["apple", "banana"]
# while True: 
#     item = input("enter: ")
#     if(item == "q"):
#         break
#     else:        
#         lunch.append(item)
#         print(lunch)
# print("done")


# set([food])
set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"

print(set_dinner)
print(food)
print(set_dinner - set([food]))

