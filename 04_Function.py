#綜合健康計算機
#https://toolboxtw.com/ja/calculator/bmr

#function 的四種型態
#functionName(name="ryan", hith="173", weight="75")
#傳入參數可對抰名稱, 預防傳錯對象

#型態一:不需要傳入參數
#型態二:需要傳入參數
#型態三:丕需要傳入參數, 需要回傳資料
#型態四:需要傳入參數, 需要回傳資料

def printMyData():
    print("哈囉，我叫毛毛")
    print("身高180")
    print("體重100")
    print("年齡28")
#練習把這個函式改成需要傳入參數

#BMI = 體重 / 身高的平方
def BMI(high, weight):
    #high = float(input("請輸入身高:\n"))/100
    #weight = float(input("請輸入體重:\n"))
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

#基礎代謝率計算公式（BMR計算公式）
#男性	66 + （13.7 × 體重（kg） + 5 × 身高（公分） - 6.8 × 年齡）
#女性	655 + （9.6 × 體重（kg） + 1.8 × 身高（公分） - 4.7 × 年齡）
def BMR(sex, age, high, weight):
    scale = 0
    if sex == 1:
        scale = 66 + (13.7 * weight) + (5 * high) - (6.8 * age)
    else:
        scale = 655 + (9.6 * weight) + (1.8 * high) - (4.7 * age)
    #print(f"BMR:{scale}")
    return scale

#TDEE計算公式（每日總消耗熱量計算公式）
#久坐、幾乎沒運動	BMR X 1.2
#每週低強度運動1~3天	BMR X 1.375
#每週中強度運動3~5天	BMR X 1.55
#每週高強度運動6~7天	BMR X 1.725
#勞力密集工作或是每天高強度訓練	BMR X 1.9
def TDEE(sex, age, high, weight,sport):
    scale = 0
    xBMR = 0
    xBMR = BMR(sex, age, high, weight)
    if sport == 1:
        scale = xBMR * 1.2
    if sport == 2:
        scale = xBMR * 1.375
    if sport == 3:
        scale = xBMR * 1.55
    if sport == 4:
        scale = xBMR * 1.725
    if sport == 5:
        scale = xBMR * 1.9
    #print("TDEE test")
    return scale

#main code
def myMainCode():
    print("綜合健康管理系統")
    set = ["00110","11110","11111"]
    i = int(input("請選擇BMI(1) BMR(2) TDEE(3)>"))
    i -= 1
    sex = 0
    age = 0
    high = 0
    weight =0
    sport = 0
    #print(set[i])
    #print(type(set[i]))
    if set[i][0] == "1":
        sex = int(input("請輸入性別(男:1 or 女:2)>"))
    if set[i][1] == "1":
        age = int(input("請輸入年齡>"))
    if set[i][2] == "1":
        high = float(input("請輸入身高>"))
    if set[i][3] == "1":
        weight = float(input("請輸入體重>"))
    if set[i][4] == "1":
        print("1:久坐、幾乎沒運動")
        print("2:每週低強度運動1~3天")
        print("3:每週中強度運動3~5天")
        print("4:每週高強度運動6~7天")
        print("5:勞力密集工作或是每天高強度訓練")
        sport = int(input("請輸入運動類別>"))

    if i == 0:
        print(f"high:{high} weight:{weight}")
        BMI(high, weight)
    elif i == 1:
        print(f"BMR:{BMR(sex, age, high, weight)}")
    elif i == 2:
        print(f"TDEE:{TDEE(sex, age, high, weight, sport)}")
#
#找出最大值
def findMax(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"num1 max:{num1}")
    elif num2 > num3 and num2 > num1:
        print(f"num2 max:{num2}")
    elif num3 > num1 and num3 > num2:
        print(f"num3 max:{num3}")

def findMax2(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

#找出最小值
def findMin(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3 and num2 < num1:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3

def findMaxAndMin(num1, num2, num3):
    print("findMaxAndMin")
    x = findMax2(num1, num2, num3)
    y = findMin(num1, num2, num3)
    return x - y

myMainCode()
#tBMR = BMR(1, 45, 173,75)
#print(f"BRI:{tBMR}")
#xTDEE = TDEE(1, 45, 173,75,5)
#print(f"TDEE:{xTDEE}")
#printMyData()
#print(findMin(1,2,3))
#print(findMax2(10,20,30))
#print(findMaxAndMin(10,30,50))