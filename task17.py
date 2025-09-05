ball = int(input("Balingizni kiriting: "))

if 90 <= ball <= 100:
    print("A (A'lo)")  

elif 80 <= ball < 90:
    print("B (Yaxshi)")  

elif 70 <= ball < 80:
    print("C (Qoniqarli)")  

elif 60 <= ball < 70:
    print("D (Qoniqarsiz)")  

elif 0 <= ball < 60:
    print("F (yomon)")

else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")

