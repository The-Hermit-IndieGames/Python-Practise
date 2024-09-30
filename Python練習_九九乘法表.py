# x 為被乘數
for x in range(1,10):
    # y 為乘數
    for y in range(1,10):
        # 輸出結果並對齊
        print(f"{x:5d} x {y:5d} = {x*y:5d}")
    # 分行
    print("\n")

# 卡結束用
input("輸入任意值結束")