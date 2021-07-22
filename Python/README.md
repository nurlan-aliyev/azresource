
## Python nədir?
Python populyar proqramlaşdırma dilidir. Bu dilin yaradıcısı <a href="https://en.wikipedia.org/wiki/Guido_van_Rossum" target="_blank">Guido van Rossum</a>dur və o, bu dili 1991-ci ildə yaradıb və paylaşıb.

Pythonun istifadə yerləri:
-   veb proqramlaşdırma (server tərəfi),
-   proqram təminatı yaradılması,
-   riyazi hesablama və işlərdə,
-   sistem skriptləşdirmədə.

### Python nəyə qadirdir?

-   Serverlərdə veb tətbiqlərin yaradılmasına
-   Verilənlər bazasına qoşulmağa və baza daxilindəki məlumatları yeniləməyə
-   Big Data ilə işləməyə və müxtəlif mürəkkəb riyazi hesablamalar aparmağa.

### Niyə Python?

-   Python müxtəlif əməliyyat sistemlərində çalışır (məs. Windows, Mac, Linux, Raspberry Pi və s.).
-   Python İngilis dilinə yaxın dil olduğu üçün daha anlaşıqlıdır.
-   Python digər dillərlə müqayisədə daha az kod sətrindən istifadə etməyə imkan yaradır.
-   Python interperetasiyadan istifadə etdiyinə görə prototipləşdirmə daha asan və daha tez başa gəlir.
-   Python prosedural yönümlü, obyekt yönümlü və funksional yönümlü istifadə oluna bilər.

### Başqa proqramlaşdırma dilləri ilə müqayisədə Python

-   Python asan oxunabilən dil sayılır və İngilis dilinə daha yaxındır.
-   Python nöqtəli vergül(;) yerinə sətr və boşluqlardan istifadə edir.
-   Python funksiyaların, şərt bloklarının və siniflərin təyinində abzaslardan və boşluqlardan istifadə edir.

### Nümunə
```python
print("Salam, Dünya!")
```
***

