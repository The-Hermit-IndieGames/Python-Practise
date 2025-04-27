import tkinter as tk  # 導入 tkinter 模組，用於製作圖形化界面
from tkinter import messagebox  # 導入 tkinter 中的 messagebox 用於顯示錯誤訊息框

# 宣告
input_year = 0
year_day_list = []
year_day_list_strings = []

big_mon = [1,3,5,7,8,10,12]
week = "周一    週二    週三    周四    週五    週六    週日  "

show_mon = 1

# 運算部分 =============================================================================================================== 運算部分 #

# 函式-判斷是否為閏年
def is_leap_year(year):
    # 如果年份能被 4 整除，則可能是閏年。
    if (year % 4 == 0):
        # 但是，如果該年份能被 100 整除，則不是閏年。
        if (year % 100 == 0):
            # 除非該年份能被 400 整除，那麼它仍然是閏年。
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# 閏年-字串版
def is_leap_year_string(year):
    if is_leap_year(year):
        return "是"
    else:
        return "不是"


# 周次修正值
def week_add(year):
    # 基於 0001年 1/1 為周一    ex. 0001年 回傳0 --> 1/1 為周一
    return ((year-1) + (year-1)//4 - (year-1)//100 + (year-1)//400) % 7


# 建立年曆 (列表: [ [1,2,3,...] , [*,*,1,2,3,...] , ......] )
def creat_year_day_list(year):
    global big_mon, year_day_list
    year_day_list.clear

    max_day = 0
    now_week = week_add(year)

    mon = 1
    # 第一層-月
    while mon <= 12:
        mon_days = []

        # 天數判斷
        if mon == 2 and is_leap_year(year):
            max_day = 29
        elif mon == 2 and is_leap_year(year) == False:
            max_day = 28
        elif mon in big_mon:
            max_day = 31
        else:
            max_day = 30
        
        # 每月初按造星期輸出空白
        mon_star = now_week
        while mon_star >= 1:
            mon_days.append(" ")
            mon_star -= 1
        
        day = 1
        # 第二層-日
        while day <= max_day:
            
            mon_days.append(day)
            now_week += 1
            if now_week >= 7:
                now_week = 0

            day += 1
        

        year_day_list.append(mon_days)
        mon += 1
        
    else:
        print("\ncreat_year_day_list END")


# 按周印出年曆
def print_year_days():
    global year_day_list, year_day_list_strings

    for mon_list in year_day_list:
        month_str = ""

        x = 0
        for day in mon_list:
            month_str += str(day).ljust(8)  # 每個元素佔據ljust()個字元
            x += 1
            if x % 7 == 0:  # 每7個元素換行
                month_str += "\n"
                x = 0

        year_day_list_strings.append(month_str)
    else:
        print("\nprint_year_days END")


creat_year_day_list(2024)
print_year_days()
print(year_day_list_strings[9])


# 視窗部分 =============================================================================================================== 視窗部分 #

# 檢查輸入是否為整數
def validate_int(char):
    # 函數用來檢查每次輸入的字符是否為數字
    # 如果是數字或是空字符(允許使用者清空輸入框，避免在刪除過程中報錯)，則返回 True，否則返回 False
    return char.isdigit() or char == ""


# 提交按鈕的事件處理函數
def submit():
    global input_year, show_mon
    user_input = entry.get()  # 從輸入框中取得使用者的輸入
    if user_input.isdigit():  # 檢查輸入是否為整數
        input_year = int(user_input)
        output_var.set(f"查詢{input_year}年")  # 更新輸出欄，顯示使用者的輸入
        show_mon = 1
        window_updata()
    else:
        # 如果輸入不是有效整數，顯示錯誤訊息
        messagebox.showerror("錯誤", "請輸入有效的年分")


# 清除按鈕的事件處理函數
def clear():
    entry.delete(0, tk.END)  # 清空輸入欄的內容
    output_var.set("")  # 清空輸出欄的內容


# 換頁按鈕 (下一頁) 的事件處理函數
def next_page():
    global show_mon
    show_mon += 1
    if show_mon >= 13:
        show_mon = 12
    output_var.set(f"目前顯示{show_mon:3d}月")  # 更新輸出欄，顯示按鈕操作的結果
    window_updata()


# 換頁按鈕 (上一頁) 的事件處理函數
def previous_page():
    global show_mon
    show_mon -= 1
    if show_mon <= 0:
        show_mon = 1
    output_var.set(f"目前顯示{show_mon:3d}月")  # 更新輸出欄，顯示按鈕操作的結果
    window_updata()


# 主視窗刷新
def window_updata():
    global input_year, show_mon
    is_leap_year_var.set(f"該年分{is_leap_year_string(input_year)}閏年")
    output_string = (f"{input_year:4d}年{show_mon:3d}月\n\n{week}\n\n{year_day_list_strings[show_mon-1]}")
    update_main_output(output_string)


# 創建主視窗 ---------------------------------------------------------------------------------------------------
window = tk.Tk()  # 初始化 Tkinter 視窗
window.title("萬年曆")  # 設置視窗標題
window.geometry("600x400")  # 設置視窗大小 (寬 300 像素, 高 300 像素)

# 輸入欄-年
entry_label = tk.Label(window, text="請輸入要查詢的西元年份：")  # 創建標籤，提示使用者輸入整數
entry_label.pack(pady=5)  # 將標籤添加到視窗中，並設置與其他元件的間距

# 輸入欄 vcmd 註冊為檢查函數，驗證每次鍵入的字元是否有效
vcmd = (window.register(validate_int), "%S")  # 綁定 validate_int 函數來檢查輸入
entry = tk.Entry(window, validate="key", validatecommand=vcmd)  # 創建輸入框，設定檢查規則
entry.pack(pady=5)  # 將輸入框添加到視窗中，並設置與其他元件的間距

# 提交按鈕
submit_btn = tk.Button(window, text="提交", command=submit)  # 創建按鈕，綁定 submit 函數作為按鈕的回調
submit_btn.pack(pady=5)  # 將按鈕添加到視窗中，並設置與其他元件的間距


# 輸出欄-閏年判斷 (Entry限制為單行)
is_leap_year_var = tk.StringVar()  # 創建一個變量來儲存輸出文字
is_leap_year_entry = tk.Entry(window, textvariable=is_leap_year_var, state="readonly")  # 創建只讀的輸出框，綁定 is_leap_year_var 顯示輸出
is_leap_year_entry.pack(pady=5)  # 將輸出框添加到視窗中，並設置與其他元件的間距
is_leap_year_var.set(f"該年分是否為閏年")


# 輸出欄-單月曆 (Text 元件顯示多行文字)
main_output_text = tk.Text(window, height=5, width=40, state="normal")
main_output_text.pack(side="top", fill=tk.BOTH, expand=True, padx=30, pady=20)
# 插入多行文字到 Text 元件中
main_output_text.insert(tk.END, "此處用於輸出月曆")
# 設置為只讀模式
main_output_text.config(state=tk.DISABLED)

# 更新 Text 內容的函式
def update_main_output(new_text):
    main_output_text.config(state=tk.NORMAL)  # 解除只讀模式
    main_output_text.delete("1.0", tk.END)    # 清除原有內容
    main_output_text.insert(tk.END, new_text) # 插入新內容
    main_output_text.config(state=tk.DISABLED) # 設置回只讀模式


# 換頁按鈕 (上一頁)
previous_btn = tk.Button(window, text="上一頁", command=previous_page)  # 創建上一頁按鈕，綁定 previous_page 函數
previous_btn.pack(side=tk.LEFT, padx=10, pady=5)  # 將上一頁按鈕添加到視窗左側，並設置間距

# 換頁按鈕 (下一頁)
next_btn = tk.Button(window, text="下一頁", command=next_page)  # 創建下一頁按鈕，綁定 next_page 函數
next_btn.pack(side=tk.RIGHT, padx=10, pady=5)  # 將下一頁按鈕添加到視窗右側，並設置間距


# 創建輸出欄，並將其設置為只讀模式
output_var = tk.StringVar()  # 創建一個變量來儲存輸出文字
output_entry = tk.Entry(window, textvariable=output_var, state="readonly")  # 創建只讀的輸出框，綁定 output_var 顯示輸出
output_entry.pack(pady=20)  # 將輸出框添加到視窗中，並設置與其他元件的間距

# 清除按鈕
clear_btn = tk.Button(window, text="清除/重新輸入", command=clear)  # 創建清除按鈕，綁定 clear 函數作為按鈕的回調
clear_btn.pack(pady=5)  # 將清除按鈕添加到視窗中，並設置與其他元件的間距




# 啟動視窗循環
window.mainloop()  # 啟動 Tkinter 的事件循環，使視窗保持開啟