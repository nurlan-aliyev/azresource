# JavaScript (JS)

## Niyə JS?

JS, web səhifələrin interaktiv olmasına imkan verən həm müştəri, həm də server tərəfində istifadə olunan mətn əsaslı bir proqramlaşdırma dilidir. HTML və CSS veb səhifələrə struktur və üslub verən dillər olduqda, JavaScript veb səhifələrə bir istifadəçini cəlb edən interaktiv elementlər verir. Hər gün istifadə edə biləcəyiniz ümumi JavaScript nümunələrinə Amazondakı axtarış qutusu, New York Times qəzetinə yerləşdirilmiş bir xəbər özetləmə videosu.

## Plan

- JS nədir?
  - [Giriş](Core/Giris.md)
  - [İlk anlayışlar](Core/IlkAnlayislar.md)
- Browser JavaScript
  - [Giriş](Browser/Giris.md)
- NodeJS
  - [Giriş](Node/Giris.md)


<!--
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


## Node.js Fayl serveri kimi 
Node.js fayl sistemi modulu kompüter daxilindəki fayllarla işləməyə imkan yaradır.

Fayl Sistem modulunu əlavə etmək üçün  `require()`  metodundan istifadə olunur:

```js
var  fs = require('fs');
```

Fayl Sistemi modulunun ən çox istifadə olunma məqsədləri:

- Faylların oxunulması
- Faylların yaradılması
- Faylların yenilənməsi
- Faylların silinməsi
- Faylların adlarının dəyişdirilməsi


## Faylların oxunulması

Bunun üçün `fs.readFile()` metodundan istifadə olunur. 

Fərz edək ki, Node.js faylı ilə bir qovluqda yerləşən HTML faylı var:
`demofayl1.html`

```html
<html>  
<body>  
<h1>Başlıq</h1>  
<p>Paraqraf.</p>  
</body>  
</html>
```

Bu HTML faylını oxuyub daxilindəki məzmunu istifadəçiyə qaytarmaq üçün Node.js faylı aşağıdakı koddan ibarətdir: 

Nümunə:

```js
var  http = require('http');  
var  fs = require('fs');  
http.createServer(function  (req, res) {  
fs.readFile('demofayl1.html',  function(err, data) {  
res.writeHead(200, {'Content-Type':  'text/html'});  
res.write(data);  
return  res.end();  
});  
}).listen(8080);
```

Yuxarıdakı kodu "demo_faylOxucu.js" kimi yaddaşda saxlayıb serveri başladaq: 

```bash
C:\Users\_Your Name_>node demo_readfile.js
```

## Faylların yaradılması
Fayl Sistem modulu yeni faylların yaradılması üçün aşağıdakı metodları özündə birləşdirir:

- `fs.appendFile()`
- `fs.open()`
- `fs.writeFile()`

`fs.appendFile()`  metodu mötərizə daxilində verilən məzmunu fayla əlavə edir, əgər fayl mövcud deyilsə belə həmin faylı yaradır. 

### Nümunə

`appendFile()` metodu ilə fayl yaradılması:

```js
var  fs = require('fs');  
  
fs.appendFile('yenifayl1.txt',  'Yazılacaq məzmun bura əlavə olunur',  function  (err) {  
if  (err)  throw  err;  
console.log('Yaddaşda saxlanıldı!');  
});
```

`fs.open()` metodu mötərizə daxilində ikinci arqument qəbul edir və ona uyğun nəticə verir. Əgər ikinci arqument "w" (ingilis dilindən <em>writing</em> sözünün baş hərfidir) kimi qeyd olunarsa açılacaq fayl daxilinə məlumat yazılması üçün istifadə olunacaq. Əgər bu fayl mövcud deyilsə boş fayl yaradılacaq: 

### Nümunə:

```js
var  fs = require('fs');  
  
fs.open('yenifayl2.txt',  'w',  function  (err,  file) {  
if  (err)  throw  err;  
console.log('Yaddaşda saxlanıldı!');  
});
```

`fs.writeFile()` metodu, mötərizə daxilində qeyd olunan fayl mövcuddursa onun məzmununu dəyişir. Əgər fayl mövcud deyilsə verilmiş məzmundan ibarət olunan fayl yaradılacaq: 

### Nümunə

```js
var  fs = require('fs');  
  
fs.writeFile('yenifayl3.txt',  'Qeyd olunacaq məzmun',  function  (err) {  
if  (err)  throw  err;  
console.log('Yaddaşda saxlanıldı!');  
});
```

