import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from api import Api
import datetime

GMT = datetime.timezone(datetime.timedelta(hours=8))    # 設定所在時區 ( 台灣是 GMT+8 )

# 動態時鐘
def clock():
    time = datetime.datetime.now(tz=GMT).strftime('%Y-%m-%d %H:%M:%S')
    _clock.set(f"現在時間：{time}")
    #每秒更新
    root.after(1000, clock)

# 定義顯示用戶輸入的回調函式
def show_input():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("輸入內容", f"你輸入了: {user_input}")
    else:
        messagebox.showwarning("警告", "輸入框為空！")

# 清除Treeview中的數據
def clear_treeview():
    # 刪除 Treeview 中的所有行
    for row in tree.get_children():
        tree.delete(row)

# 取得天氣資訊API資料
def getWatcher():
    _now = datetime.datetime.now(tz=GMT).strftime('%Y-%m-%d %H:%M:%S')
    print(f"getWatcher API Start...{_now}")
    api = Api()
    resp = api.get(api.apis[0])
    isSUccess = resp['status']
    _success = "更新" if isSUccess else "更新失敗"
    _updatedAt.set(f"{_now} {_success}")
    _records = resp['data']['records']['Station'] if isSUccess else []
    if(isSUccess):
        # 先清空
        clear_treeview()
    items = []
    for (i, record)  in enumerate(_records):
        StationName = record['StationName']
        TownName = record['GeoInfo']['TownName']
        Weather = record['WeatherElement']['Weather']
        _Air = record['WeatherElement']['AirTemperature']
        AirTemperature = "異常" if _Air == -99.0 else _Air
        VisibilityDescription = record['WeatherElement']['VisibilityDescription']
        Speed = record['WeatherElement']['GustInfo']['PeakGustSpeed']
        tree.insert('', tk.END, value=(StationName, AirTemperature, Weather, VisibilityDescription, Speed))

    #30 秒更新一次
    root.after(30000, getWatcher)

#取地震資訊每30秒更新一次
def getEart():
    _now = datetime.datetime.now(tz=GMT).strftime('%Y-%m-%d %H:%M:%S')
    print(f"更新地震資訊...{_now}")
    api = Api()
    resp = api.get(api.apis[5])
    isSUccess = resp['status']
    _success = "更新" if isSUccess else "更新失敗"
    _eartTime.set(f"{_now} {_success}")
    _records = resp['data']['records']['Earthquake'] if isSUccess else []

    for row in tree2.get_children():
        tree2.delete(row)
    
    for (i, record)  in enumerate(_records):
        _color = record['ReportColor']
        _desc = record['EarthquakeInfo']['Epicenter']['Location']
        _time = record['EarthquakeInfo']['OriginTime']
        _type = record['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeType']
        _value = float(record['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'])
        _areas = record['Intensity']['ShakingArea']
        _county = _desc[:2]
        
        if i == 0:
            if _value >= 4:
                eart.config(fg="red")
                eartArea.config(fg="red")
            else:
                eart.config(fg="green")
                eartArea.config(fg="green")
            _eart.set(f"{_value}級")
            _eartArea.set(_county)
            _eartTime.set(_time)
        
        tree2.insert('', tk.END, values=(_time, _county, f"{_type}{_value}", _desc))
    #30 秒更新一次
    root.after(30000, getEart)
# 創建主應用窗口
root = tk.Tk()
root.title("跨平台輸入匡範例")
root.geometry("1400x768")  # 設定窗口大小

frame1 = tk.Frame(root, padx=15, pady=15, width=600, height=768)
#frame1.grid(row=1, column=0)
frame1.pack(fill='y', side='left')

frame2 = tk.Frame(root, padx=15, pady=15, width=600, height=768)
#frame2.grid(row=1, column=1)
frame2.pack(fill='y', side='left')

frame3 = tk.Frame(frame2, bd=1, relief="groove", width=600, pady=15)
frame3.grid(row=1, column=0, sticky='w')

# 標籤
label = tk.Label(frame1, text="請輸入API KEY：")
# 輸入框
entry = tk.Entry(frame1, width=30)
# 按鈕
submit_button = tk.Button(root, text="送出", command=show_input)

# 標題
title = tk.Label(frame1, text="各城市的氣象資訊", justify="left", font=font.Font(size=24, weight="bold"))

# 顯示時鐘的字串
_clock = tk.StringVar()
current = tk.Label(frame1, textvariable=_clock)

#最後一次更新時間，變數字串
_updatedAt = tk.StringVar()
updateAt = tk.Label(frame1, textvariable=_updatedAt)

# 創建 Treeview 控件
tree = ttk.Treeview(frame1, columns=("c", "tp", "b", "t", "r"), show='headings')
_columnW = 120
tree.heading("c", text="觀測站")
tree.heading("tp", text="當前溫度")
tree.heading("b", text="天氣型態")
tree.heading("t", text="能見度(公里)")
tree.heading("r", text="風速/秒")
#tree.heading("su", text="日出")
#tree.heading("sd", text="日落")

tree.column("c", anchor="center", width=_columnW)
tree.column("tp", anchor="center", width=_columnW)
tree.column("b", anchor="center", width=_columnW)
tree.column("t", anchor="center", width=_columnW)
tree.column("r", anchor="center", width=_columnW)
#tree.column("su",anchor="center", width=_columnW)
#tree.column("sd",anchor="center", width=_columnW)
tree.config(height=22)

clock()
getWatcher()

#label.grid(row=0, column=0, columnspan=2, sticky='w')
#entry.grid(row=1, column=0, sticky='w' )
#submit_button.grid(row=1, column=1, sticky='w')
# 地震警報


title2 = tk.Label(frame2, text="觀測站地震資訊", justify="left", font=font.Font(size=24, weight="bold"))
_eart = tk.StringVar()
_eartArea = tk.StringVar()
_eartTime = tk.StringVar()

eart = tk.Label(frame3, textvariable=_eart, font=font.Font(size=48, weight="bold"))
eartArea = tk.Label(frame3, textvariable=_eartArea, font=font.Font(size=48, weight="bold"))
eartTime = tk.Label(frame3, textvariable=_eartTime)

tree2 = ttk.Treeview(frame2, columns=("time", "area", "eart", "desc"), show='headings')
_columnW = 100
tree2.heading("time", text="時間")
tree2.heading("area", text="區域")
tree2.heading("eart", text="震度")
tree2.heading("desc", text="說明")

tree2.column("time", anchor="center", width=150)
tree2.column("area", anchor="center", width=100)
tree2.column("eart", anchor="center", width=150)
tree2.column("desc", anchor="center", width=350)

getEart()

tree2.config(height=20)
eartArea.pack(side='left')
eart.pack(side='left')
eartTime.pack(side='right')
tree2.grid(row=2, column=0, sticky="nsew")

title.grid(row=2, column=0, columnspan=2)
current.grid(row=3, column=0, sticky='w')
updateAt.grid(row=3, column=1, sticky='e')
tree.grid(row=4, column=0, columnspan=2, sticky="nsew")




# 啟動應用的主循環
root.mainloop()
