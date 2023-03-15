import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import myLib.Healthy as hy

win = tk.Tk()
myHy = hy.Healthy()
def healthy(i):
    pass

win.title('健康管理系統')
window_width = win.winfo_screenwidth()    # 取得螢幕寬度
window_height = win.winfo_screenheight()  # 取得螢幕高度

width = 400
height = 240
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
win.geometry(f'{width}x{height}+{left}+{top}')
# win.configure(background='#fff')   # 設定背景色黑色


labSex = tk.Label(win, text="姓            別")
labSex.grid(row=0, column=0)
cmbSex = ttk.Combobox(win, values='aaa', width=15)
cmbSex.grid(row=0, column=1)

labAge = tk.Label(win, text="年            齡")
labAge.grid(row=1, column=0)
txtAge = tk.Entry(win)
txtAge.grid(row=1, column=1)

labHigh = tk.Label(win, text="身            高")
labHigh.grid(row=2, column=0)
txtHigh = tk.Entry(win)
txtHigh.grid(row=2, column=1)

labWeight = tk.Label(win, text="體            重")
labWeight.grid(row=3, column=0)
txtWeight = tk.Entry(win)
txtWeight.grid(row=3, column=1)


labSport = tk.Label(win, text="日常活動量")
labSport.grid(row=4, column=0)
cmbSport = ttk.Combobox(win, values='ccc', width=25)
cmbSport.grid(row=4, column=1)

labMsg = tk.Label(win, text="", width=20)
labMsg.grid(row=5, column=1)

btnScale = tk.Button(win, text="BMI")
btnScale.grid(row=6, column=0)

btnScale = tk.Button(win, text="BMR")
btnScale.grid(row=6, column=1)

btnScale = tk.Button(win, text="TDEE")
btnScale.grid(row=6, column=2)

win.mainloop()