## Faylların yenilənməsi
Fayl Sistemi modulu faylların yenilənməsi üçün aşağıdakı metodaları təqdim edir:

- `fs.appendFile()`
- `fs.writeFile()`

`fs.appendFile()` metodu verilmiş məzmunu faylın sonuna əlavə edir:

### Nümunə

"Faylın sonuna əlavə olunacaq məzmun." oxuduğunuz formada "yenifayl1.txt" faylının sonuna əlavə olunacaq:

```js
var  fs = require('fs');  
  
fs.appendFile('yenifayl1.txt',  'Faylın sonuna əlavə olunacaq məzmun.',  function  (err) {  
if  (err)  throw  err;  
console.log('Yeniləndi!');  
});
```

`fs.writeFile()` qeyd olunmuş faylı və daxilindəki məzmunu dəyişir:

### Nümunə

```js
var  fs = require('fs');  
  
fs.writeFile('yenifayl3.txt',  'Yenilənən məzmun',  function  (err) {  
if  (err)  throw  err;  
console.log('Yeniləndi!');  
});
```

## Faylların silinməsi
Hər hansısa faylı silmək üçün `fs.unlink()` metodundan istifadə olunur. 

### Nümunə

```js
var  fs = require('fs');  
  
fs.unlink('yenifayl2.txt',  function  (err) {  
if  (err)  throw  err;  
console.log('Fayl silindi!');  
});
```

## Faylların adlarının dəyişdirilməsi

Faylların adlarının dəyişdirilməsi üçün `fs.rename()` metodu istifadə olunur.

### Nümunə
"yenifayl1.txt" faylının adının "dəyişdirilmişfayl1.txt":

```js
var  fs = require('fs');  
  
fs.rename('yenifayl1.txt',  'dəyişdirilmişfayl1.txt',  function  (err) {  
if  (err)  throw  err;  
console.log('Faylın adı dəyişdirildi!');  
});
```
***
## URL modulu
URL modulu veb ünvanını oxunabilən hissəcikıərə parçalayır. 


URL modulunu əlavə etmək üçün `require()` metodu istifadə olunur:

```js
var  url = require('url');
```

URL ünvanını parçalamaq üçün `url.parse()` metodundan istifadə etmək gərəkdir. Bu method, yeni bir URL obyekti (JS terminidir) qaytarır (return edir):

Nümunə:
Veb ünvanının oxunabilən hissələrə parçalanması: 
```js
var  url = require('url');  
var  adr =  'http://localhost:8080/default.htm?year=2017&month=february';  
var  q = url.parse(adr,  true);  
  
console.log(q.host);  //'localhost:8080' qaytarır  
console.log(q.pathname);  // '/default.htm' qaytarır 
console.log(q.search);  //'?year=2017&month=february' qaytarır
  
var  qdata = q.query;  //bu obyekti qaytarır: { year: 2017, month: 'february' }  
console.log(qdata.month);  //'february' qaytarır
```

## Node.js Fayl serveri
Veb ünvanını hissələrə bölməyi öyrəndikdən sonra artıq fayl sistemi ilə birlikdə istifadə edə bilərik. 

İki ayrı HTML faylı yaradıb Node.js faylı yerləşən qovluq daxilində yaddaşda saxlayırıq. 

`yay.html`

```html
<!DOCTYPE html>  
<html>  
<body>  
<h1>Yay</h1>  
<p>Yay çox gözəldir!</p>  
</body>  
</html>
```
`winter.html`

```html
<!DOCTYPE html>  
<html>  
<body>  
<h1>Qış</h1>  
<p>Qarlı havanı sevirəm!</p>  
</body>  
</html>
```

İndi isə bu fayllardan istənilən birinin istifadəçiyə verilməsi üçün Node.js serveri yaradaq: 

`demo_faylserveri.js:`

```js
var  http = require('http');  
var  url = require('url');  
var  fs = require('fs');  
  
http.createServer(function  (req, res) {  
var  q = url.parse(req.url,  true);  
var  filename =  "."  + q.pathname;  
fs.readFile(filename,  function(err, data) {  
if  (err) {  
res.writeHead(404, {'Content-Type':  'text/html'});  
return  res.end("404 Məzmun tapılmadı");  
}  
res.writeHead(200, {'Content-Type':  'text/html'});  
res.write(data);  
return  res.end();  
});  
}).listen(8080);
```
Serveri başlatmaq üçün aşağıdakı sətri yazırıq: 

```shell
C:\Users\_Your Name_>node demo_fileserver.js
```
***
-->