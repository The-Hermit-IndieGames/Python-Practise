# 宣告
input_year = 0
year_day_list = []
year_day_list_strings = []

big_mon = [1,3,5,7,8,10,12]
week = "周一    週二    週三    周四    週五    週六    週日  "
line = "===================================================="

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


# 函式-型別限制-整數
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("\a輸入錯誤，請輸入數字(整數)。")


# 主程式
print('\n歡迎使用萬年曆\n')

# 資料輸入
input_year = get_int_input("\n請輸西元年份(整數): ")

# 判斷
if is_leap_year(input_year):
    print(f"{input_year} 年是閏年。")
else:
    print(f"{input_year} 年不是閏年。")


creat_year_day_list(input_year)
print_year_days()

while show_mon <= 12:
    output_string = (f"\n{line}\n{input_year:4d}年{show_mon:3d}月\n\n{week}\n\n{year_day_list_strings[show_mon-1]}")
    print(output_string)
    show_mon += 1
else:
    print("\n E N D ")

