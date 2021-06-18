
# HTML Cədvəlləri
HTML cədvəlləri veb developerlərə, verilənləri sıralara və sətirlərə yerləşdirmək üçün imkan yaradır. 

## Cədvəllərin təyini
Bunun üçün, `<table>` elementindən istifadə olunmalıdır. Cədvəlin hər sətri `<tr>` teqi, hər başlıq `<th>`, hər məlumat xanası isə `<td>` teqi ilə işarə olunur. 

Default olaraq `<th>` (cədvəl başlığı) qalın və mərkəzdə yerləşir, `<td>` (məlumat xanası) isə adi font ölçüsünə malikdir və solda yerləşir. 

Nümunə:
```html
<table style="width:100%">
  <tr>
    <th>Ad</th>
    <th>Soyad</th>
    <th>Yaşı</th>
  </tr>
  <tr>
    <td>Murad</td>
    <td>Amirali</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Ülvi</td>
    <td>Alizade</td>
    <td>19</td>
  </tr>
</table>
```
<table style="width:100%">
  <tr>
    <th>Ad</th>
    <th>Soyad</th>
    <th>Yaşı</th>
  </tr>
  <tr>
    <td>Murad</td>
    <td>Amirali</td>
    <td>18</td>
  </tr>
  <tr>
    <td>Ülvi</td>
    <td>Alizade</td>
    <td>19</td>
  </tr>
</table>

## Cədvələ sərhəd əlavə olunması
Bunun üçün, CSS-in **border** xususiyyətindən istifadə etmək lazımdır. 

Nümunə:
```css
table, th, td {
  border: 1px solid black; //serhed
}
```
## Sıxılmış sərhəd xüsusiyyəti, border-collapse
Default olaraq, cədvəlin sərhədi 2 xətdən ibarətdir. Sərhədi bir xətdən ibarət etmək üçün, **border-collapse** xüsusiyyətindən istifadə etmək lazımdır. 

Nümunə:
```css
table, th, td {
  border: 1px solid black;//serhed
  border-collapse: collapse;//serhedin yığılması
}
```
## Məlumat və onun sərhədi arasında məsafə təyini
Bu məsafə cədvəlin görünüşünə təsir edir və təyin olunmasa cədvəldəki məlumatlarla onların yerləşdiyi xanaların arasında məsafə olmur. Məsafəni təyin etmək üçün, CSS-in **padding** xususiyyətindən istifadə etmək lazımdır.

Nümunə:
```css
th, td {
  padding: 15px;//boşluq
}
```
## Başlıqları xananın sol tərəfində yerləşdirilməsi
Default olaraq, başlıqlar qalın olur və mərkəzdə yerləşir. Bu başlıqları xananın soluna sürüşdürmək üçün, CSS-in **text-align** xüsusiyyətindən istifadə olunur. 

Nümunə:
```css
th {
  text-align: left;//sola sürüşdürme
}
```
## Sütunların birləşdirilməsi
Bir xanadakı məlumatın, birdən çox sütunü əhatə etməsi üçün CSS-in **colspan** atributundan istifadə etmək lazımdır. 

Nümunə:
```html
<table style="width:100%">
  <tr>
    <th>Ad</th>
    <th colspan="2">Ünvan</th>
  </tr>
  <tr>
    <td>Koroğlu</td>
    <td>Çenlibel, 13</td>
  </tr>
</table>
```
<table style="width:100%">
  <tr>
    <th>Ad</th>
    <th colspan="2">Ünvan</th>
  </tr>
  <tr>
    <td>Koroğlu</td>
    <td>Çenlibel, 13</td>
  </tr>
</table>

## Sətrlərin birləşdirilməsi
Bir xanadakı məlumatın, birdən çox sətri əhatə etməsi üçün CSS-in **rowspan** atributundan istifadə etmək lazımdır. 

Nümunə: 
```html
<table style="width:100%">
  <tr>
    <th>Ad:</th>
    <td>Koroğlu</td>
  </tr>
  <tr>
    <th rowspan="2">Ünvan:</th>
    <td>Çenlibel, 13</td>
  </tr>
</table>
```
<table style="width:100%">
  <tr>
    <th>Ad:</th>
    <td>Koroğlu</td>
  </tr>
  <tr>
    <th rowspan="2">Ünvan:</th>
    <td>Çenlibel, 13</td>
  </tr>
</table>

## Cədvəl adı
Cədvələ ad vermək üçün, **caption** teqindən istifadə olunur. 

Nümunə:
``` html
<table style="width:100%">
  <caption>Jurnal</caption>
  <tr>
    <th>Ay</th>
    <th>Xercler</th>
  </tr>
  <tr>
    <td>Yanvar</td>
    <td>100 AZN</td>
  </tr>
  <tr>
    <td>Fevral</td>
    <td>125 AZN</td>
  </tr>
</table>
```
<table style="width:100%">
  <caption>Jurnal</caption>
  <tr>
    <th>Ay</th>
    <th>Xercler</th>
  </tr>
  <tr>
    <td>Yanvar</td>
    <td>100 AZN</td>
  </tr>
  <tr>
    <td>Fevral</td>
    <td>125 AZN</td>
  </tr>
</table>

<ins>*Qeyd*:</ins> `<caption>` teqi, `<table>` teqindən dərhal sonra əlavə olunmalıdır.


## Cədvəlin xüsusiləşdirilməsi
Müəyyən cədvəl üçün xüsusi bir dizayn yaratmaq istəyirsinizsə, bu cədvələ id atributu əlavə olunmalıdır. 

Nümunə:
```html
<table id="c01">
  <tr>
    <th>Ad</th>
    <th>Soyad</th>
    <th>Doğum ili</th>
  </tr>
  <tr>
    <td>Alan</td>
    <td>Turing</td>
    <td>1912</td>
  </tr>
</table>
```
İndi isə bu cədvəli xüsusiləşdirmək üçün CSS-dən istifadə olunur: 
```css
#c01 {
  width: 100%;
  background-color: #f1f1c1;
}
#c01 tr:nth-child(even) {
  background-color: #eee;
}
#c01 tr:nth-child(odd) {
  background-color: #fff;
}
#c01 th {
  color: white;
  background-color: black;
}
```
Burada qeyd olunan **tr:nth-child** xüsusiyyəti, cədvəl sırasının n-ci elementini seçir. **nth-child(even)** - *cüt* sıradakı, **nth-child(odd)** - *tək* sıradakı elementlər daxildir 

# Xülasə
- `<table>` elementi vasitəsilə cədvəl təyin olunur
- `<tr>` elementi vasitəsilə cədvəl sətri təyin olunur 
- `<td>` elementi vasitəsilə cədvələ məlumat daxil edilir
- `<th>` elementi vasitəsilə cədvəl başlığı təyin olunur
- `<caption>` elementi vasitəsilə, cədvələ ad verilir
- CSS-in **border** xüsusiyyəti ilə cədvəlin sərhədi təyin olunur
- CSS-in **border-collapse** xüsusiyyəti ilə, sərhədi 2 xətdən 1 xətdə çevirmək olur
- CSS-in **padding** xüsusiyyəti ilə, xanalara daxili məsafə(boşluq) verilir
- CSS-in **text-align** xususiyyəti ilə, cədvəl yazılarının, xanaya görə yerləşməsi təyin olunur
- **colspan** atributu vasitəsilə, bir neçə sütun birləşdirilir
- **rowspan** atributu ilə bir neçə sətr birləşdirilir 
- **id** atributu ilə cədvələ xüsusi nişan verilir

***
