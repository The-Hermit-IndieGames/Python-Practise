# 宣告: 周幾?(n為一年的第一天)、月、日
now_week = 0
week = ["n","n+1","n+2","n+3","n+4","n+5","n+6"]
mon = 1
big_mon = [1,3,5,7,8,10,12]
day = 1
max_day = 30


# 函式-型別限制-整數
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("\a輸入錯誤，請輸入數字(整數)。")


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
    

# 函式-輸出日期並每周對齊
def print_day():
    global day, now_week
    print(f"{day:>6}",end="")
    if now_week == 6:
        print()
        now_week = 0
    else:
        now_week += 1


# 開始 ==========================================================================================================
print('\n歡迎使用萬年曆\n')

# 資料輸入
year = get_int_input("\n請輸西元年份(整數): ")

# 判斷
if is_leap_year(year):
    print(f"{year} 年是閏年。\n")
else:
    print(f"{year} 年不是閏年。\n")


print(f"\n  {year:6d} 年-年曆 (請依據 1/1 星期幾自行對齊)\n")
# 第一層-月
while mon <= 12:
    print(f"{" ":20s}{mon:<3d}月")

    # 對齊: 周幾
    print(end=" ")
    for i in range(7):
        print(f"{week[i]:>5s}",end=" ")
    else:
        print("")
    
    # 天數判斷
    if mon == 2 and is_leap_year(year):
        max_day = 29
    elif mon == 2 and is_leap_year(year) == False:
        max_day = 28
    elif mon in big_mon:
        max_day = 31
    else:
        max_day = 30
    
    # 周次對齊
    print(" "*(6*now_week),end="")

    # 第二層-日
    while day <= max_day:
        print_day()
        day += 1
    else:
        day = 1
        print("\n")

    # 結尾/下個月
    mon +=1
# 卡結束用
input("輸入任意值結束")