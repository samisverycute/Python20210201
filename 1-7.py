s = int (input("請輸入數學成績"))
a = int (input("請輸入英文成績"))
if s>=90 and a>=90:
    print("有獎品")
elif s<60 and a<60:
    print("要處罰")
elif s<60 or a<60:
    print("再加油")
