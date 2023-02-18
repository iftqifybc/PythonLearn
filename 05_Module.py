#剪刀 石頭 布
#猜硬幣
#抽籤吃什麼
#擲骰子
#Module
#Random module
#List and split()
#巢狀列表二維陣列/三維陣列(多維陣列)
#3引號字串
import random
import toolsGraph as srh

#擲硬幣
def guessCoin():
    guess = int(input("請猜硬幣的(1:正面  2:反面)"))
    a = random.randint(1,2)
    if (a == 1 and guess == 1) or (a==2 and guess == 2):
        print("猜對了")
    else:
        print("猜錯了")

    if a == 1:
        print(f"正面:{a}")
    else:
        print(f"反面:{a}")

#抽籤點餐
def lottery():
    tmp = input("請輸入想吃的晚餐, 用逗號隔開>>>").split(",")
    #print(len(tmp))
    #print(tmp[0])
    print(f"晚餐可以吃:{tmp[random.randint(0,len(tmp))-1]}")

    #print("lottery test")

def createList():
    num = [1,2,3]
    print(num)
    num = [[21,22,23],[24,25,26],[27,28,29]]
    print(num)
    num = [[[311,312,313],[314,315,316],[317,318,319]],[4,5,6],[7,8,9]]
    print(num)
    std1 = ["apple", 1, 2, 3]
    std2 = [
                ["apple", 1, 2, 3],
                ["banala", 4, 5, 6],
                ["lemo", 7, 8, 9]
            ]
    std3 = [
        [
            ["apple", 1, 2, 3],
            ["banala", 4, 5, 6],
            ["lemo", 7, 8, 9]
        ],
        [
            ["dog", 11, 21, 31],
            ["pig", 41, 51, 61],
            ["cat", 71, 81, 91]
        ]
    ]
    print(std1)
    std1.append(4)
    print(std1)
    std1.insert(2,5)
    print(std1)

    #將 List 作為 Stack（堆疊）使用
    std1.pop()
    std1.pop()
    print(f"pop:{std1}")

    #將 List 作為 Queue（佇列）使用
    #from collections import deque
    #queue = deque(["Eric", "John", "Michael"])
    #queue.append("Terry")  # Terry arrives
    #queue.append("Graham")  # Graham arrives
    #print(queue)

    # List Comprehensions（串列綜合運算）
    #squares = []
    #for x in range(10):
    #    squares.append(x ** 2)
    #print(squares)
    #print(queue.popleft())

    #matrix = [
    #    [1, 2, 3, 4],
    #    [5, 6, 7, 8],
    #    [9, 10, 11, 12],
    #]
    #print([[row[i] for row in matrix] for i in range(4)])
    #print(std2)
    #std2.append(["juice", 10, 20, 30])
    #print(std2)

    #print(std3[0])
    #std3[0].append(["juice",10,20,30])
    #print(std3[0])
#剪刀 石頭  布
def srp():
    #print("srh")
    comp = "srh"
    z = random.randint(0,2)
    x = input("請輸入(剪刀:s, 石頭:r, 布:h)\n")
    y = comp[z]
    tmpData = {"s":"剪刀", "r":"石頭", "h":"布"}
    print(f"你出:{tmpData[x]}, 電腦:{tmpData[y]}")
    '''
    if x == "s":
        print(srh.scissor)
    elif x == "r":
        print(srh.rock)
    elif x == "h":
        print(srh.hand)

    if y == "s":
        print(srh.scissor)
    elif y == "r":
        print(srh.rock)
    elif y == "h":
        print(srh.hand)
    '''
    if (x == "s" and y == "h") or\
       (x == "r" and y == "s") or\
       (x == "h" and y == "r"):
        print("you win")
    elif(x == "s" and y == "s") or\
        (x == "r" and y == "r") or\
        (x == "h" and y == "h"):
        print("平手")
    else:
        print("you lose")
def srp_2():
    i = 0
    while i<=10:
        myArray = ["剪刀", "石頭", "布"]
        mySel = input("enter 剪刀(s)石頭(r)布(p):\n")
        if mySel == "s":
            mySel  = 0
        elif mySel == "r":
            mySel = 1
        else:
            mySel =2
        cpu = random.randint(0,2)
        print(f"你出:{myArray[mySel]}, 電腦出:{myArray[cpu]}")
        if mySel == (cpu + 1) % 3:
            print("you win")
        elif cpu == (mySel +1) %3:
            print("you lose")
        else:
            print("pace")
        i += 1
#guessCoin()
#queryDic(input("enter(apple, banala, cat, dog, pig)"))
#toolsBox.std(input("enter name:"))
srp_2()
#lottery()
#playDice()
#createList()