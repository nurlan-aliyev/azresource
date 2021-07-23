
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
