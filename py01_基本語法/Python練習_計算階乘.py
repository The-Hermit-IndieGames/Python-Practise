#函式-型別限制-整數
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("\a輸入錯誤，請輸入數字(整數)。")


#資料輸入
number = get_int_input("\n請輸整數: ")

output = 1

while(number > 0):
    output *= number
    number -= 1

print(output)