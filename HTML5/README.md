
  
# HTML nədir?

- HTML Hyper Text Markup Language yəni, Hiper Mətn Nişanlama dili mənasını verir
- HTML veb səhifələr üçün standart nişanlama dilidir
- HTML veb səhifələrin strukturunu təyin edir
- HTML bir neçə elementlərdən ibarətdir
- HTML veb brauzerə, səhifənin içindəkiləri necə nümyaiş etmək lazım olduğunu göstərir 

Sadə bir HTML sənədi:
```html
<!DOCTYPE html> 
<html>
<head>
<title>Səhifənin başlığı</title>
</head>
<body>

<h1>Sadə başlıq</h1>
<p>Sadə paraqraf</p>

</body>
</html>
```
Nümunənin izahı: 
`<!DOCTYPE html>` teqi lazımlıdır, hər bir HTML sənədində yazılmalıdır və o brauzerə sənədin HTML5 versiyasında yazıldığını göstərir
`<html>` yazılmış HTML sənədinin əsas elementidir və səhifənin əsasını təşkil edir
`<head>` elementi, sənəd haqqında lazımi məlumatların və yaxud linklərin yerləşdiyi teqdir
`<title>` elementi, HTML sənədinin başlığını təyin edir. (bu başlıq brauzerdə göstərilir)
`<body>` elementi, səhifənin "gövdəsi"-ni təyin edir və burada brauzer tərəfindən göstərilən elementlər yer alır (məs. başlıqlar, paraqraflar, şəkillər, linklər, cədvəllər və s.) 
`<h1>` elementi, mövcud olan ən vacib və ən böyük başlıq elementidir
`<p>` elementi paraqrafı təyin edir

# HTML Elementi nədir? 

HTML elementi teq başlanğıcı (**<**), teq adı və teq sonundan (**>**) ibarətdir. 

`<teqadı>Teq daxili yazılar</teqadı>`

<ins>*Qeyd*:</ins> Bəzi HTML elementlərinin daxilində heç bir şey olmur. Belə elementlər boş element adlanır və bunlara misal olaraq `<br>` elementini göstərmək olar. Boş elementlərin sonluq teqi olmur! 

***

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

# HTML atributları
HTML atributları, HTML elementlərinə əlavə məlumat daxil etmək üçün istifadə edilir. 

Bütün HTML elementlərinə atribut əlavə etmək mümkündür
Atributlar başlanğıc teqdə qeyd olunur
Atributlar əsasən ad/dəyər cütü formasında qeyd olunur məs. `style:"color:red;"`

## href atributu
`<a>` teqi hiperlinkdir və href atributu həmin linkin yönlənəcəyi səhifənin URL adresini təyin edir:

Nümunə:

`<a href="https://www.wikipedia.org">Wikipedia-dan oxu</a>`

## src atributu
src ingilis dilində olan "source" yəni mənbə sözünün qısaldılmasıdır. Və bu atributdan çoxlu elementlərdə istifadə olunur. Misal olaraq HTML səhifəsinə şəkil əlavə etmək üçün istifadə olunan `<img>` elementində src atributu, şəklin adresini təyin edir. 

Nümunə: 

`<img src="tesla_model_y.jpg">`

## width və height atributları
width ingilis dilindən tərcümədə "en", height isə "hündürlük" deməkdir. Şəkil əlavə olunarkən `<img>` elementində src atributundan əlavə olaraq width və height atributları da qeyd olunmalıdır. Bu atributların ölçü vahidi pikseldir. 

Nümunə:

`<img src="tesla_model_y.jpg" width="250" height="300">`

## alt atributu
alt ingilis sözü olan "alternative" sözünün qısaltmasıdır və əsasən `<img>` elementində istifadə olunur. Əgər hər hansısa səbəbə görə şəkil göstərilə bilmirsə, həmin alternativ mətn şəkilin yerinə göstərilir. Və yaxud səhifəni hər hansısa oxucuyla oxudanda şəkilin alt mətni oxudulur. 

Nümunə:

`<img src="tesla_model_y.jpg" alt="Tesla Model Y avtomobili">`

## style attributu
style atributu vasitəsilə HTML elementlərinə rəng, şrift, ölçü və s. xüsusiyyətlər əlavə edilir. 

Nümunə:

`<p style="color:red;">Qırmızı rengli paraqraf</p>`

## lang attributu
İngilis dilindən tərcümədə "dil" mənasını verən "language" sözünün qısaltması olan lang atributu, səhifənin dili barədə axtarış motorlarına və brauzerlərə məlumat verir və vacib sayılan atributlardan biridir. Həmişə <html> teqinin içində qeyd olunmalıdır. 

Aşağıdakı nümunədə səhifənin dili İngilis dili kimi təyin olunur:

```html
<!DOCTYPE html>
<html lang="en">
<body>
...
</body>
</html>
```

## title atributu
Bu atribut element haqqında məlumat vermək üçün istifadə olunur, əsasən mausu elementin üstünə gətirib saxladıqda bu mətn görünür. 

Nümunə:

`<p title="Paraqraf haqqında məlumat">Sade paraqraf</p>`

