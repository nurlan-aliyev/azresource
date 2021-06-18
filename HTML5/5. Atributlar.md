
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
