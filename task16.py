BAZAVIY_NARX = 100_000

age = int(input("Yoshingizni kiriting: "))

if age <= 8:
    chegirma = 0.50       
elif 8 <= age <= 18:
    chegirma = 0.20     
elif age >= 18:
    chegirma = 0.00       
        

chegirma_som = int(BAZAVIY_NARX * chegirma)
yakuniy_narx  = BAZAVIY_NARX - chegirma_som


print(f"Yakuniy narx: {yakuniy_narx:,} so'm "
      f"({int(chegirma*100)}% chegirma qo'llanildi)")


