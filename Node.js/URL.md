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

## Node.js File Server

Now we know how to parse the query string, and in the previous chapter we learned how to make Node.js behave as a file server. Let us combine the two, and serve the file requested by the client.

Create two html files and save them in the same folder as your node.js files.

summer.html

<!DOCTYPE html>  
<html>  
<body>  
<h1>Summer</h1>  
<p>I love the sun!</p>  
</body>  
</html>

winter.html

<!DOCTYPE html>  
<html>  
<body>  
<h1>Winter</h1>  
<p>I love the snow!</p>  
</body>  
</html>


Create a Node.js file that opens the requested file and returns the content to the client. If anything goes wrong, throw a 404 error:

demo_fileserver.js:
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
Remember to initiate the file:

Initiate demo_fileserver.js:
```bash
C:\Users\_Your Name_>node demo_fileserver.js
```
If you have followed the same steps on your computer, you should see two different results when opening these two addresses:

[http://localhost:8080/summer.html](http://localhost:8080/summer.html)

Will produce this result:

# Summer

I love the sun!

[http://localhost:8080/winter.html](http://localhost:8080/winter.html)

Will produce this result:

# Winter

I love the snow!
