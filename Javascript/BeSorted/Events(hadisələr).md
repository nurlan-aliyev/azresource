
## Node.js mühitində hadisələr (events)

Kompüterdə yerinə yetieilən hər bir dəyişikliyə hadisə kimi baxmaq mümkündür (məs. serverə qoşulmaq, faylı açmaq və s.)


Node.js mühitində *obyektlər* (objects) hadisələri tətikləyə bilər, nümunə kimi **readStream** obyektinin faylları açıb bağlaması göstərilə bilər. 


### Nümunə

```js
var  fs = require('fs');  
var  rs = fs.createReadStream('./demofile.txt');  
rs.on('open',  function  () {  
console.log('Fayl açıldı');  
});
```

## Events modulu

Node.js mühitində, hadisəıəri yaratmaq, tətikləmək və yaxud dinləmək üçün istifadə edilən "Events" modulu mövcuddur. 

Əvvəlcədən yaradılmış Events (ivents) modulunu daxil etmək üçün `require()` metodundan istifadə edilir. Əlavə olaraq bütün xüsusiyyətlər və metodlar *EventEmitter* obyektinin altqrupuna daxildir. Həmin xüsusiyyətlərdən istifadə etmək üçün EventEmitter obyektini yaratmaq lazım gəlir:


```js
var  events = require('events');  
var  eventEmitter =  new  events.EventEmitter();
```

## EventEmitter obyekti  

Aşağıdakı nümunədə hadisə tətiklənən zaman "salam" funksiyası icra olunacaq:

Hər hansısa hadisəni tətikləmək üçün `emit()` metodundan istifadə edilir. 


### Nümunə

```js
var  events = require('events');  
var  eventEmitter =  new  events.EventEmitter();  
  
//hadisəyə nəzər salmaq üçün
var  myEventHandler =  function  () {  
console.log('Salam, dəyərli proqramçı!');  
}  
  
//'salam' hadisəsinin yaradılması
eventEmitter.on('salam', myEventHandler);  
  
//'salam' hadisəsinin tətiklənməsi  
eventEmitter.emit('salam');
```
***