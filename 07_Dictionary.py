# 單字練習機
# dictionary
# dict 主要在快速查詢特定資源使用
# 利用陣列 或 字串的觀念來帶
# name = "abcdefg"
# names = ["ryan", "jay", "john", "benson"]
# 基本上是由大括號{ }所包成的, 並由key & value 所組成的
# 特性如下
#   Key 不可重複 具有可變性 無順序性
#     -但可使用 Key 進行索引
#     -在 Key 查找時，一律使用中括弧[ ]
# 常見的功能
#   查詢 x 是否存在 x in dict *x 是 key
#   查詢資料 dict[“key”]
#   新增 / 更改資料 dict[“key”]=“value”
#   刪除資料 del dict(“key”)
#   查詢 Key dict.get[“key”]
#   取得所有 Key dict.keys()
#   取得所有 Value dict.values()
#   取得所有 (Key, Value) 的數對 dict.items()

# https://selflearningsuccess.com/python-dictionary/
def queryDic(query):
    dic = {"apple":"蘋果", "banala":"香蕉", "cat":"小貓", "dog":"小狗", "pig":"小豬"}
    for i in dic:
        #print(i)
        #print(query)
        if query == i:
            print(dic[i])

def Dic2():
    dic = {"score":[1,2,3]}
    print(dic)
    print(dic["score"])

def demo_A():
    myDict = {
        "蘋果": "apple",
        "香蕉": "banana",
        "狗": "dog",
        "age": 25,
        "score": 77.8,
        "isMale": True,
        0: "你好",
        2.5: "Hello World"
    }
    #print(myDict["age"])
    print(f"keys:{myDict.keys()}")
    print(f"values:{myDict.values()}")
    print(f"items:{myDict.items()}")
def demoDic():
    dinDic = {
        "蘋果":"apple",
        "香蕉":"banana",
        "狗":"dog",
        "age":25,
        "score":77.8,
        "isMale":True,
        0:"你好",
        2.5:"Hello World",
        "test":{
            "A":10,
            "B":"eng",
            "C":"中英"
        }
    }
    print(dinDic)
    demoddd = {}
    demoddd["小黑"] = "{'High':100, 'Wight':88}"
    print(f"demoddd:{demoddd}")
    for key in dinDic:
        print(f"key:{key}, value:{dinDic[key]}")
        if key == "test":
            for i in dinDic[key].keys():
                print(f"  values:{dinDic[key][i]}")

def demoDic2():
    import toolsBox
    #print(toolsBox.pwdCreate())

    # afternoon_tea = [['Muffin', 39], ['Scone', 25], ['Biscuit', 20]]
    # print(afternoon_tea)
    # print(dict(afternoon_tea))

    dict = {"a":"apple",
           "b":"banana",
           "c":"cat",
           "d":"dog"
           }
    print(f"dict:{dict}")
    while True:
        menu()
        opt = ""
        key = ""
        value = ""
        chkPwd = ""
        opt = input("請選擇:\n")
        if opt == "1":  # insert
            key = input("insert key:\n")
            chkPwd = input("是否由密碼產生器生成(y/n)")
            if chkPwd == "y":
                value = toolsBox.pwdCreate()
                value += input("insert value:" + value)
                #print(f"1:value:{value}")
            else:
                value = input("insert value:")
            if key in dict:
                print("key 己經存在")
            else:
                dict[key] = value
                print(f"2:value:{value}")
        elif opt == "2":  # delete
            key = input("insert key:\n")
            del dict[key]
        elif opt == "3":  # update
            key = input("insert key:\n")
            value = input("insert value:\n")
            dict[key] = value
        elif opt == "4":  # select
            print("查詢全部(a)\n查詢某值(s)\n")
            sel = input("請選擇:\n")
            if sel == "a":
                print(dict)
            else:
                chk = input("請輸入要查詢key:\n")
                chkData = True
                for i in dict:
                    if chk == i:
                        print(f"key:{i}, value:{dict[i]}")
                        chkData = True
                        break
                    else:
                        print("哈哈哈")
                        chkData = False

                if not chkData:
                    print("找不到key值")
        else:
            print("QUIT")
            break
    #xxx = dict(afternoon_tea)
    #print(xxx)
    #aaa = {x: x ** 2 for x in range(1, 11)}
    #print(f"aaa:{aaa}")
    #bbb = dict([(i, chr(65 + i)) for i in range(26)])
    # {i : chr(65+i) for i in range(26)}
    #print(f"bbb:{bbb}")

    # print({k: v for k, v in someDict.iteritems()} == someDict.copy())
    #print({x: x ** 2 for x in range(1, 4)})
    #print(dic.keys())
    #print(dic.values())
    #print(dic.items())
    #for key in dic:
    #    print(f"key:{key}")

    #for key, value in dic.items():
    #    print(f"key:{key}, value:{value}")

def test1():
    cusSp = {
        "小黑":1000,
        "小黃":2000,
        "小花":3000,
        "小白":4000,
        "小金":5000,
        "小藍":2500,
        "小紅":6000
    }
    print(cusSp)

    for cus in cusSp:
        #print(cusSp[cus])
        if cusSp[cus] >= 3000:
            cusSp[cus] = "VIP"
        else:
            cusSp[cus] = "一般"
    print(cusSp)
