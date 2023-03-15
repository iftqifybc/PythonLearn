import tkinter as tk

root = tk.Tk()
root.title('基本版計算機')
root.geometry('280x200')

label = tk.Label(root,
                borderwidth=1, relief='solid',
                background='#333', width=20,
                font=('Arial',20), justify='left',
                anchor='e')
label.place(x=5, y=10)

# 計算函式
def test(e):
    pass


btn_7 = tk.Button(root, text='7', font=('Arial',20), width=2)
btn_7.place(x=5, y=45)
btn_8 = tk.Button(root, text='8', font=('Arial',20), width=2)
btn_8.place(x=65, y=45)
btn_9 = tk.Button(root, text='9', font=('Arial',20), width=2)
btn_9.place(x=125, y=45)
btn_a = tk.Button(root, text='+', font=('Arial',20), width=2)
btn_a.place(x=185, y=45)

btn_4 = tk.Button(root, text='4', font=('Arial',20), width=2)
btn_4.place(x=5, y=80)
btn_5 = tk.Button(root, text='5', font=('Arial',20), width=2)
btn_5.place(x=65, y=80)
btn_6 = tk.Button(root, text='6', font=('Arial',20), width=2)
btn_6.place(x=125, y=80)
btn_b = tk.Button(root, text='-', font=('Arial',20), width=2)
btn_b.place(x=185, y=80)

btn_3 = tk.Button(root, text='3', font=('Arial',20), width=2)
btn_3.place(x=5, y=115)
btn_2 = tk.Button(root, text='2', font=('Arial',20), width=2)
btn_2.place(x=65, y=115)
btn_1 = tk.Button(root, text='1', font=('Arial',20), width=2)
btn_1.place(x=125, y=115)
btn_c = tk.Button(root, text='x', font=('Arial',20), width=2)
btn_c.place(x=185, y=115)

btn_ac = tk.Button(root, text='AC', font=('Arial',20), width=2)
btn_ac.place(x=5, y=150)
btn_0 = tk.Button(root, text='0', font=('Arial',20), width=2)
btn_0.place(x=65, y=150)
btn_e = tk.Button(root, text='=', font=('Arial',20), width=2)
btn_e.place(x=125, y=150)
btn_d = tk.Button(root, text='/', font=('Arial',20), width=2)
btn_d.place(x=185, y=150)

root.mainloop()