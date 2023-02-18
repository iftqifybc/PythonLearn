#Python字串(string)基礎與20種常見操作
#https://selflearningsuccess.com/pythonstring/
#綜合練習 BMI計算機
#BMI = 體重 / 身高的平方
#high = float(input("請輸入身高:\n"))/100
#weight = float(input("請輸入體重:\n"))
#BMI = round(weight/high**2, 1)
#print(f"你的BMI:{BMI}")

#資料型態(int,float,string,bool,list,tuple,directionary
#同形態相加
#資料型態判斷
#print(type(1))
#print(type(1.))
#print(type(True))
#print(type("1"))
#print(type(["1","2","3"]))
#print(type(("1","2","3")))
#print(type({"1":"apple","2":"blnala","3":"Cat"}))

#運算符號
#資料型態轉換
#數字用法
#字串用法

#資料型態(int float string bool)
#各種資料型態使用時機
#int
#3
#1_000_000
#print(1_000_000)
#score = 50

#float
#4.5
#high = 173.5

#string
#'小花' 單引號
#"小花" 雙引號
#name "小黑"
#取得字串中某一個字
#name[0] name[1]
#name = "小黑"[1]
#print(name)
#print("12345"[0])
#print("12345"[1])
#print("12345"[2])
#print("12345"[3])
#print("12345"[4])

#boolean 是/否 真/假
#True or Fasle
#isBoy = True


#資料型態轉換#int() float() str()
#type 判斷資料型態使用
#加總輸入的數字
#num = input("input number:")
#sum = int(num[0]) + int(num[1])
#print(f"SUM={sum}")

#建立一個基本的計算機
#error
#num1 = input("num1:")
#num2 = input("num2:")
#print(num1 + num2) #字串相加

#num1 = int(input("number1:\n"))
#num2 = int(input("number2:\n"))
#print(f"sum={num1+num2}")

#字串的用法
#在輸出字串中使用雙引號
#print("Hello \"Ryan\"")
#print('Hello "Ryan"')
#print("\n")
#在同行字串換行

#運算符號 and #數字的用法
#+ - * /
#// 取商數
#% 取餘數
#** 幾次方
#連續運算 先乘除後加減
#可利用括號()運算先做
#round(5.1314,2) 變數, 小數第幾位
#print(15+8)
#print(15-8)
#print(15*8)
#print(15/8)
#print(15//8)
#print(15%8)
#print(5**2)
#num = num +1
#num += 1

#再探討print function
#name = "ryan"
#print(f"name:{name}")
#name = input("input name:")
#high = int(input("input high:"))
#weigh = int(input("input weigh:"))
#age = int(input("input age:"))
#print(f"hell {name}, 我的身高是{high}, 體重：{weigh}, 年齡：{age} ")

#https://selflearningsuccess.com/pythonstring/
#Python字串(string)基礎與20種常見操作
#str().upper()
#str().lower()
#len(str)
#str().isupper()
#str().islower()
#str[1:], str[1:5], str[03:]
#capitalize()：將字串的首字轉為大寫字母。
#title()：將字串中的每個單字字首轉為大寫字母。
#strip()：清除字串的前後空白。
#在字串的前面加上 r
#print(r"abcdeFG")
#print("Hell Ryan\n" * 5)
#join() 將字串結合
#replace() 替換
#index() 或 find() 找尋位置
#count() 計算出現的次數
#print("he" in "hello")