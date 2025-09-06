BAZAVIY_NARX = 100_000

age = int(input("Yoshingizni kiriting: "))

if age < 7:
    chegirma = 0.50
elif 7 <= age <= 17:
    chegirma = 0.20
elif age > 60:
    chegirma = 0.30
else:
    chegirma = 0.00

chegirma_som = int(BAZAVIY_NARX * chegirma)
yakuniy_narx = BAZAVIY_NARX - chegirma_som

print(f"Yakuniy narx: {yakuniy_narx:,} so'm")
print(f"Chegirma: {int(chegirma*100)}%")