## Python-un endirilməsi
Əgər sizin kompyuterinizdə Python endirilibsə bunu aşağıadkı sətrlə yoxlaya bilərsiniz: 
```cmd
C:\Users\_adınız_>python --version
```
<em>Linux</em> və ya <em>Mac</em> əməliyyat sistemlərində bunu yoxlamaq üçün terminalda aşağıdakı sətri yazmaq lazımdır: 
```bash
python --version
```
Əgər kompyuterinizdə Python endirilməmişdirsə rəsmi veb səhifəsindən rahatlıqla və pulsuz formada endirə bilərsiniz.   [<b><em>Endirmə linki</em></b>](https://www.python.org/)

----------

## Python haqqında qısa məlumatlar

Python interperetasiya olunan dildir, yəni skriptlər (**.py**) uzantısı ilə saxlanılır və Pytho interpertorunda icra edilir. 

Aşağıda əmrlər sətrində (**CMD**) Python faylının icra olunması yolu göstərilib: 
```cmd
C:\Users\_adınız_>python salamdunya.py
```
Buradakı `salamdunya.py` Python faylının adıdır. 

İndi isə `salamdunya.py` faylının koduna baxaq:

```python
print("Salam, Dünya!")
```
[Kodu özünüz bu linkdən yoxlaya bilərsiniz](https://replit.com/@NurlanAliyev/salamdunya#main.py)
***
Yazdığınız faylı yaddaşda saxlayıb CMD vasitəsilə onu icra etmək lazımdır. 
```cmd
C:\Users\_adınız_>python salamdunya.py
```
CMD ekranında qarşınıza aşağıdakı yazı görünəcək:
```
Salam, Dünya!
```
Təbriklər, artıq ilk Python proqramını yazıb icra etdiniz!

##  Python Əmrlər sətri

Bəzən qısa kodları yoxlamaq lazım gəlir, bunun üçün Python faylı yaratmaq mütləq deyil, çünki Python özü əmrlər sətri rolu oynayır və yazılan sətrləri ardıcıl icra edir. 

Pythonu bu formada istifadə etmək üçün  Windows, Mac və ya Linux  əmrlər sətrində aşağıdakı sətri yazmaq lazımdır: 

```bash
C:\Users\_adınız_>python
```
Əgər bu işə yaramırsa sadəcə "**py**" yazıb yoxlamaq lazımdır. 
```bash
C:\Users\_adınız_>py
```
Artıq siz istədiyiniz Python kodunu yazıb icra edə bilərsiniz.
```
C:\Users\N>python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Salam, Dunya!")
```
"**Enter**" düyməsini basdıqdan sonra ekranda aşağıdakı yazılar görünəcək: 


```cmd
C:\Users\N>python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Salam, Dunya!")
Salam, Dunya!
>>>
```

Python interfeysi ilə işiniz bitəndən sonra sadəcə `exit()` yazıb "**Enter**" düyməsinə basmağınız kifayət edir. 

***

# Python sintaksis icrası
Əvvəlki mövzularda toxunulduğu kimi Python birdəfəlik əmrlər sətrindən icra oluna bilir. 

```cmd 
>>> print("Salam, Dunya!")
```

## Python abzasları
Abzas dedikdə koddan əvvəl yerləşən boşluqlar nəzərdə tutulur. 

Başqa proqramlaşdırma dillərində boşluqların elə də böyük mənası olmadığı halda Python dilində onlar böyük önəm daşıyır. 

Python kod blokunu tanımaq üçün abzaslanma tələb edir: 

Nümunə:
```python
if 5 > 2:
  print("Beş ikidən böyükdür!")
```
Fikir verdinizsə, `if` şərt blokunu tanımlamaq üçün sonrakı sətrdə `print` əmri qarşısında abzaslanma mövcuddur (Lori dildə desək ən azı 1 dəfə "*Space*" düyməsinə basmaq lazımdır). 

Əgər bu qaydaya riayət olunmazsa interperetor yanlış mesajı qaytaracaq:

```python
if 5 > 2:
print("Beş ikidən böyükdür!")
```

## Python Dəyişənləri
Başqa dillərlə müqayisədə dəyişənlər Pythonda verilənlər tipləri(data types) bildirilmədən qeyd olunur. Yəni müəyyən adlı dəyişəni təyin edərkən verilənlər tipini(Int, String, Double, Float, Char və s.) qeyd etmək lazım deyil. 


Nümunə:
```python
x = 5
y = "Salam, Dünya!"
```

Python dəyişənləri təyin etmək üçün xüsusi əmr tələb etmir, sadəcə "**=**" işarəsi kifayətdir. 

Dəyişənlər haqqında daha geniş danışacayıq.  

## Şərhlər

- Python tək sətrli şərhləri dəstəkləyir
- Şərhlər "**#**" simvolu ilə başlayır və həmin sətr tamamilə şərh kimi qəbul olunur

Nümunə:

```python
#Bu tək sətrli şərhdir.
print("Salam, Dünya!")
```

***

- Şərhlər Python kodunu istifadəçiyə izah etmək və yaxud oxunmasını rahatlaşdırmaq məqsədilə istifadə edilir. 

-Şərhlərdən ***debugging*** zamanı icrası istənməyən kod bloklarında istifadə olunur.

## Şərhlərin yaradılma qaydası
Şərhlər **#** simvolu ilə başlanır.

Nümunə:

```python
#Bu tək-sətrli şərhdir
print("Salam, Dünya!")
```

Şərhlər sətrin sonunda da qeyd oluna bilər: 

Nümunə:

```python
print("Salam, Dünya!") #Bu tək-sətrli şərhdir
```

Şərhlər təkcə kodu izah etmək üçün deyil hər hansısa kod blokunu gizləmək üçün də istifadə oluna bilər:

Nümunə:

```python
#print("Bu sətr icra olunmuyacaq")
print("Yalnız bu sətr icra olunacaq!")
```

## Çox-sətrli şərhlər
Python dili başqa dillərlə müqayisədə çox-sətrli şərhlər üçün xüsusi simvol istifadəçiyə təqdim etmir.


Lakin çox-sətrli şərhlər üçün hər sətrə **#** işarəsi qoymaq kifayətdir. 

Nümunə:

```python
#Bu şərh
#çox-sətrli şərhlərə
#nümunədir
print("Salam, dəyərli Proqramçı!")
```

Və yaxud, daha asan olmağı üçün çox-sətrli ***string***lərdən (3 dırnaq işarəsi) istidadə etmək mümkündür. 

Nümunə:

```python

"""
Bu çox-sətrli 
şərhlərə aid olan
nümunədir
"""
print("Hello, World!")
```
***