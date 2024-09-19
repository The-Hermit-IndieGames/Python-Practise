

#函式-型別限制-浮點數
def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            # 如果成功，返回輸入值
            return user_input  
        except ValueError:
            print("輸入錯誤，請輸入數字(浮點數)。")


#開始
print('歡迎使用BMI計算機\n')

#資料輸入

height = get_float_input("請輸您的身高(公尺): ")
weight = get_float_input("請輸您的體重(公斤): ")



#計算部分
bmi = weight / ( height ** 2 )
print(f"\n您的BMI為: {bmi}")

if bmi < 18.5:
        print("您的體重過輕\n")
elif 18.5 <= bmi < 24.0:
        print("您的體重正常\n")
elif 24 <= bmi < 27.0:
        print("您的體重過重\n")
else:
        print("您的體重肥胖\n")

#結束
i = input("輸入任意值結束 ")

