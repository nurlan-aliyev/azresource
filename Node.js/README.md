
# Node.js nədir?
- Node.js açıq qaynaqlı server mühitidir
- Node.js pulsuz istifadəlidir
- Node.js müxtəlif platformalarda çalışır (Windows, Linux, Unix, Mac OS X, və s.)
- Node.js server tərəfdən JavaScript istifadə edir

# Niyə Node.js?
Node.js asinxron (bir-birindən asılı olmayaraq müxtəlif kod bloklarının icra olunması mənasını verir) proqramlaşdırma məntiqi ilə çalışır.


Fayl mübadiləsini PHP və ya ASP aşağıdakı formada həll edirlər:

- Əməliyyatı kompüterin fayl sisteminə göndərir
- Fayl sisteminin göndərilən faylın açılıb oxunmasını gözləyir
- Alınan məzmunu istifadəçiyə geri qaytarır
- Növbəti sorğu üçün artıq hazır vəziyyətə gəlir


Fayl mübadiləsini Node.js isə aşağıdakı formada həll edir: 

- Əməliyyatı kompüterin fayl sisteminə göndərir
- Növbəti sorğu üçün artıq hazır vəziyyətə gəlir
- Fayl sistemi faylı açıb oxuduqdan sonra server artıq məzmunu istifadəçiyə qaytarır
- Node.js gözləməni ləğv edir və növbəyi sorğuya keçir 

Node.js tək prosesli( verilmiş anda tək kod vahidini icra edir ), bloklanmayan, asinxron proaramlaşdırmadan istifadə edir və bu yaddaş cəhətdən çox səmərəlidir. 

# Node.js nəyə qadirdir?
- Node.js səhifə üçün dinamik məzmun yarada bilər
- Node.js serverdə faylı yarada, aça, oxuya, yaza, silə və bağlaya bilər 
- Node.js formlardan məlumat yığa bilər
- Node.js verilənlər bazasına məlumatı əlavə edə, silə və modifiyə edə bilər 

### Node.js faylı nədir?
- Node.js faylları müxtəlif hadisələr (event) üzərində icra olunacaq əməliyyatları özündə birləşdirir
- Həmin bu hadisələrə nümumə olaraq istifadəçinin serverdəki portlardan birini əldə etməsi göstərilə bilər 
- Node.js faylları hər hansısa effektə sahib olmaları üçün üabaqcadan serverə yerləşdirilməlidir 
- Node.js fayllarının sonluğu ".js" kimi qeyd olunur
***
## Node.js üçün endirilmə qaydası
Rəsmi Node.js vebsəhifəsində Node.js üçün endirilmə qaydaları qeyd olunub: <a href="https://nodejs.org" target="_blank">Endirmək üçün klikləyin</a>

## İlk anlayışlar
Kompüterinizə Node.js endirib qurlaşdırdıqdan sonra veb brauzerdə "Salam Dünya" yazısını çap edək:

"ilkFayl.js" adlı Node.js faylını yaradıb daxilinə bu kodları yazaq:

```js
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Salam Dünya!');
}).listen(8080);
```

Və bu faylı kompüterinizdə ya iş nasasında ya da öz seçdiyiniz fayl daxilində saxlayın. 

Əgər hər hansısa istifadəçi kompüterinizin 8080 portuna qoşulsa kod onlarə salamlayacaq. 

İndilik kodu başa düşyinizə ehtiyac yoxdur. Kodu daha sonra izah edəcəyik. 

<strong>əmrlər sətri</strong> (məs. <b>CMD</b>)
Node.js faylları kompüterinzin əmrlər sətri proqramı vasitəsilə başladılmalıdır. 

Həmin bu programı açmaq isə əməliyyat sistemindən asılı olaraq dəyişir. Windows istifadəçiıəri üçün "Start" düyməsi sıxılır və <b>"CMD"</b> proqramı çağırılır. 

"ilkFayl.js" faylının yerləşdiyi fayla naviqasiya etdikdən sonra yaratdığımız faylı başlatmaq üçün aşağıdakı sətr yazılır: 

```
node ilkFayl.js
``` 

Artıq sizin kompüteriniz server kimi fəaliyyət göstərir!

Seçdiyiniz veb brauzer vasitəsilə <a href="http://localhost:8080" target="_blank">http://localhost:8080</a> ünvanına daxil olsanız qarşınıza "Salam Dünya!" yazısı çıxacaq.
***
# Node.js modulu nə deməkdir?
Modulları JavaScript kitabxanaları ilə bir tutmaq olar.  

### Qabaqcadan yaradılmış modullar 
Node.js sizi endirmə etmədən bir çox istifadəyə hazır kitabxanalarla təmin edir. Bu kitabxanaları "Google" vasitəsilə axtara bilərsiniz. 

## Modulların əlavə edilməsi
Modulları proqramlara əlavə etmək üçün <b>require()</b> funksiyasından istifadə olunur. 

```js
var http = require('http');
```

Bu kod vasitəsilə artıq <b>HTTP</b> modulu proqrama əlavə olunur. Artıq server yaratmaq üçün aşağıdakı kodları yazmaq bəs edəcək: 

```js 
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Salam Dünya!');
}).listen(8080);
```
## İstifadəçi tərəfindən yaradılan modullar
Siz öz modullarınızı asanlıqla yaradıb proqrama əlavə edə bilərsiniz. 

Aşağıdakı kod vasitəsilə tarix və zaman qaytaran modulu yaratmaq mümkündür:


Nümunə:
```js 
exports.tarixZaman= function () {
  return Date();
};
```
<b>exports</b> vasitəsilə modulu proqramdan kənara ixrac etmək mümkündür, yəni artıq bu modul proqramdan kənarda da işləyəcək. 

Yuxarıdakı faylı "ilkModul.js" kimi yadda saxlayırıq.


## Öz yaratdığınız modulun proqrama əlavə olunması
Yuxarıdakı əməliyyatları yerinə yetirdikdən sonra yaratdığınız modulu istənilən Node.js faylında istifadə edə bilərsiniz. 

Nümunə:
```js
var http = require('http');
var dt = require('./ilkModul');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("İndiki tarix və zaman: " + dt.tarixZaman());
  res.end();
}).listen(8080);
```

<ins>*Qeyd:*</ins> modulu qovluq daxilində tapmaq üçün "./" istifadə olunur. 

Yuxarıdakı kodu "demo_modul.js" faylı kimi saxlayırıq. 

Sonda <b>CMD</b> sətrində <pre>node demo_modul.js</pre> yazıb başladərıq. Əgər hər şey düzgün olunubsa brauzerlə 8080 portuna girilsə tarix və zaman görüləcək. 

***