def test2():
    std = {
        "小黑":{
            "High":173,
            "Weight":75
        },
        "小黃":{
            "High":160,
            "Weight":45
        }
    }

    #print(std["小黑"])
    #print(std.get("小黑"))
    print(std.keys())
    xxx = list(std)
    print(f"xxx:{xxx}")
    yyy = list(std[xxx[0]].keys())
    print(f"yyy:{yyy}")
    #xxx = list(std["小黑"].keys())
    #print(type(xxx))
    #print(xxx)
    selName = input("enter query name:\n")
    for i in xxx:
        #print(f"i:={type(i)}, std[i]:{type(std[i])}")
        #print(i)
        if i == selName:
            for j in yyy:
                print(f"{j}, {str(std[i][j])}")
            break
        else:
            print("not fund data")
            #break
def test3():
    import random
    eng_dic = {
        "蘋果": "apple",
        "香蕉": "banana",
        "貓": "cat",
        "狗": "dog",
        "蛋": "egg",
        "食物": "food",
        "遊戲": "game",
        "手": "hand",
        "冰": "ice",
        "果醬": "jam",
        "國王": "king",
        "標籤": "label",
        "郵件": "mail",
        "脖子": "neck",
        "油": "oil",
        "豬": "pig",
        "皇后": "queen"
    }
    #print(eng_dic)
    #print(eng_dic.keys())
    #print(list(eng_dic))
    questionNum = int(input("請問要練習幾次:\n"))
    count = 0
    for i in range(1, questionNum+1):
        questions = list(eng_dic)
        random_question = questions[random.randint(0,len(questions)-1)]
        ans = input(f"請問這個題目:「{random_question}」的英文是:\n")
        if eng_dic[random_question] == ans:
            print("答對了")
            count += 1
        else:
            print(f"對錯了,{random_question}的英文是:{eng_dic[random_question]}")
    print(f"總共{questionNum}題,答對了{count}題")
def test4():
    dic = {
        "小黑":{
            "High":172,
            "Weight":80
        },
        "小黃":{
            "High":158,
            "Weight":45
        },
        "小花":{
            "High":168,
            "Weight":55
        },
        "小白":{
            "High":180,
            "Weight":75
        }
    }
    #print(dic.keys())
    #print(dic.values())
    for i in dic.keys():
        print(f"i:{type(i)}")
        print(f"name:{i}")
        print(f"values:{dic[i]}")
        for j in dic[i]:
            print(f"  {j}:{dic[i][j]}")

#demo_A()
#plusControl()
#Dic2()
#test1()
#test2()
test3()
#test4()
#demoDic2()
#queryDic(input("enter a words(apple, banala, cat, dog, pig)\n"))

engDict = {
    "小黑":"apple",
    1:"banana",
    2:"cat",
    3:"dog",
    4:"english",
    5:"foot",
    6:"good",
    7:["a","b","C"],
    8.2:"hi",
    "isBoy":True,
    "name":{
        "UID":"aaa",
        "PWD":"12345"
    }
}
#print(engDict)
#print(engDict[7][0])
#print(list(engDict))
#for key in engDict:
#    print(f"{key}:{engDict[key]}")
    #print(type(key))
    #print(f"{key}:{engDict[key]}")
    #if key == 7:
        #print(type(engDict[key]))
    #    for tmp in engDict[key]:
    #        print(f"  tmp:{type(tmp)}:{tmp}")
#engDict[7] = "hand"
#print(engDict)

#engDict[7] = {
#    "UID":"Ryan",
#    "PWD":"q1w2e3r4"
#}
#print(engDict)

students = {
    "name":["小黑", "小黃", "小花", "小白"],
    "age":{
        "小黑":20,
        "小黃":30,
        "小花":40,
        "小白":50
    }
}
#print(students["name"][0])
#print(students["age"]["小花"])

students_list = [
    {
        "name":"小黑",
        "age":20
    },
    {
        "name":"小黃",
        "age":39
    },
    {
        "name":"小花",
        "age":40
    },
    {
        "name":"小白",
        "age":50
    }
]
#print(f"{students_list[0]['name']}, {students_list[0]['age']}")
# 字典常搭配的函式
# dict.keys
# dict.values
# dict.items
print(f"keys:{engDict.keys()}")
print(f"keys:{list(engDict.keys())[0]}")
print(f"keys:{list(engDict)}")
for key,value in list(engDict.items()):
    #pass
    #print(key)
    #print(value)
    print(f"key:{key}, value:{value}")

print(f"values:{engDict.values()}")
#print(f"values:{list(engDict.values())}")
print(f"items:{engDict.items()}")
#print(f"items:{list(engDict.items())}")

#tmpDict = {key:value}
tmpDict = {
    "apple":"蘋果",
    1:"banana"
}
print(tmpDict["apple"])
print(tmpDict[1])
print(tmpDict)
names = ["ryan", "jay",1]
print(names)

