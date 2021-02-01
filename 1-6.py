s = int (input("請輸入成績"))
if s >100:
    print("輸入錯誤")
elif s <0:
    print("輸入錯誤")
elif s >=90:
    print("A級")  
elif s >=80:
    print("B級")  
elif s >=70:
    print("C級")
elif s >=60:
    print("D級")  
else:
    print("E級")  
