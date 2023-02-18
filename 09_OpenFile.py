#檔案的讀取和寫入
#檔案的讀&寫
#open("檔案路徑", mode = "開啟模式")
#絕對路徑
#相路路徑

#mode = "r" read
#mode = "w" write
#mode = "a" append
import json
import toolsBox
def openFileTxt_1():
    #file = open("123.txt", mode="r", encoding="utf-8")
    #print(file.read())
    #file.close()

    file = open("123.txt", mode="a", encoding="utf-8")
    file.write("小白, 100")
    file.close()

def openFileTxt_2():
    fileCtrl = input("(r)讀取/(w)覆寫寫入/(a)新增:\n")
    if fileCtrl == "r":
        with open("123.txt", mode="r", encoding="utf-8") as file:
            for line in file:
             print(line)
            #print(type(file.readline()))
            #print(type(file.readlines()))
            #print(file.read())
    elif fileCtrl == "w":
        with open("123.txt", mode="w", encoding="utf-8") as file:
            file.write("小金,88")
    elif fileCtrl == "a":
        with open("123.txt", mode="a", encoding="utf-8") as file:
            file.write("小金,88")

file_name = "myData//123.json"
def menu():
    print("歡迎使用帳號、密碼管理系統")
    print("=========================")
    print("1. 新增key & value")
    print("2. 刪除key & value")
    print("3. 修改key & value")
    print("4. 查詢key & value")
    print("0. 結  束  程  式")
    print("=========================")
def loadData():
    global file_name
    with open(file_name, mode="r", encoding="utf-8") as file:
        tmpData = file.read()
        if tmpData == "":
            #print("a")
            return {}
        else:
            #print("b")
            return json.loads(tmpData)
def insertData(name, uid, pwd):
    global file_name
    tmpData = loadData()
    if chkData(tmpData, name):
        newData = {
                "uid": uid,
                "pwd": pwd
        }
        tmpData[name] = newData
        #print(tmpData)
        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(tmpData, ensure_ascii=False, indent=2))
        return True
    else:
        return False
def deleteData(name):
    global file_name
    dchk = ""
    password = loadData()
    if chkData(password, name):
        return False
    else:
        dchk = input("你確定要刪除嗎?y or n\n")
        if dchk == "y" or dchk == "Y":
            del password[name]
            # print(f"del password:{password}")
            with open(file_name, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(password, ensure_ascii=False, indent=2))
            return True
def updateData(name, uid, pwd):
    global file_name
    password = loadData()
    if chkData(password, name):
        return False
    else:
        password[name]["uid"] = uid
        password[name]["pwd"] = pwd
        print(f"帳號:{uid}, 密碼:{pwd}")
        print("=========================")
        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(password, ensure_ascii=False, indent=2))
        return True
def select(name):
    password = loadData()
    if chkData(password, name):
        return False
    else:
        uid = password[name]["uid"]
        pwd = password[name]["pwd"]
        print(f"帳號:{uid}, 密碼:{pwd}")
        return True
def chkData(tmpData, name):
    if name in tmpData.keys():
        return False
    else:
        return True
def openFileJSON():
    password = {
        "google": {
            "uid": "ryan",
            "pwd": "q1w2e3r4"},
        "yahoo": {
            "uid": "yellow",
            "pwd": "z1x2c3v4"},
        "maopa": {
            "uid": "flower",
            "pwd": "a1s2d3f4"}
    }
    #print(type(password))
    """
    json.dumps(password)
    print(password)
    """
    sel = ""
    chkPwd = ""
    sel = ""
    while True:
        menu()
        sel = input("請選擇要使用的功能:\n")
        if sel == "1": #新增
            name = input("輸入帳號名稱:")
            uid = input("輸入使用者帳號:")
            chkPwd = input("是否由密碼產生器生成(y/n)")
            if chkPwd == "y":
                pwd = toolsBox.pwdCreate()
                pwd += input("輸入使用者密碼:" + pwd)
                # print(f"1:value:{value}")
            else:
                pwd = input("輸入使用者密碼:")
            if insertData(name, uid, pwd):
                print("新增完成")
            else:
                print("新增失敗, 己經有同樣的資料")
        elif sel == "2": #刪除
            name = input("輸入刪除名稱:")
            if deleteData(name):
                print("刪除完成")
            else:
                print("無此帳號")
            # pass
            #deleteData(name)
        elif sel == "3": #修改
            name = input("輸入帳號名稱:")
            uid = input("輸入使用者帳號:")
            chkPwd = input("是否由密碼產生器生成(y/n)")
            if chkPwd == "y":
                pwd = toolsBox.pwdCreate()
                pwd += input("輸入使用者密碼:" + pwd)
                # print(f"1:value:{value}")
            else:
                pwd = input("輸入使用者密碼:")
            if updateData(name, uid, pwd):
                print("修改完成")
            else:
                print("無此帳號")
            #updateData(name, uid, pwd)
        elif sel == "4": #查詢
            name = input("輸入查詢名稱:")
            if select(name):
                print("=======查詢完成=============")
            else:
                print("無此帳號")
            #for line in password:
            #    print(f"{line}, {password[line]}")
        else: #離開
            break
