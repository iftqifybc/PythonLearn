class Healthy:
    def __init__(self):
        pass
    def BMI(self, high, weight):
        self.bmi = round(weight / (high/100) ** 2, 1)
        print(f"BMI:{self.bmi}")
        return self.bmi
    def BMR(self, sex, high, weight, age):
        if sex == "0":
            self.bmr = 66 + (13.7 * weight) + (5 * high) - (6.8 * age)
        else:
            self.bmr = 655 + (9.6 * weight) + (1.8 * high) - (4.7 * age)
        print(f"BMR:{self.bmr}")
        return round(self.bmr,1)
    def TDEE(self, sex, high, weight, age, sport):
        self.bmr = self.BMR(sex, high, weight, age)
        if sport == "0":
            self.tdee = self.bmr * 1.2
        elif sport == "1":
            self.tdee = self.bmr * 1.375
        elif sport == "2":
            self.tdee = self.bmr * 1.55
        elif sport == "3":
            self.tdee = self.bmr * 1.75
        elif sport == "4":
            self.tdee = self.bmr * 1.9
        print(f"TDEE:{self.tdee}")
        # else:
        #     self.tdee = 0
        return round(self.tdee, 1)