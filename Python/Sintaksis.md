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