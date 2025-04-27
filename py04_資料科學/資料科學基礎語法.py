import tkinter as tk
from tkinter import messagebox

# 創建主視窗
window = tk.Tk()
window.title("簡單的 GUI 應用")
window.geometry("800x450")

# 檢查輸入是否為整數
def validate_int(char):
    return char.isdigit() or char == ""

# 事件處理函數
def submit():
    user_input = entry.get()
    if user_input.isdigit():
        output_var.set(f"您輸入的數字是：{user_input}")
    else:
        messagebox.showerror("錯誤", "請輸入有效的整數")

def clear():
    entry.delete(0, tk.END)
    output_var.set("")

def next_page():
    output_var.set("你按了 下一頁 按鈕")

def previous_page():
    output_var.set("你按了 上一頁 按鈕")

# 輸入欄位
entry_label = tk.Label(window, text="請輸入整數：")
entry_label.pack(pady=5)

vcmd = (window.register(validate_int), "%S")
entry = tk.Entry(window, validate="key", validatecommand=vcmd)
entry.pack(pady=5)

# 提交按鈕
submit_btn = tk.Button(window, text="提交", command=submit)
submit_btn.pack(pady=5)

# 輸出欄位 (只讀)
output_var = tk.StringVar()
output_label = tk.Label(window, text="輸出欄位：")
output_label.pack(pady=5)

output_entry = tk.Entry(window, textvariable=output_var, state="readonly")
output_entry.pack(pady=5)

# 清除按鈕
clear_btn = tk.Button(window, text="清除/重新輸入", command=clear)
clear_btn.pack(pady=5)

# 換頁按鈕
previous_btn = tk.Button(window, text="上一頁", command=previous_page)
previous_btn.pack(side=tk.LEFT, padx=20, pady=10)

next_btn = tk.Button(window, text="下一頁", command=next_page)
next_btn.pack(side=tk.RIGHT, padx=20, pady=10)

# 啟動主視窗循環
window.mainloop()
