#函式-型別限制-整數
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("\a輸入錯誤，請輸入數字(整數)。")


#開始   
print('歡迎使用銀行管理系統\n')
money = 0
continue_bool = True
while (continue_bool):

    #功能選擇
    value = get_int_input("\n請選擇功能(1.存款、2.提款、3.查詢餘額、4.退出系統): ")
    match value:
        case 1:
            print("1.存款")
            money_f = get_int_input(f"#請輸入存款金額: ")
            money += money_f
            print(f"#已存入:{money_f} ；當前餘額: {money}")
        case 2:
            print("2.提款")
            money_f = get_int_input(f"#請輸入提款金額: ")
            if (money - money_f) >= 0:
                money -= money_f
                print(f"#已提款:{money_f} ；當前餘額: {money}")
            else:
                print(f"#餘額不足! 當前餘額: {money}")
        case 3:
            print("3.查詢餘額")
            print(f"#當前餘額: {money}")
        case 4:
            print("4.退出系統")
            continue_bool = False
        case _:
            print(f"不存在的功能代碼: {value}")

print('\n程式結束')