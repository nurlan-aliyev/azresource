
## Dəyişənlər

Dəyişənlər daxilində dəyər saxlayan yaddaş vahidləridir. 

## Dəyişənlərin yaradılması

Python dili dəyişən yaratmaq üçün xüsusi əmrdən istifadə etmir. Dəyişənə qiymət təyin edərkən artıq o yaradılır və yaddaşda rezerv edilir. 

Nümunə:

```python
x =  5  
y =  "Lerik"  
print(x) # 5 çap edilir
print(y) # Lerik çap edilir
```
Dəyişənlərin data tipləri (***data types***) əvvəlcədən təyin olunmur, və hətta onlar sonradan başqa tiplərə çevrilə bilərlər. 

Nümunə:

```python
x =  4 # x int tiplidir  
x =  "Həşim"  # x artıq String tipinə çevrildi  
print(x) # Həşim çap olunur 
```

## Casting (qəlibləmə)

Əgər xüsusi bir tipə uyğun dəyişən yaratmaq istəyirsinizsə qəlibləmə üsulu (əridilmiş metalları istəlinən formaya salmaq üçün qəlib istifadə olunur, bu söz o məntiqdən götürülüb) əlverişlidir. 

Nümunə:

```python
x =  str(3) # x String tipində '3' qiymətinə malik olur  
y =  int(3) # y İnt tipində  3 qiymətinə malik olur  
z =  float(3) # z Float tipində 3.0 qiymətinə malik olur
```

## Dəyişənin tipinin öyrənilməsi

İstənilən dəyişənin tipini  `type()`  funksiyası ilə öyrənmək mümkündür. 

Nümunə:
```python
x =  5  
y =  "Elnur"  
print(type(x)) # int sinifinin mesajı çap olunacaq  
print(type(y)) # str sinifinin mesajı çap olunacaq
```

## Tək və yaxud qoşa dırnaqlar

String tipli dəyişənlər həm tək (**'**) və yaxud qoşa (**"**) dırnaq işarəsi ilə yaradıla bilər. Lakin qeyd olunacaq *string* tipli dəyişənin daxilində apostrof və yaxud tək dırnaq işarısi olacaqsa qoşa dırnaq işarəsi istifadə etmək daha məqsədəuyğundur. 

Nümunə: 
```python
x =  "Bakı"  
# yuxarıdakı sətr aşağıdakı sətr ilə eynidir 
x =  'Bakı'

# lakin aşağıdakı sətr fərqlidir

x = "I'm a developer"

x = 'I\'m a developer' # apostrof \ ilə ayırd edilir ki səhvə yol açmasın

```

