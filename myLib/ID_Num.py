import random     # import random 模組
class IDN:
    # 建立英文字和數字對照表
    local_table = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34,
                   'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
                   'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}
    chk_array = []
    local = ""
    sex = 0
    def __init__(self):
        pass
    def cre_ID_Num(self):
        local = random.choice(list(self.local_table.keys()))
        # print(local_table[local])
        chk_array = list(str(self.local_table[local]))
        # print(chk_array)
        chk_array[0] = int(chk_array[0])
        chk_array[1] = int(chk_array[1]) * 9
        sex = random.choice([1, 2])
        chk_array.append(sex * 8)
        # print(chk_array)
        nums_str = ''
        for i in range(7):
            nums = random.randint(0, 9)
            nums_str = nums_str + str(nums)
            # print(f"i:{i}, nums:{nums}, nums_str:{nums_str}")
            chk_array.append(nums * (7 - i))
        check_num = 10 - sum(chk_array) % 10
        if check_num == 10: check_num = 0
        id_number = str(local) + str(sex) + nums_str + str(check_num)  # 組合成身分證字號
        # print(id_number)
        return id_number
    def validate_ID_Num(self, id_number):
        check = False
        while True:
            try:  # 使用 try
                # print("IN")
                id_arr = list(id_number)
                if len(id_arr) != 10: break
                local = str(self.local_table[id_arr[0]])
                check_arr = list(local)
                check_arr[0] = int(check_arr[0])
                check_arr[1] = int(check_arr[1]) * 9
                sex = id_arr[1]
                if sex != '1' and sex != '2': break
                check_arr.append(int(sex) * 8)
                for i in range(7):
                    check_arr.append(int(id_arr[i + 2]) * (7 - i))

                check_num = 10 - sum(check_arr) % 10
                print(f"check_num:{check_num}, id_arr[9]:{id_arr[9]}")
                if check_num == 10: check_num = 0
                print(f"check_num:{check_num}, id_arr[9]:{id_arr[9]}")
                if check_num != int(id_arr[9]): break
                check = True
                break
            except:  # 使用 except，如果發生例外狀況，跳出迴圈
                break

        if check == False:
            return False
            # print('身分證字號格式錯誤')
        else:
            return True
            # print('身分證字號正確')
    def validata_ID_Num_2(self, id_number):
        sum = 0
        xxx = [8,7,6,5,4,3,2,1,1]
        id_arr = list(id_number)
        local = str(self.local_table[id_arr[0]])
        sum += int(local[0])
        sum += int(local[1]) * 9
        # print(id_arr.pop(0))
        id_arr.pop(0)
        for i,j in enumerate(id_arr):
            sum += int(xxx[i]) * int(j)

        print(f"id_arr:{id_arr}, local:{local}, sum:{sum}")
        if sum % 10:
            return False
        else:
            return True