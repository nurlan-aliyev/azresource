
# SQL nədir?
- SQL (<b>S</b>tructured <b>Q</b>uery <b>L</b>anguage) tərcümədə <i>Strukturlaşdırılmış Sorğu Dili</i> deməkdir.
- SQL vasitəsilə verilənlər bazasını yarada və idarə edə bilərsiniz

## SQL nəyə qadirdir?
- SQL verilənlər bazasına müxtəlif sorğular göndərə bilər
- SQL verilənlər bazasından məlumat əldə edə bilər
- SQL verilənlər bazasına məlumat əlavə edə bilər
- SQL verilənlər bazasındakı mövcud informasiyanı dəyişə bilər
- SQL verilənlər bazasından məlumat silə bilər
- SQL yeni verilənlər bazası yarada bilər
- SQL verilənlər bazasında cədvəllər yarada bilər
 
### Veb səhifənizdə SQL-dən istifadə:
Müəyyən verilənlər bazasından məlumat oxuyub istifadəçiyə göstərən veb səhifə yaratmaq üçün sizə aşağıdakılar lazımdır:

-  RDBMS verilənlər bazası proqramı (məs. MS Access, SQL Server, MySQL)
- Server yönümlü skriptləmə dili (məs. PHP və ya ASP)
- SQL-dən istifadə edərək istədiyiniz məlumatı əldə etmək
- HTML və CSS vasitəsilə səhifənin dizayn etmək
 
## RDBMS
RDBMS (<b>R</b>elational <b>D</b>atabase <b>M</b>anagement <b>S</b>ystem) tərcümədə <i>Əlaqəli verilənlər bazası idarəetmə sistemi</i> deməkdir.

<b>RDBMS</b>,  SQL dilinin əsasını təşkil edir

RDBMS daxilində saxlanılan məlumat, verilənlər bazasının elementlərindən biri olan <i>cədvəllərdə</i> saxlanılır. Cədvəl bir-biri ilə əlaqəli olan məlumatlardan ibarət olan bir elementdir,  sıralara və sütunlara bölünür. 
*** 
# Verilənlər bazasında cədvəllər
verilənlər bazası çox vaxt bir və ya bir neçə cədvəllərdən ibarət olur. Hər cədvəl özünəməxsus ad ilə seçilir. 

# SQL əmrləri
Verilənlər bazasında hər hansısa əməliyyatı yerinə yetirmək üçün SQL əmrlərinə ehtiyac duyulur. 

Aşağıdakı SQL əmri "Müştərilər" cədvəlindəki məlumatları alır:

Nümunə:
```sql
SELECT * FROM Customers;
```

Siz bir neçə SQL əmri haqqında bu yazılardan məlumat toplayacaqsınız.


<i><ins>Qeyd</ins></i> SQL əmrləri hamısı <b>BÖYÜK HƏRFLƏRLƏ</b> yazılır. 

# SQL dilində nöqtəli vergül
Bəzi verilənlər bazası sistemləri hər əmrin sonunda nöqtəli vergül tələb edir.

Bəzi vacib SQL əmrləri:

- <b>SELECT</b> - verilənlər bazasından məlumat alır
- <b>UPDATE</b> - bazadakı məlumatı yeniləyir
- <b>DELETE</b> - bazadakı məlumatı silir
- <b>INSERT</b> INTO - bazaya yeni məlumat daxil edir
- <b>CREATE DATABASE</b> - yeni verilənlər bazası yaradər
- <b>ALTER DATABASE</b> - bazanı dəyişir
- <b>CREATE TABLE</b> - yeni cədvəl yaradır
- <b>ALTER TABLE</b> - cədvəli dəyişir
- <b>DROP TABLE</b> - cədvəli silir
- <b>CREATE INDEX</b> - axtarış üçün indeks yaradır 
- <b>DROP INDEX</b> - indeksi silir
***
# SQL SELECT əmri

SELECT əmri verilənlər bazasından məlumat almaq üçün istifadə etmək üçün istifadə olunur.

Qaytarılan məlumat nəticə cədvəlində saxlanılır. 

```sql
SELECT Syntax
SELECT column1, column2, ...
FROM table_name;
```

Burada, column1, column2, ... məlumat istənilən cədvəlin sütun adlarıdır. Əgər cədvəldəki bütün məlumatı çağırmaq istəyirsinizsə aşağıdakı əmri icra etməlisiniz.
```sql
SELECT * FROM table_name;
```
Nümunə:

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>


Aşağıdakı SQL sorğusu "MüştəriAdı" və "Şəhər" sütunlarındakı məlumatları alır.

Nümunə:
```sql
SELECT CustomerName, City FROM Customers;
```