Qeyd: Bütün atributlar böyük hərflə yazıla bilər məs. SRC, HREF və s. Amma bu tövsiyə olunan deyil, beynəlxalq konsortium kiçik hərflərlə yazmağı tövsiyyə edir. Və həmişə atributların daşıdığı dəyəri ("") daxilində yazmağınız tövsiyyə olunur. 


Tövsiyyə olunan: 

`<a href="https://www.youtube.com/">YouTube</a>`

Qəbul olunmaz:

`<a href=https://www.youtube.com/>YouTube</a>`


Xülasə:
Bütün HTML elementlərinin atributları ola bilər

 - `<a>` elementinin href atributu səhifənin yönləndiyi URL adresini təyin edir
 - `<img>` elementinin src atributu, göstərilən şəklin adresini təyin edir 
 - `<img>` elementinin width və height atributları, uyğun olaraq şəklin eni və hündürlüyü (uzunluğudur) 
 - `<img>` alt atributu, şəkil haqqında olan alternativ mətndir
style atributu, elementə rəng, şrift, ölçü və s. xüsusiyyətləri təyin etmək üçün istifadə olunur
- `<html>` teqi daxilindəki lang atributu veb səhifənin dilini təyin edir 
title atributu element haqqında əlavə məlumat göstərmək üçün istifadə olunur

***

# HTML Başlıqları
HTML başlıqları, adından da göründüyü kimi səhifədəki yazıların başlıqlarını qeyd etmək üçün istifadə olunan teqlərdir, kiçik h hərfi ilə işarə olunur və 1-dən 6-ya qədər ölçüsü azalaraq gedir. 

Nümunə:

- <h1> Başlıq 1</h1>
- <h2> Başlıq 2 </h2>
- <h3> Başlıq 3 </h3>
- <h4> Başlıq 4 </h4>
- <h5> Başlıq 5 </h5>
- <h6> Başlıq 6 </h6>

Bu başlıqlar `<h1>` – `<h6>` arasında olur. `<h1>` ən vacib başlıq, `<h6>` isə çox vacib olmayan başlıqdır. 

Nümunə:
```html
<h1>Başlıq 1</h1>
<h2>Başlıq 2</h2>
<h3>Başlıq 3</h3>
<h4>Başlıq 4</h4>
<h5>Başlıq 5</h5>
<h6>Başlıq 6</h6>
```
Axtarış motorları (Google, Bing, Yandex və s.) veb səhifələrin strukturlarını və içindəkilərini indeksləmək (axtarış zamanı lazım olur) üçün, səhifədə mövcud olan başlıqlardan istifadə edir. İstifadəçilər əsasən axtarış zamanı qabaqlarına çıxan başlıqlara uyğun səhifələrə girir. Buna görə də veb səhifədə ən vacib şeylərdən biri də başlıqlardır. 

<ins>*Qeyd:*</ins> HTML başlıqlarından yalnızca sənəd başlıqları üçün istifadə edin. Bu başlıqlardan hər hansısa sözü böyük və qalın göstərmək üçün istifadə eləsəniz axtarış motorları səhifənizi düzgün indeksləyə bilməz. 

Hər başlığın qabaqcadan təyin olunmuş şrift ölçüsü olsa da, siz onları CSS (haqqında danışılacaq) vasitəsi ilə istədiyiniz ölçünü verə bilərsiniz. 

Nümunə:

`<h1 style="font-size:56px;">Başlıq 1</h1>`

***

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

# HTML linkləri
Demək olar ki, bütün veb səhifələrdə linklər mövcuddur. Linklər istifadəçilərə bir səhifədən digərinə keçid etmə imkanı yaradır.

Mausu linkin üzərinə gətirdikdə, onun işarəsi dəyişib əl işarəsinə çevrilir. Və linklər sadəcə mətndən ibarət olmur, istənilən elementdən link kimi istofadə etmək mümkündür.

# Linklərin yazılma qaydası

`<a href="url">link mətni</a>`

`<a>` link elementinin ən əsas atributu, linkin yönləndiyi adresi bildirən ***href***-dir. 

Nümunə:
Aşağıdakı nümunədə, Google axtarış sisteminə yönlənmiş linkin yaradılması göstərilib:

`<a href="https://www.google.com/">Google-da axtar</a>`
<a href="https://www.google.com/">Google-da axtar</a>

İlkin olaraq bütün brauzerlərdə linklər aşağıdakı formalarda olur:

- Kliklənməmiş linkin altından xətt çəkilir və mavi rəngdə olur
- Kliklənmiş linkin altından xətt çəkilir və çəhrayı rəngdə olur
- Kliklənmiş və aktiv olan linkin altəndan xətt çəkilir və qırməzı rəngdə olur

<ins>*Qeyd*:</ins> Linklərin stili **CSS**(**C**ascading **S**tyle **S**heets) vasitəsilə dəyişilir və istənilən formaya salına bilər.

# target atributu
*Default* (qabaqcadan təyin olunmuş hal) olaraq səhifədə açılan linklər veb brauzerin cari pəncərəsində göstərilir. Bunu dəyişdirmək üçün target atributundan istifadə etmək lazımdır:

