#while

#for
#range
import random
import toolsGraph
#密碼產生器
def pwdCreate():
    chrUpper = int(input("幾個大寫的字:"))
    chrLower = int(input("幾個小寫的字:"))
    chrNumber = int(input("幾個數字:"))
    chrSyntax = int(input("幾個符號:"))
    pwd = ""
    tmp = ""
    countUpper = len(toolsGraph.letters_upper)
    countLower = len(toolsGraph.letters_lower)
    countNumber = len(toolsGraph.numbers)
    countSyntax = len(toolsGraph.symbols)
    #print(f"countUpper:{countUpper}")
    for i in range(chrUpper):
        pwd += random.choice(toolsGraph.letters_upper)
        #pwd += toolsGraph.letters_upper[random.randint(0, countUpper-1)]
        #tmp = toolsGraph.letters_upper[random.randint(0, countUpper-1)]
        #pwd.append(tmp)
    for i in range(chrLower):
        pwd += random.choice(toolsGraph.letters_lower)
        #pwd += toolsGraph.letters_lower[random.randint(0, countLower - 1)]
        #tmp = toolsGraph.letters_lower[random.randint(0, countLower-1)]
        #pwd.append(tmp)
    for i in range(chrNumber):
        pwd += random.choice(toolsGraph.numbers)
        #pwd += toolsGraph.numbers[random.randint(0, countNumber - 1)]
        #tmp = toolsGraph.numbers[random.randint(0, countNumber-1)]
        #pwd.append(tmp)
    for i in range(chrSyntax):
        pwd += random.choice(toolsGraph.symbols)
        #pwd += toolsGraph.symbols[random.randint(0, countSyntax - 1)]
        #tmp = toolsGraph.symbols[random.randint(0, countSyntax-1)]
        #pwd.append(tmp)
    print(f"pwd:{pwd}")
    pwd = list(pwd)
    print(f"pwd:{pwd}")
    random.shuffle(pwd)
    print(f"pwd:{pwd}")
    tmp = "".join(pwd)
    #for i in pwd:
    #    tmp += i
    print(f"pwd:{tmp}")

#BMI
def BMI():
    chk = True
    while chk:
        high = float(input("請輸入身高:\n"))#/100
        weight = float(input("請輸入體重:\n"))
        #print(type(high))
        #print(f"a:high:{high} weight:{weight}")
        xBMI = round(weight/(high/100)**2, 1)
        print(f"你的BMI:{xBMI}")
        if xBMI >= 35:
            print("重度肥胖")
        elif xBMI >= 30:
            print("中度肥胖")
        elif xBMI >= 27:
            print("輕度肥胖")
        elif xBMI >= 24:
            print("體重過重")
        elif xBMI >= 18:
            print("正常體重")
        else:
            print("體重太輕")
        if (input("continue scale BMI y or n\n").lower() == "n"):
            chk = False

#擲骰子
def playDice():
    chkPlay = True
    while chkPlay:
        guess = int(input("猜骰子(1:大) 或 (2:小)\n "))
        play = 0
        num = 0
        play =random.randint(1, 6)

        #print(dice[play-1])

        print(f"computer:{play}")
        if (guess == 2 and play == 1) or (guess == 2 and play == 2) or (guess ==2 and play == 3):
            print("you win & 小")
        elif(guess == 1 and play == 4) or (guess == 1 and play == 5) or (guess ==1 and play == 6):
            print("you win & 大")
        else:
            print("you lose")

        #print(play)
        print(toolsGraph.dice[play-1])
        if input("是否繼續玩 y or n\n") == "n":
            chkPlay = False
            print("Gave over")

#找出最高的成績
def find_high_score():
    scores = input("輸入學生成續, 用逗號隔開:\n").split(",")
    high_score = 0
    print(f"scores:{scores}")
    for i in scores:
        i = int(i)
        if i > high_score:
            high_score = i
    print(f"high score:{high_score}")

#find data
#def scoreQuery(name):
def scoreQuery():
    score = [
        ["小黑", 65],
        ["小黃", 90],
        ["小花", 80],
        ["小白", 95],
        ["小金", 100]
    ]
    count = 3
    i =0
    tmpScores = []
    while i < count:
        scores = input("請輸學生的姓名與成續, 用逗號隔開\n").split(",")
        tmpScores.append(scores)
        i += 1
    score = tmpScores
    #print(score)

    name = input("請輸入要查詢學生的名子:\n")
    chkData = False
    for scoreName in score:
        #print(scoreName)
        if name == scoreName[0]:
            #print("Go")
            chkData = True
            print(f"name:{scoreName[0]}, score:{scoreName[1]}")

    if not chkData:
        print("找不到這位學生")

#計算積數 偶數的合
def oddEven():
    odd = 0
    even = 0
    for i in range(1,101):
        if i % 2 == 1:
            even += i
            #print(f"even:{i}")
        elif i % 2 == 0:
            odd += i
            #print(f"odd:{i}")

    #for i in range(1,11,1):
    #    print(i)
    #    odd += i
    print(f"ODD={odd}, EVEN={even}")

def myWhileDemo():
    i = 1
    blChk = True
    while blChk:
        print(f"i:{i}")
        i +=1
        if i == 5:
            blChk = False

def myForDemo1():
    for i in "毛爸咖啡":
        print(f"進入迴圈, i={i}")
    print("迴圈結朿")

    for j in ["小黑", "小白", "小黃", "小花"]:
        print(f"進入迴圈,Hello {j}")
    print("迴圈結朿")

def myForDemo2():
    import numpy as np
    scores = [1,2,3,4,5,6,7,8,9,10]
    #scores = np.random.randint(60,100,20)
    tmpLen = len(scores)
    print(f"scores:{scores}, tmpLen:{tmpLen}")
    sum = 0
    for score in scores:
        sum += score
    print(f"sum:{sum}, 平均:{round(sum/tmpLen,2)}")

#scoreQuery(input("enter a name go score:\n"))
#guessNumber()
#oddEven()
#findMax()
#for
#Range function

#pwdCreate()
#name = "ABC"
#print(name)
#print(type(name))
#tmp = list(name)
#print(tmp)
#print(type(tmp))
#tmp = "".join(tmp)
#print(type(tmp))
#print(tmp)
#name = "ryan"
#name = list(name)
#print(name)
#name = "".join(name)
#print(name)
#BMI()
#find_high_score()
#oddEven()

#playDice()
#myWhileDemo()
#myForDemo2()
#find_high_score()
#scoreQuery("小白")
scoreQuery()
#tmp = []
#x = "小黑"
#y = 88
#tmp.append([x, y])
#x = "小白"
#y = 66
#tmp.append([x, y])
#print(tmp)
#for i in tmp:
#    print(f"i:{i}")
#oddEven()