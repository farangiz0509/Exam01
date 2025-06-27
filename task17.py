score = int (input("enter the score"))

if score >= 90:
    print("A")
elif score >= 80 or score <= 70:
    print("B")
elif score >= 60  or score <= 50:
    print("C")
elif score >= 50 or score <= 40:
    print("D")
else:
    print("KIRISH BALI 40 DAN YUQORI BOLISHI KERAK")