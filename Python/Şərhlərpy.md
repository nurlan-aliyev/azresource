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