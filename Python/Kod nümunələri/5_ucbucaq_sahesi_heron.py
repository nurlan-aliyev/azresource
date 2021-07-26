"""
Python dili üzrə kod nümunələri - müəllif Nurlan Aliyev,  26/07/2021

Kod №5 - Üçbucağın sahəsinin Heron düsturu ilə tapılması

Kopyalayıb kodu test edə bilərsiniz

Və yaxud bu link vasitəsilə yoxlaya bilərsiniz  https://replit.com/@NurlanAliyev/5UcbucaqSahesiHeron#main.py
"""


# Üçbucağın tərəfləri

a = 5
b = 6
c = 7

# Tərəfləri istifadəçidən oxumaq üçün aşağıdakı 3 sətri şərh blokundan çıxarın
# a = float(input('Birinci tərəfi daxil edin: '))
# b = float(input('İkinci tərəfi daxil edin: '))
# c = float(input('Üçüncü tərəfi daxil edin: '))

# Yarımperimetrin hesablanması
s = (a + b + c) / 2

# Sahənin hesablanması
sahe = (s*(s-a)*(s-b)*(s-c)) ** 0.5 # ** işarəsi qüvvət simvoludur, 0.5 kokaltının qüvvətini göstərir
print(f'Üçbucağın sahəsi {sahe}-a/ə(ya/yə) bərabərdir')
