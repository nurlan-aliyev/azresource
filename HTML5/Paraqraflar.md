
# HTML Paraqrafları
Paraqraflar həmişə yeni sətrdən başlayır və çox vaxt mətn bloku olur. Paraqraflar `<p>` elementi ilə təyin olunur və brauzerlər avtomatik olaraq, paraqrafın əvvəli və sonuna boşluq əlavə edir ki, digər elementlərdən fərqlənsin. 

Nümunə:
```html
<p>Bu paraqrafdır</p>
<p>Bu digər bir paraqrafdır</p>
```

HTML sənədinin brauzerdə necə görünəcəyini əvvəlcədən bilmək olmur. Çünki müxtəlif ölçülü cihazlarda bu sənədə baxılarkən, həmin sənəd müxtəlif formalarada görünə bilər. HTML vasitəsilə, elementlər daxili mətnə boşluq qoymaqla görünüşü dəyişə bilməzsiniz. Brazuer HTML sənədini oxuyub nümayişə hazır vəziyyətə gətirən zaman bütün lüzumsuz boşluq və sətrləri silir. 

Nümunə:
```html
<p>
Bu paraqraf elementi
çoxlu sətrlərdən 
ibarət olsa da
brauzer buna 
diqqət vermir
</p>

<p>
Bu paraqraf      çoxlu
  boşluqlardan  ibarət
olsa da, brauzer 
       buna diqqət 
etmir.
</p>
```
<p>
<b>Bu paraqraf elementi
çoxlu sətrlərdən 
ibarət olsa da
brauzer buna 
diqqət vermir</b>
</p>

<p>
<b>Bu paraqraf      çoxlu
  boşluqlardan  ibarət
olsa da, brauzer 
       buna diqqət 
etmir. </b>
</p>

# HTML-də üfuqi xətt
`<hr>`  teqi əsasən, HTML səhifəsindəki mövzu dəyişikliyi zamanı istifadə olunur və səhifədə üfuqi bir xətt çəkir. 

Nümunə:
```html
<h1>Başlıq 1</h1>
<p>Sadə paraqraf</p>
<hr>
<h2>Başlıq 2</h2>
<p>Sadə paraqraf 2</p>
<hr>
```
`<hr>` teqi boş elementdir, yəni onun sonluq teqi mövcud deyil. 

# `<br>` elementi
Bu element HTML sənədinin cari sətrini sonlandırıb yeni sətrə keçid edir:

Nümunə:
```html
<p>Bu paraqrafda<br>müxtəlif<br>sətr keçidləri var.</p>
```
<p><b>Bu paraqrafda<br>müxtəlif<br>sətr keçidləri var.</b></p>

`<br>` teqi də boş elementdir, yəni sonluq teqi mövcud deyil.

# `<pre>`elementi
Bu elementin əsas özəlliklərindən biri, daxilinə yazılmış mətni olduğu kimi, və boşluqları silmədən göstərməsidir. Əsasən şeir və yaxud hər hanısa proqramın kod hissəsini sənəddə göstərmək üçün ondan istifadə edilir. 

Nümunə:
```html
<pre>
    Bu yazılar olduğu  kimi
        boşluqlarla birgə göstəriləcək
</pre>
```

<pre>
    <b>Bu yazılar olduğu  kimi
        boşluqlarla birgə göstəriləcək</b>
</pre>

***
