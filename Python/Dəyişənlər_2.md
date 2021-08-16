# Python dəyişənləri - müxtəlif qiymətlərin dəyişənlərə təyin edilməsi

### Hər dəyişənə ayrı qiymətlərin verilməsi 
Python bir kod sətrində müxtəlif dəyişənlərə müxtəlif qiymətləri təyin etməyə imkan yaradır. 

Nümunə:
```python
x, y, z = "Portağal", "Banan", "Albalı"
print(x) #Portağal çap olunur
print(y) #Banan çap olunur
print(z) #Albalı çap olunur
```

# Bir qiymətin müxtəlif dəyişənlərə təyin edilməsi

Aşağıdakı nümunədə bir qiymətin müxtəlif dəyişənlərə verilməsi göstərilib.

Nümunə:
```python
x = y = z = "Armud"
print(x)
print(y)
print(z)
```

# List daxili qiymətlərin dəyişənlərə paylanması

Python list və yaxud tuple daxilindəki qiymətləri həmin sayda dəyişənlərə təyin etməyə imkan yaradır.

Nümunə:
```python
meyvələr = ["Alma", "Mango", "Ananas"]
x, y, z = meyvələr
print(x) #Alma çap olunur
print(y) #Mango çap olunur
print(z) #Ananas çap olunur
```
***
