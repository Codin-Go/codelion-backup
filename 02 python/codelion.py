# Product1. 오늘 뭐 드실?

# if, while True
# append
# not append on set 

# import random 
# import time 

# # fruit = set(["apple", "banana", "melon"])

# fruit = ["apple", "banana", "melon"]
# fruit_add = input ("add enter : ")
# fruit_fin = fruit.append(fruit_add)

# while True: 
#     print(fruit_fin)
#     if(fruit_add == "q"):
#         break
#     else:
#         fruit_fin = fruit.append(fruit_add)
# print(fruit_fin)


import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))