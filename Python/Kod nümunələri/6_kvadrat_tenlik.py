"""
Python dili üzrə kod nümunələri - müəllif Nurlan Aliyev,  26/07/2021

Kod №6 - hədləri real ədədlər olan və a ≠ 0 olan ax2 + bx + c = 0 kvadrat tənliyinin həlli

Kopyalayıb kodu test edə bilərsiniz

Və yaxud bu link vasitəsilə yoxlaya bilərsiniz  https://replit.com/@NurlanAliyev/6KvadratTenlik#main.py
"""

import math, cmath

a = 1
b = 6
c = 8

# Diskriminantın hesablanması
d = (b**2) - (4*a*c)

if d >= 0: #əgər diskriminant 0dan böyük bərabərdirsə
    
    kok1 = (-b-math.sqrt(d))/(2*a)
    kok2 = (-b+math.sqrt(d))/(2*a)
else: #əgər d<0 olarsa kompleks kök alınır
    kok1 = (-b-cmath.sqrt(d))/(2*a)
    kok2 = (-b-cmath.sqrt(d))/(2*a)
    
    
#Nəticələrin çap olunması
print(f'Tənliyin kökləri: x1 = {kok1}, x2 = {kok2}')