Aşağıdakı SQL sorğusu "Müştərilər" cədvəlindəki bütün məlumatları alır:

```sql
SELECT * FROM Customers;
```
***
# SQL SELECT DISTINCT əmri
SELECT DISTINCT əmri yeganə(fərqli) məlumatları çağırmaq üşün istifadə olunur. 

Cədvəl daxilində bir sütundə eyni dəyərə malik bir neçə məlumat ola bilir. Bu məıumatlardan təkrarlanmamaq şərti ilə verilən sorğu üçün SELECT DISTINCT əmri istifadə olunur. 

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

Nümunə: 
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>

Sadəcə <b>SELECT</b> əmri ilə nümunə. Aşağıdakı SQL əmri "Şəhər" sətrindən olan bütün məlumatları (eyni dəyərə malik olan kopyalar da daxil olmaqla) çağırır. 

```sql
SELECT Country FROM Customers;
```
İndi isə <b>SELECT DISTINCT</> əmrindən istifadə edək və nəticəni görək.

Nümunə:
```sql
SELECT DISTINCT Country FROM Customers;
```
Nəticə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>

Aşağıdakı SQL əmri fərqli müştəri şəhərlərinin sayını çap edir:

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

<i><ins>Qeyd:</ins></i> Yuxarısakı nümunə Firefox brauzerində çalışmır çünki həmin brauzer MS Access bazasından istifadə edir. 
***
# SQL WHERE şərti
WHERE şərti məlumatları filterləmək üçün istifadə olunur. 

Nümunə:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
<i><ins>Qeyd:</ins></i> WHERE şərti təkcə SELECT əmri ilə deyil UPDATE, DELETE, və s. əmrlərlə də işlənir.

Nümunə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>

Aşağıdakı nümunədə WHERE şərtinin istifadəsi göstərilmişdir, Müştərilər cədvəlindən "Bakı" şəhərinə olan məlumat göstəriləcək:

```sql
SELECT * FROM Customers
WHERE City='Bakı';
```

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>


## Mətn sahələri və ədədi sahələr
SQL mətn dəyişəninin ətrafında tək dırnaq işarəsini tələb edir. (Digər verilənlər bazaları qoşa dırnaq işarəsini də qəbul edə bilər).

Lakin, ədədi dəyişənlər dırnaq daxilində <ins>yazılmamalıdır.</ins>

Nümunə:
```sql
SELECT * FROM Customers
WHERE CustomerID=1;
```

Sorəudan alınan cavab:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
</table>

## WHERE şərti ilə istifadə olunan operatorlar:

- <b>\=</b>	Bərabərdir
- \>	Böyükdür
- \<	Kiçikdir
- \>=	Böyük bərabərdir
- \<=	Kiçik bərabərdir
- \<>	Bərabər deyil
- <b>BETWEEN</b>	Müəyyən aralıqda	
- <b>LIKE</b>	Hər hansısa şərtə uyğun axtarış üçün
- <b>IN</b>	Bir sütuna aid müctəlif qiymətlər üçün
	

<i><ins>Qeyd:</ins></i> SQL-in bəzi versiyalarında bərabər deyil operatoru "!="	kimi işarə olunur
***

# SQL dilində AND, OR və NOT Operatorları
WHERE şərti AND, OR və NOT operatorları ilə işlənə bilir.

AND və OR operatorları məlumatları birdən çox şərtə uyğun filtrləmək üçün istifadə olunur. 

- <b>AND</b> operatoru vasitəsilə verilən şərtin hər iki tərəfi <b>TRUE</b> dəyəri alırsa həmin məlumatlar çap olunur.
- <b>OR</b>operatoru vasitəsilə verilən şərtin hər hansı bir tərəfi <b>TRUE</b> dəyəri alırsa həmin məlumatlar çap olunur.
- <b>NOT</b> operatoru vasitəsilə verilən şərtin hər hansı bir tərəfi <b>NOT TRUE</b> dəyəri alırsa həmin məlumat(lar) çap olunur.

```sql
/* AND */
SELECT sütun1, sütun2, ...
FROM cedvel_adı
WHERE shert1 AND shert2 AND shert3 ...;
```

```sql
/* OR */
SELECT sütun1, sütun2, ...
FROM cedvel_adı
WHERE shert1 OR shert2 OR shert3 ...;
```
```sql
/* NOT */
SELECT sütun1, sütun2, ...
FROM cedvel_adı
WHERE NOT shert;
```
Nümunəvi verilənlər bazası:

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
</table>

<b>AND</b> operatoruna aid nümunə:

Aşağıdakı SQL nümunəsində verilmiş bazadan ölkə sütunu "İngiltərə" və şəhər sütunu "York" dəyərinə malik məlumatlar çap olunacaq:

