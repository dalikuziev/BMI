print("BMI haqida ma'lumot olish uchun marhamat!")
weight = float(input("Vazningizni kiriting: "))
height = float(input("Bo'yingizni kiriting: "))

bmi = round(weight / (height**2), 1)

if bmi < 18.5:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz yengil vaznli ekansiz!")
elif bmi < 25:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz normal vaznli ekansiz!")
elif bmi < 30:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, sizda biroz ortiqcha vazn bor!")
elif bmi < 35:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, sizda ortiqcha vazn bor!")
else:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, sizda haddan tashqari ortiqcha vazn bor!")
