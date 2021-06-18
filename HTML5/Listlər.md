
# HTML sıraları (listlər)
HTML sıraları, veb developerlərə bir-biri ilə əlaqəli olan bir neçə elementi grouplaşdırmaq imkanı yaradır. 

Nümunə:
### Nömrələnməmiş sıralar
- Element
- Element
- Element 

### Nömrələnmiş sıralar
1. Birinci Element 
2. İkinci Element
3. Üçüncü Element 

# Nömrələnməmiş sıralar
Nömrələnməmiş sıralar, `<ul>` teqi ilə başlanır. Hər sıra elementi isə `<li>` teqi ilə qeyd olunur. 

Bu sıra elementləri, default olaraq kiçik qara dairələrlə göstərilir.

Nümunə:
```html
<ul>
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>
```
<ul>
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>

# Nömrələnmiş sıralar 
Bu sıralar `<ol>` teqi ilə başlayır. Hər sıra elementi isə nömrələnməmiş sıralarda olduğu kimi `<li>` teqi ilə işarə olunur. 

Default olaraq bu sıralar rəqəmlərlə işarə olunur. 

Nümunə:
```html
<ol>
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>
```
<ol>
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

# Nömrələnməmiş sıraların işarəsinin dəyişdirilməsi
Sıra elementlərinin işarəsini dəyişmək üçün, **list-style-type** xüsusiyyətindən istifadə etmək lazımdır. Bu xüsusiyyət aşağıdakı dəyərləri ala bilir:

- disc - Default olaraq qara, kiçik dairələrdir
- circle - İçi boş, kiçik dairə
 - square - Qara, kiçik kvadrat
- none - Sıra elementi işarə ilə göstərilmir

Nümunə - Disc
```html
<ul style="list-style-type:disc;">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>
```
Nümunə - Circle
```html
<ul style="list-style-type:circle;">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>
```
Nümunə - Square
```html
<ul style="list-style-type:square;">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>
```
Nümunə - None
```html
<ul style="list-style-type:none;">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ul>
```
# İç-içə yazılmış sıralar 
list elementi olan `<li>` daxilində yeni sıra və ya başqa bir HTML elementini, məs. şəkili, linkləri və s. daşıya bilər
```html
<ul>
  <li>Kofe</li>
  <li>Çay</li>
    <ul>
      <li>Qara çay</li>
      <li>Yaşıl çay</li>
    </ul>
  </li>
  <li>Su</li>
</ul>
```
<ul>
  <li>Kofe</li>
  <li>Çay</li>
    <ul>
      <li>Qara çay</li>
      <li>Yaşıl çay</li>
    </ul>
  </li>
  <li>Su</li>
</ul>


# Üfüqi sıralar 
Sıraları CSS vasitəsilə fərqli formada stilini dəyişmək mümkündür. Bu yollardan ən çox istifadə olunanı, naviqasiya menyusu yaratmaq üçün istifadə olunan üfüqi sıralardır. 
```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 16px;
  text-decoration: none;
}

li a:hover {
  background-color: #111111;
}
</style>
</head>
<body>

<ul>
  <li><a href="#home">Ana sehife</a></li>
  <li><a href="#news">Xeberler</a></li>
  <li><a href="#contact">Elaqe</a></li>
  <li><a href="#about">Haqqımızda</a></li>
</ul>

</body>
</html>
```
# Nömrələnmiş sıra, type atributu 
Bu atribut, `<ol>` teqi daxilindəki səra elementlərinin, nömrələnmə növünü təyin edir

type atributunun aşağıdakı növləri vardır:

- **type="1"** - Sıra elementləri rəqəmlərlə işarələnəcək
- **type="A"** - Sıra elementləri böyük hərflərlə işarələnəcək 
- **type="a"** - Sıra elementləri kiçik hərflərlə işarələnəcək 
- **type="I"** - Sıra elementləri, böyük formatda Rum rəqəmləri ilə işarələnəcək
- **type="i"** - Sıra elementləri, kiçik formatda olan Rum rəqəmləri ilə işarələnəcək

Nümunə - Ədədlər:
`<ol type="1">`
<ol type="1">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

Nümunə - Böyük hərflər:
`<ol type="A">`
<ol type="A">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

Nümunə - Kiçik hərflər:
`<ol type="a">`
<ol type="a">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

Nümunə - Böyük Rum rəqəmləri:
`<ol type="I">`
<ol type="I">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

Nümunə - Kiçik Rum rəqəmləri:
`<ol type="i">`
<ol type="i">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

# Sıra nömrələnməsinin təyini
Default olaraq, nömrələnmiş sıralar, 1-dən başlayaraq sıralanır. Əgər xüsusi bir ədəddən başlanmasını istəyirsinizsə, onda start atributundan istifadə etmək lazımdır: 

Nümunə:
`<ol start="20">`
<ol start="20">
  <li>Çay</li>
  <li>Kofe</li>
  <li>Su</li>
</ol>

***
