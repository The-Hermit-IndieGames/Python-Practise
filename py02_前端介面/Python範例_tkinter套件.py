# by chatGPT

import tkinter as tk  # 導入 tkinter 模組，用於製作圖形化界面
from tkinter import messagebox  # 導入 tkinter 中的 messagebox 用於顯示錯誤訊息框

# 創建主視窗
window = tk.Tk()  # 初始化 Tkinter 視窗
window.title("簡單的 GUI 應用")  # 設置視窗標題
window.geometry("300x300")  # 設置視窗大小 (寬 300 像素, 高 200 像素)

# 檢查輸入是否為整數
def validate_int(char):
    # 函數用來檢查每次輸入的字符是否為數字
    # 如果是數字或是空字符(允許使用者清空輸入框，避免在刪除過程中報錯)，則返回 True，否則返回 False
    return char.isdigit() or char == ""

# 提交按鈕的事件處理函數
def submit():
    user_input = entry.get()  # 從輸入框中取得使用者的輸入
    if user_input.isdigit():  # 檢查輸入是否為整數
        output_var.set(f"您輸入的數字是：{user_input}")  # 更新輸出欄，顯示使用者的輸入
    else:
        # 如果輸入不是有效整數，顯示錯誤訊息
        messagebox.showerror("錯誤", "請輸入有效的整數")

# 清除按鈕的事件處理函數
def clear():
    entry.delete(0, tk.END)  # 清空輸入欄的內容
    output_var.set("")  # 清空輸出欄的內容

# 換頁按鈕 (下一頁) 的事件處理函數
def next_page():
    output_var.set("你按了 下一頁 按鈕")  # 更新輸出欄，顯示按鈕操作的結果

# 換頁按鈕 (上一頁) 的事件處理函數
def previous_page():
    output_var.set("你按了 上一頁 按鈕")  # 更新輸出欄，顯示按鈕操作的結果

# 輸入欄位
entry_label = tk.Label(window, text="請輸入整數：")  # 創建標籤，提示使用者輸入整數
entry_label.pack(pady=5)  # 將標籤添加到視窗中，並設置與其他元件的間距

# vcmd 註冊為檢查函數，驗證每次鍵入的字元是否有效
vcmd = (window.register(validate_int), "%S")  # 綁定 validate_int 函數來檢查輸入
entry = tk.Entry(window, validate="key", validatecommand=vcmd)  # 創建輸入框，設定檢查規則
entry.pack(pady=5)  # 將輸入框添加到視窗中，並設置與其他元件的間距

# 提交按鈕
submit_btn = tk.Button(window, text="提交", command=submit)  # 創建按鈕，綁定 submit 函數作為按鈕的回調
submit_btn.pack(pady=5)  # 將按鈕添加到視窗中，並設置與其他元件的間距

# 輸出欄位
output_var = tk.StringVar()  # 創建一個變量來儲存輸出文字
output_label = tk.Label(window, text="輸出欄位：")  # 創建標籤來標識輸出欄
output_label.pack(pady=5)  # 將標籤添加到視窗中，並設置與其他元件的間距

# 創建輸出欄，並將其設置為只讀模式
output_entry = tk.Entry(window, textvariable=output_var, state="readonly")  # 創建只讀的輸出框，綁定 output_var 顯示輸出
output_entry.pack(pady=5)  # 將輸出框添加到視窗中，並設置與其他元件的間距

# 清除按鈕
clear_btn = tk.Button(window, text="清除/重新輸入", command=clear)  # 創建清除按鈕，綁定 clear 函數作為按鈕的回調
clear_btn.pack(pady=5)  # 將清除按鈕添加到視窗中，並設置與其他元件的間距

# 換頁按鈕 (上一頁)
previous_btn = tk.Button(window, text="上一頁", command=previous_page)  # 創建上一頁按鈕，綁定 previous_page 函數
previous_btn.pack(side=tk.LEFT, padx=20, pady=10)  # 將上一頁按鈕添加到視窗左側，並設置間距

# 換頁按鈕 (下一頁)
next_btn = tk.Button(window, text="下一頁", command=next_page)  # 創建下一頁按鈕，綁定 next_page 函數
next_btn.pack(side=tk.RIGHT, padx=20, pady=10)  # 將下一頁按鈕添加到視窗右側，並設置間距

# 啟動主視窗循環
window.mainloop()  # 啟動 Tkinter 的事件循環，使視窗保持開啟
