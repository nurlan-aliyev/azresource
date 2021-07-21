## Node.js üçün endirilmə qaydası
Rəsmi Node.js vebsəhifəsində Node.js üçün endirilmə qaydaları qeyd olunub: <a href="https://nodejs.org" target="_blank">Endirmək üçün klikləyin</a>

## İlk anlayışlar
Kompüterinizə Node.js endirib qurlaşdırdıqdan sonra veb brauzerdə "Salam Dünya" yazısını çap edək:

"server.js" adlı Node.js faylını yaradıb daxilinə bu kodları yazaq:

```js
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Salam Dünya!');
}).listen(8080, () => console.log("Server qalxdı"));
```

Və bu faylı kompüterinizdə ya iş masasında ya da öz seçdiyiniz fayl daxilində saxlayın.  
Əgər hər hansısa istifadəçi kompüterinizin 8080 portuna qoşulsa kod onlarə salamlayacaq.  
İndilik kodu başa düşməyinizə ehtiyac yoxdur. Kod daha sonra ətraflı izzah ediləcək. 
Amma sadə formada 8080 portunda server yaradılır.

<strong>Əmrlər sətri</strong> (məs. <b>CMD</b> və ya <b>Shell Bash</b>)
Node.js faylları kompüterinzin əmrlər sətri proqramı vasitəsilə başladılmalıdır.  
Həmin bu programı açmaq isə əməliyyat sistemindən asılı olaraq dəyişir. 
- Windows istifadəçiıəri üçün "Start" düyməsi sıxılır və <b>"CMD"</b> proqramı çağırılır.
- Linux istifadəçiıəri üçün CTRL+ALT+T kombninasiyasından istifadə edilə bilər

"server.js" faylının yerləşdiyi fayla naviqasiya etdikdən sonra yaratdığımız faylı başlatmaq üçün aşağıdakı sətr yazılır: 

```shell
node server.js
``` 

Əmrlər sətrində "Server qalxdı!" yazsını gördükdən sonra brauzerdən <a href="http://localhost:8080" target="_blank">http://localhost:8080</a> ünvanına daxil olaraq "Salam Dünya!" yazısını görə bilərsiniz.
