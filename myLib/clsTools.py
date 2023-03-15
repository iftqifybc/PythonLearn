import json
class CreateUidPwd:
    def __init__(self):
        self.filePath = "myData//create.json"
    def insert(self, name, uid, pwd):
        tmpData = self.__loadData()
        if self.__chkData(tmpData, name):
            newData = {
                "uid": uid,
                "pwd": pwd
            }
            tmpData[name] = newData
            # print(tmpData)
            with open(self.filePath, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(tmpData, ensure_ascii=False, indent=2))
            return True
        else:
            return False
    def delete(self):
        pass
    def update(self):
        pass
    def select(self, name):
        password = self.__loadData()
        if self.__chkData(password, name):
            print("無此帳號")
        else:
            # print(password)
            uid = password[name]["uid"]
            pwd = password[name]["pwd"]
            print(f"帳號:{uid}, 密碼:{pwd}")
            print("=========================")
    def __loadData(self):
        with open(self.filePath, mode="r", encoding="utf-8") as file:
            tmpData = file.read()
            if tmpData == "":
                return {}
            else:
                return json.loads(tmpData)
    def __chkData(self, tmpData, name):
        if name in tmpData.keys():
            return False
        else:
            return True
    def menu(self):
        print("歡迎使用帳號、密碼管理系統")
        print("=========================")
        print("1. 新增key & value")
        print("2. 刪除key & value")
        print("3. 修改key & value")
        print("4. 查詢key & value")
        print("0. 結  束  程  式")
        print("=========================")