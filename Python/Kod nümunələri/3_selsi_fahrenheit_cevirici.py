"""
Python dili üzrə kod nümunələri - müəllif Nurlan Aliyev,  26/07/2021

Kod №3 - Selsi-Fahrenheit çevirməsi

Kopyalayıb kodu test edə bilərsiniz

Və yaxud bu link vasitəsilə yoxlaya bilərsiniz  https://replit.com/@NurlanAliyev/3SelsiFahrenheitCevirici#main.py
"""

# Aşağıdakı qiyməti istəyə uyğun dəyişə bilərsiniz
# və yaxud altdakı sətri şərh blokunnan çıxarıb istifadəçidən temperatur göstəricisini ala bilər
# selsi = float(input('Temperatur göstəricisini (Selsi şkalası ilə) daxil edin: '))

selsi = 37.5

# Fahrenheitə çevrilmə (fahrenheit = (selsi * 9/5) + 32

fahrenheit = (selsi * 1.8) + 32

#Nəticənin çap olunması
print(f'{selsi} dərəcə Selsi, {fahrenheit} dərəcə Fahrenheitə bərabərdir')
