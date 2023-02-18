# 猜數字遊戲
#猜數字遊戲
#left , right
def guessNumber():
    import random
    #isChk = True
    tmpNum = random.randint(1, 100)
    left = 1
    right = 100
    while True:
        print("這是一個猜數字遊戲, 範圍介於1~100")
        print(f"提示數字介於{left} and {right}")
        num = int(input("enter a number(1~100):"))
        print(f"tmpNum:{tmpNum}")
        if num > tmpNum:
            right = num
            print("數字小一點")
        elif num == tmpNum:
            print("答對了")
            break
        else:
            left = num
            print("數字大一點")

# 變數使用的範圍
#  全域變數
#  區域變數:作用域只有在function 內宣告的變數
w = 10
def f1(x, y):
    w = 20
    z = x + y
    print(f"區域變數:{z}")
#f1(10, 20)
#print(w)

def f2():
    z = 10
    print(f"全區變數:{w}")
#f2()

#是不是有做縮排的都是區域變數
#if
#if True:
#    a = 10

#print(f"if a:{a}")
#while
#chk = True
#while chk:
#    a = 10
#    chk = False
#print(f"while a:{a}")

#for
#for i in range(1):
#    a = 10
#print(f"for a:{a}")

#print(z)

#如何在函式的內部更改區域變數-＞全域變數
a = 10
def abc():
    #global a
    a = 20
    print(f"區域函式:{a}")
    #推廌的做法
    return a
#a = abc()
#print(f"全域函式:{a}")

# 測驗
def test_1(a, b):
    c = a + b
    return c
#print(test_1(10, 20))

x = 5
def test_2():
    x = 50
    return x
#x = test_2()
#print(x)

y = 10
def test_3():
    global y
    y = 50
    if 2 > 1:
        y = 100
    return y
#print(test_3())

#print(f"全域函式:{a}")
#ex 在C語言的寫法
#void main(){
#
#
# }

#迴圈 break / continue
chk = False
def breakContinumFor():
    for score in [1,2,3,4,5,6,7,8,9]:
        if score == 5:
            continue
            #if chk:
            #    break
            #else:
            #    continue
        print(f"score:{score}")
def breakContinueWhile():
    i = 1
    while i <= 6:
        if i == 3:
            i += 1
            break
        print(f"i:{i}")
        i += 1
# 測驗
#test_1(10, 20)
#print(c)

#test_2()
#print(x)

#test_3()
#print(y)
guessNumber()
#breakContinumFor()
#breakContinueWhile()
