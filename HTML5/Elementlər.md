
# HTML Elementləri
HTML elementi başlanğıc teqi, sonluq teqi və daxilindəki məlumatla təyin olunur. 

Nümunə: 

`<teqadı>Teqdaxili məlumatlar...</teqadı>`

# İç-içə yerləşən HTML elementləri
HTML elementləri bir birinin daxilində yer ala, yəni biri digərinə daxil ola bilər. Və bütün HTML sənədlərində iç-içə yerləşmiş elementlər vardır. 

Növbəti nümunədə 4 elementdən ibarət bir HTML sənədi göstərilmişdir:
```html
<!DOCTYPE html>
<html>
<body>

<h1>Sadə başlıq</h1>
<p>Sadə paraqraf</p>

</body>
</html>
```
Nümunənin izahı:
`<html>` elementi sənədin əsas elementidir və digər o, bütün HTML sənədini təyin edir. Onun başlanğıc teqi–`<html>`, sonluq teqi isə–`</html>` kimi qəbul olunur. `<html> `elementinin daxilində isə `<body>` elementi yerləşir. Bu element, səhifənin "gövdəsini" təyin edir. Başlanğıc teqi `<body>`, sonluq teqi isə `</body>` kimi işarə olunur. 

`<body>` elementinin daxilində isə 2 element, `<h1>` və `<p>` elementləri yerləşir. `<h1>` elementi başlığı təyin edir, başlanğıc teqi `<h1>` sonluq teqi isə `</h1>` kimi işarə olunur. `<p>` elementi paraqraf təyin edir və `<p>` teqi ilə başlanıb, `</p>` teqi ilə sonlanır. 

# Sonluq teqini unutmaq olmaz!
Bəzi HTML elementlərinin sonluq teqi qeyd olunmasa belə brauzer tərəfindən göstərilir: 

Nümunə: 
```html
<html>
<body>

<p>Teqsiz paraqraf 1
<p>Teqsiz paraqraf 2

</body>
</html>
```
Bu metod düzgün nəticə göstərsə də, istifadəsi məqsədə uyğun deyil və birmənalı olaraq sonluq teqlərindən istifadə etmək lazımdır. 

# Boş HTML elementləri
Daxilində məlumat daşımayan və sonluq teqi olmayan elementlər boş elementlər adlanır. Bunlara misal olaraq `<br>` elementini göstərə bilərik. `<br>` elementi cari sətirdən yeni sətrə keçir və sonluq teqi olmur. 

Nümunə: 

`<p>Bu paraqraf artıq <br> yeni setrden başlayır.</p>`

***