```sql
SELECT * FROM Customers
WHERE Country='İngiltərə' AND City='York';
```
Nəticə:

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
</table>

<b>OR</b> operatoruna aid nümunə:

Aşağıdakı SQL nümunəsində verilmiş bazadan şəhər sütunu "York" və yaxud "Sabirabad" dəyərinə malik məlumatlar çap olunacaq:
```sql
SELECT * FROM Customers
WHERE City='York' OR City='Sabirabad';
```

Nəticə: 
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
</table>

<b>NOT</b> operatoruna aid nümunə:

Aşağıdakı SQL nümunəsində verilmiş bazadan ölkə sütunu "İngiltərə" olmayan məlumatlar çap olunacaq: 

Nümunə: 
```sql
SELECT * FROM Customers
WHERE NOT Country='İngiltərə';
```
Nəticə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
</table>

<b>AND, OR</b> və <b>NOT</b> operatorlarının birləşdirilməsinə aid nümunə:

Aşağıdakı SQL nümunəsində verilmiş bazadan ölkə sütunu "Azərbaycan" olan və şəhər ya "Bakı" ya da "Lerik" dəyərinə malik məlumatlar çap olunacaq (qoşqu şərtlər mötərizə daxilində yazılmalıdır.):

Nümunə:
```sql
SELECT * FROM Customers
WHERE Country='Azərbaycan' AND (City='Lerik' OR City='Bakı');
```

Nəticə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>

***
# SQL ORDER BY əmri
ORDER BY əmri nəticəni azalan və yaxud çoxalan sırada düzmək üçün istifadə olunur. 

ORDER BY nəticələri defolt olaraq artan sıra ilə düzür. Nəticələri azalan sıra ilə düzmək üçün DESC əmri istifadə olunur. 

Nümunə:

```sql
ORDER BY Syntax
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

Nümunəvi verilənlər bazası:

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
</table>

<b>ORDER BY</b> nümunəsi
Aşağıdakı SQL kodu cədvəldəki məlumatları "MüştəriAdı" sütununa uyğun artan sıra ilə sıralayır. 

Nümunə:

```sql
SELECT * FROM Customers
ORDER BY CustomerName;
```

Nəticə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>İngiltərə</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
</table>


Aşağıdakı SQL kodu cədvəldəki məlumatları "MüştəriAdı" sütununa uyğun azalan sıra ilə sıralayır. 

Nümunə:
```sql
SELECT * FROM Customers
ORDER BY Country DESC;
```

Nəticə:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>İngiltərə</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
</table>

***

# SQL INSERT INTO əmri
INSERT INTO əmri cədvələ yeni məlumatlar daxil etmək üçün istifadə olunur. 

INSERT INTO əmrini iki yolla istifadə etmək mümkündür: 

1. İlk olaraq həm sütun həm də daxil olunacaq məlumatları qeyd etmək lazımdır: 
```sql
INSERT INTO cedvel_adı (sütun1, sütun2, sütun3, ...)
VALUES (deyer1, deyer2, deyer3, ...);
```

2. Əgər cədvəlin bütün sütunlarına məlumat daxil olunursa sütun adları xüsusilə yazılmağına ehtiyac duyulmur. 

Nümunəvi verilənlər bazası:
<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
</table>

<b>INSERT INTO</b> əmrinə aid nümunə: 
```sql
INSERT INTO Customers (CustomerName, City,  Country)
VALUES ('Nurlan Aliyev', 'Lerik', 'Azərbaycan');
```
"Müştərilər" cədvəli artıq aşağıdakı formada olacaqdır:

<table>
<tr>
<th>MüştəriNo</th>
<th>MüştəriAdı</th>
<th>Şəhər</th>
<th>Ölkə</th>
</tr>
<tr>
<td>1</td>
<td>Ülvi Əlizadə</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>2</td>
<td>Murad Əmrəli</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>3</td>
<td>Böyükağa Bəyverdizadə</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>4</td>
<td>Həşim Həşimli</td>
<td>Bakı</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>5</td>
<td>Emin Əhədli</td>
<td>Sabirabad</td>
<td>Azərbaycan</td>
</tr>
<tr>
<td>6</td>
<td>Chris Brown</td>
<td>York</td>
<td>Ingiltərə</td>
</tr>
<tr>
<td>7</td>
<td>Nurlan Aliyev</td>
<td>Lerik</td>
<td>Azərbaycan</td>
</tr>
</table>

<i><ins>Qeyd:</ins></i> MüştəriNo sütununa heç bir müdaxilə olunmur, səbəb isə hər yeni məlumat daxil ediləndə avtomatik olaraq o sütunun yenilənməsidir. 

***