def invoice():
    myInv = open("我的發票.txt", mode="r", encoding="utf-8").read().split()
    #with open("我的發票.txt", mode="r", encoding="utf-8") as f1:
    #    myInv = f1.read().split()
    mapInv = open("中獎號碼.txt", mode="r", encoding="utf-8").read().split()
    #with open("中獎號碼.txt", mode="r", encoding="utf-8") as f2:
    #    mapInv = f2.read().split()
    for i, num in enumerate(myInv):
        #print(f"i:{i}, num:{num}")
        if num in mapInv:
            print('第', i + 1, '張發票對中號碼', num, '!')
def invoice_2():
    myInv = open('我的發票2.txt').read().split()
    mapInv = open('中獎號碼2.txt').read().split()

    for i, num in enumerate(myInv):
        for win_num in mapInv:
            #print(f"win_num:{win_num}")
            if num[-5:] == win_num[-5:]:
                print('第', i + 1, '張發票對中號碼', num[-5:], '!')
            elif num[-4:] == win_num[-4:]:
                print('第', i + 1, '張發票對中號碼', num[-4:], '!')
            elif num[-3:] == win_num[-3:]:
                print('第', i + 1, '張發票對中號碼', num[-3:], '!')
def myOpenCsv():
    import csv
    # with open('eggs.csv', 'w', newline='') as csvfile:
    #    spamwriter = csv.writer(csvfile, delimiter=' ',
    #                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')

        print(type(spamreader))
        for row in spamreader:
            # print(spamreader)
            # print(type(spamreader))
            # print(row)
            # print(type(row))
            print(''.join(row))
def test1():
    with open("myData//345.txt", mode="r", encoding="utf-8") as file:
        sum = 0
        #print(type(file.read()))
        for line in file.read().split():
            #print(line)
            sum += int(line)
        print(f"sum:{sum}")
#openFileTxt_1()
#openFileTxt_2()
openFileJSON()
#invoice()
#invoice_2()
#test1()
#scores = [100,200,300,400,500]
#i = 0
#for key in scores:
#    i += 1
#    print(f"i:{i}, key:{key}")
#    #print(f"i:{i+1}, j:{j}")

# https://www.json.org/json-en.html
# https://jsonformatter.org/json-editor
with open("myData//123.json", mode="r", encoding="utf-8") as f:
    tmpData = json.loads((f.read()))
    name = "sym"
    tmpData[name] = {
        "uid":"red",
        "pwd":"456"
    }
    print(tmpData)
with open("myData//123.json", mode="w", encoding="utf-8") as x:
    print(type(tmpData))
    x.write(json.dumps(tmpData, indent=2))
print(tmpData)
# d = [x **2 for x in range(1, 11)]
# print('d =', d)

# with open("myData//234.txt", mode="w", encoding="utf-8") as f:
#     myData = {
#         "uid":"ryan",
#         "pwd":"123",
#         "high":180,
#         "weight":80
#     }
#     f.write(str(myData))

# with open("myData//aaa.json",mode="r", encoding="utf-8") as f:
#     xxx = json.loads(f.read())
#     print(xxx)
    # xxx = f.read()
    # print(type(xxx))
    # aaa = json.loads(xxx)
    # print(f"type:{type(aaa)}, aaa:{aaa}")
    # # xxx = json.loads((f.read()))
    # tmpData = '{"uid":"aaa","pwd":"ccc"}'
    # xxx = json.loads(tmpData)
    # print(xxx)
    # print(type(xxx))
    #tmpDict = json.loads(f.read())
    #print(tmpDict)
    #print(type(tmpDict))
    #print(tmpDict['uid'])