target atributu aşağıdakı qiymətləri ala bilər:

- _self - Default olaraq linki cari pəncərədə açır.
- _blank - Linki yeni brauzer pəncərəsində açır. 
- _parent - Link əsas çərçivədə açılır. 
- _top - Link ən üst çərçivədə açılır. 

Nümunə:
**target="_blank"** vasitəsilə linki yeni brauzer pəncərəsində açın: 

`<a href="https://www.freecodecamp.org/" target="_blank">FreeCodeCamp-a keçid et</a>`
<a href="https://www.freecodecamp.org/" target="_blank">FreeCodeCamp-a keçid et</a>

# Şəkillərdən link kimi istifadə
Şəkili link kimi istifadə etmək üçün, `<img>` elementini `<a>` elementinin daxilində qeyd edin.

Nümunə: 
```html
<a href="default.asp">
<img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
</a>
```
# Email adresinə yönləndirmək
Bunun üçün href atributunun daxilində ***mailto*** yazmaq lazımdır

Nümunə:

`<a href="mailto:someone@example.com">Email göndər</a>`

# Link başlıqları
***title*** atributu element haqqında əlavə məlumat verir. Mausu həmin elementlərin üzərinə gətirdikdə bu mətn element üzərində göstərilir.

Nümunə:

`<a href="https://www.youtube.com" title="Youtube-a keçid et">YouTube-dan bax</a>`
<a href="https://www.youtube.com" title="Youtube-a keçid et">YouTube-dan bax</a>

# Link rənginin dəyişdirilməsi
Link rənglərini CSS vasitəsilə dəyişmək mümkündür.

Aşağıdakı nümunədə, klinklənməmiş link yaşıl rəngdə olacaq və altından xətt çəkilməyəcək. Kliklənmiş link çəhrayı olacaq və altından xətt çəkilməyəcək. Və aktiv link sarı olacaq və altından xətt çəkiləcək.  Əlavə olaraq da, mausu linkin üzərinə gətirdikdə onun rəngi qırmızı olacaq və altından xətt çəkiləcək. 

Nümunə:
```html
<style>
a:link {
  color: green; //yaşıl
  background-color: transparent;
  text-decoration: none; //altdanxett yığışdırılır
}

a:visited {  //klinklenmiş link
  color: pink; //çehrayı
  background-color: transparent;
  text-decoration: none; //altdanxett yığışdırılır
}

a:hover { //üzerine gelende
  color: red; //qırmızı
  background-color: transparent;
  text-decoration: underline; //altdanxett
}

a:active { //aktiv link
  color: yellow; //sarı
  background-color: transparent;
  text-decoration: underline; //altdanxett
}
</style>
```
# Əlfəcinlər (Bookmarks)
Linklər vasitəsilə HTML sənədində əlfəcin və yaxud bookmark (bukmark) yaratmaq mümkündür. Bookmarkların əsas özəlliyi, klikləndiyi zaman istifadəçini səhifənin müəyyən edilmiş hissəsinə yönləndirir. 

Bunu əldə etmək üçün ilk növbədə bookmarkın özünü təyin edib sonradan link vasitəsilə ona yönləndirmək lazımdır. Link kliklənəndə, səhifə bookmarkın yerləşməsinə uyğun aşağı və yaxud yuxarı doğru hərəkət edir. 

Nümunə:
İlk növbədə bookmark yaratmaq üçün id atributu istifadə edilir, sonra isə həmin atributa yönlənən bir link yaradılır: 
```
<h2 id="BirinciBolme">Birinci bölməyə</h2>

<a href="#BirinciBolme">Birinci bölməyə keçid et</a>
```
***

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

# HTML Şərhləri
HTML şərhləri brauzerdə göstərilmir amma onlar sizə yazdığınız kodu başqaları tərəfindən oxunmasını daha da rahatlaşdırır.

## HTML şərh teqləri

Aşağıda göstərildiyi kimi HTML faylına şərh əlavə etmək lazımdır:

`<!-- Şerhleri bura yazın -->`

Fikir verdinizsə, nida işarəsi **(!)** başlanğıcında istifadə olunsa da, sonda istifadə olunmur. 

<ins>*Qeyd:*</ins> Şərhlər brauzer tərəfindən istifadəçilərə göstərilmir və onlar sizə HTML faylının oxunmasını daha da rahatlaşdırmağa imkan yaradır. 

Şərhlərdən istifadə etməklə siz HTML kodunda hər hansısa bir bölməni geniş izah edə və yadda saxlamaq üçün bəzi qeydlər apara bilərsiniz. 

Nümunə:
```html
<!-- Sade şerh -->

<p>Sade paraqraf</p>

<!-- Yadda saxlamaq üçün yazılan qeyd -->
```
Şərhlərdən həmçinin yeni bir kod sətrini yoxlamaq və yaranan problemə həll tapana kimi müvəqqəti yaddaş yeri kimi istifadə etmək də olar: 

Nümunə: 
```html
<!-- Aşağıdakı şekil gösterilmeyecek
<img  src="bina.jpg" alt="Bina">
-->
```
***

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
