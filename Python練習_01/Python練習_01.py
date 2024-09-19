﻿#函式-型別限制-整數
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("\a輸入錯誤，請輸入數字(整數)。")


#函式-判斷是否為閏年
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
    


#開始   
print('歡迎使用閏年判斷\n')


#資料輸入
year = get_int_input("請輸西元年份(整數): ")


#判斷
if is_leap_year(year):
        print(f"{year} 年是閏年。")
else:
        print(f"{year} 年不是閏年。")