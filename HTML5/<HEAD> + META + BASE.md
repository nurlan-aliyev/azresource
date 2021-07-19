Meta + Base elementləri

```html
<head>
<base href="https://www.saytadi.com/"  target="_blank">  
```
 -saytdakı bütün şəkil, video və digər faylların sırf burda çəkilən saytdan almasını qeyd edir. başqa hostingdəki (sayt yaddaşındakı) fayllar yüklənmir.
```html
...
<meta charset="UTF-8">
```
(***UTF-8*** simvol (hərf/rəqəm/işarə) toplusu olan bir beynəlxaq simvol standartıdır.
Normalda HTML5-dən öncə kompüterlərdə ASCII və yaxud 255 simvoldan ibarət olan ANSII standartı var idi. 28 kiçik və 28 böyük olmaqla latın hərfləri, 0-9 aralığında rəqəmlər və  (**"* /+ - ( ) , ş & ^ % # @"**)  işarələri bu standarta daxildir.
Lakin, **Unicode** (*Universal Code*) standartlaşdırıldıqdan sonra dünya üzərindəki bütün dillərin hərfləri (Çin, Yapon, Ərəb, Gürcü, Fars, Ölü dillər və o cümlədən Azərbaycan hərfləri Ə, Ö, Ğ, Ç Ş, Ü, I və s.) əlavə edildi. İndilərdə bu standartda 3000-dən çox simvol mövcuddur. 

```
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
<meta name="description" content="Sayt haqqında bilgi">
<meta name="keywords" content="Acar soz, Açar Söz, HTML, DƏRSLİK" >
<meta name="author" content="Müəllif S-n Amil" >
<meta name="viwport" content="width-device-width", "initial-scale=1.0" >  (cihazınızın ekran ölçüsünə görə veb səhifənin uyğunlaşması, saytın ekrana uzlaşması.

</head>
```
