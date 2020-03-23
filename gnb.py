# 產生一個隨機整數
# 讓使用者重複輸入數字去猜
# 猜對的話要告訴他 猜對了!
# 猜錯的話 要告訴的 比答案小還大

import random
print("小遊戲，猜數字")
a = int(input("請輸入最小數字："))
b = int(input("請輸入最大數字： "))
n = random.randint(a , b)
count = 0
while True:
    g = int(input("請輸入數字： "))
    count += 1  #count = count + 1  
    if g == n:
        print("您猜對了！")
        break
    elif g > n:
            print("太大了喔！")
    elif g < n:
            print("太小了喔！")
    print("您已猜了，第", count,"次。")
        