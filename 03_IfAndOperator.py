#實作點餐系統

print("=====歡迎光臨，請使用自動點餐系統=====")
print("1:原味無骨炸雞 $300")
print("2:神奇辣起士無骨炸雞 $350")
print("3:奶油優格炸雞 $400")
ch1 = input("請選擇炸雞口味(輸入:1 or 2 or 3)\n")
sum = 0
if ch1 == "1":
    sum += 300
elif ch1 == "2":
    sum += 350
elif ch1 == "3":
    sum += 400
ch2 = input("是否加點第二份, 原味+$50, 其他口味+$100(輸入:y or n)\n")
if ch2 == "y":
    if ch1 == "1":
        sum += 50
    else:
        sum += 100

ch3 = input("要加點洋蔥圈+$50嗎?(輸入 y or n)\n")
if ch3 == "y":
    sum += 50

ch4 = input("要加點薯條+$80嗎?(輸入 y or n)\n")
if ch4 == "y":
    sum += 80

if ch2 == "y" and ch3 == "y" and ch4 == "y":
    sum -= 30

print(f"總金額：{sum}, 謝謝使用自動點餐系統")


#判斷積數或是偶數
#num = int(input("input number:"))
#if num % 2 == 1:
#    print("積數")
#else:
#    print("偶數")
#建立一個更好的計算機

'''
num1 = int(input("input num1:"))
num2 = int(input("input num2:"))
op = input("input operator syntax:")
total = 0
if op == "+":
    total = num1 + num2
elif op == "-":
    total = num1 - num2
elif op == "*":
    total = num1 * num2
elif op == "/":
    total = num1 / num2

print(f"sum={total}")

'''

'''
score = int(input("input score:\n"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
'''

'''
score1 = 60
score2 = 100
score3 = 100
if score1 >90 and score1 <=100:
    print("A+")
else:
    print("E")
'''

#if

#if else

#if elif else


#邏輯運算
# #>, <, >=, <=, ==, !=
# and or not
a = 100
b = 100
#if a==100 and b == 100:
#    print("OK")
#if a==100 or b == 100:
#    print("OK")
#if not a==100:
