#問答程式
# class 定義一個新的資料型態, include base type and function
# 使用class 建立的變數為物件型態Object
# class 類別 object 物件 attribute 屬性 或 變數
# def 初始函數 __init__
# def methon 方法
# description, answer
# func ask

class Phone:
    def __init__(self, num, name, price, waterproof):
        print("初始函式")
        self.num = num
        self.name = name
        self.price = price
        self.waterproof = waterproof

class PhoneA:
    def __init__(self, num, name, price, waterproof, power):
        self.num = num
        self.name = name
        self.price = price
        self.waterproof = waterproof
        self.power = power
    def play(self, num):
        self.power -= num
        if self.power <= 0:
            self.power = 0

# test1
# create a class Question
# attribute 2 description, answer
# method ask print question return right True or False
class Question:
    description = ""
    answer = ""
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

    def ask(self):
        ans = input(self.description)
        if ans == self.answer:
            return True
        else:
            return False

# test2
# create class QuestionGame
# attribute questions, score
# method play, print question and get, output score
class QuestionGame:
    questions = 0
    score = 0

    def __init__(self, questions, score):
        self.questions = questions
        self.score = score

    def play(self):
        for question in self.questions:
            if question.ask():
                print("答對了")
                self.score += 1
            else:
                print(f"答錯了, 答案是{question.answer}")
        print(f"共答對了{self.score}題")

# project
# QuestionGame add method random_pick 可以隨機挑選幾題
# play 可以隨機挑選題目讓使用者回題
# finish
import random
import json
class PrjQuestionGame:
    questions = 0
    score = 0
    def __init__(self, questions, score):
        self.questions = questions
        self.score = score
    def play(self, num):
        random_question = self.random_pick(num)
        for question in random_question:
            if question.ask():
                print("答對了")
                self.score += 1
            else:
                print(f"答錯了, 答案是{question.answer}")
        print(f"共{num}題, 答對了{self.score}題")
    def random_pick(self, num):
        random_questions = random.sample(self.questions, num)
        print(type(random_questions))
        return random_questions

# phone1 = Phone()
# phone1.num = "123456"
# phone1.price = 19800
# phone1.waterproof = True
# print(f"num:{phone1.num}, price:{phone1.price}, waterproof:{phone1.waterproof}")
#
# phone2 = Phone()
# phone2.num = "456789"
# phone2.price = 25800
# phone2.waterproof = False
# print(f"num:{phone2.num}, price:{phone2.price}, waterproof:{phone2.waterproof}")

# 二
# phone1 = Phone("100001", "google", 2000, True )
# print(f"num:{phone1.num}, name:{phone1.name}, price:{phone1.price}, waterproof:{phone1.waterproof}")
#
# #create and add update member
# phone1.year = 2023
# phone1.num = "0919"
# print(phone1.num)
# print(phone1.year)

# 三
# phone3 = PhoneA("100001", "google", 2000, True, 80)
# print(phone3.power)
# phone3.play(20)
# print(phone3.power)

# test1
# question = Question("請問1+1=???\n(a)2\n(b)3\n(c)4\n-->","a")
# if question.ask():
#     print("答對了")
# else:
#     print("答錯了")

# test2
# question1 = Question("請問1+1=???\n(a)2\n(b)3\n(c)4\n-->","a")
# # print(f"question1:{type(question1)}")
# question2 = Question("請問2+2=???\n(a)2\n(b)3\n(c)4\n-->","c")
# question3 = Question("請問3+3=???\n(a)5\n(b)6\n(c)7\n-->","b")
# questions = [question1, question2, question3]
# question_game = QuestionGame(questions, 0)
# question_game.play()

# project test
file_name = "myData//questions.json"
with open(file_name, mode="r", encoding="utf-8") as file:
    question_list = json.loads(file.read())
# print(question_list)
questions = []
for question in question_list:
    des = question["description"]
    ans = question["answer"]
    qq = Question(des, ans)
    questions.append(qq)
print(questions)

print("====問題遊戲====")
num = int(input("要做幾題:\n"))
prjQuestionGame = PrjQuestionGame(questions, 0)
prjQuestionGame.play(num)

# class Personal:
#     def __init__(self, name, high, weigh):
#         print("begin function")
#         self.name = name
#         self.high = high
#         self.weight = weigh
#     def sayHello(self, name):
#         print(f"Hello {name}")


# p1 = Personal("name", 172, 80)
# # print(type(p1))
# # p1.name = "ryan"
# # p1.high = 172
# # p1.weight = 80
# # p1.isboy = True
# print(p1.name)
# print(p1.high)
# print(p1.weight)
# p1.sayHello("jay")
# # print(p1.isboy)