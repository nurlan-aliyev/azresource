
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
```
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
```
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
