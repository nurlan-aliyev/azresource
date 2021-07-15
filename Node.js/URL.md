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
return  res.end("404 Not Found");  
}  
res.writeHead(200, {'Content-Type':  'text/html'});  
res.write(data);  
return  res.end();  
});  
}).listen(8080);
```
Serveri başlatmaq üçün aşağıdakı sətri yazırıq: 

```bash
C:\Users\_Your Name_>node demo_fileserver.js
```
