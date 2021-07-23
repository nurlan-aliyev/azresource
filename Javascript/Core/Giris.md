# Node.js nədir?
- Node.js açıq qaynaqlı JavaScript server mühitidir
- Node.js pulsuz istifadəlidir
- Node.js müxtəlif platformalarda çalışır (Windows, Linux, Unix, Mac OS X, və s.)

# Niyə Node.js?
Node.js asinxron (bir-birindən asılı olmayaraq müxtəlif kod bloklarının icra olunması mənasını verir) proqramlaşdırma məntiqi ilə çalışır.


Fayl mübadiləsini PHP və ya ASP kimi texnologiyalarda aşağıdakı formada icra edilir:

- İcra olunan əməliyyat kompüterin fayl sisteminə göndərilir
- Fayl sisteminin göndərilən faylın açılıb oxunmasını gözləyir
- Alınan məzmunu istifadəçiyə geri qaytarır
- Növbəti sorğu üçün artıq hazır vəziyyətə gəlir

Fayl mübadiləsini Node.js isə aşağıdakı formada həll edir: 

- İcra olunan əməliyyat kompüterin fayl sisteminə göndərilir
- Növbəti sorğu üçün artıq hazır vəziyyətə gəlir
- Fayl sistemi faylı açıb oxuduqdan sonra server artıq məzmunu istifadəçiyə qaytarır
- Node.js gözləməni ləğv edir və növbəyi sorğuya keçir 

Node.js çox hallarda tək prosesli (baxılan əməlliyyat zamanı prosessorun tək axını işlədilir), bloklanmayan, asinxron proaramlaşdırmadan istifadə edir və bu yaddaş cəhətdən çox səmərəlidir. 

# Node.js nəyə qadirdir?
- ASP.net, PHP və digər dillərdə olan bütün funksionallıqlar

# Node.js-in digər dillərdən fərqi nədir?
- Digər dillər hər hansı blok kodu icra etməmiş digərinə keçmir. Asinxronluğa görə isə Node.js bunu bacarır

### Node.js faylı nədir?
- Node.js faylları müxtəlif hadisələr (event) üzərində icra olunacaq əməliyyatları özündə birləşdirir
- Həmin bu hadisələrə nümumə olaraq istifadəçinin serverdəki portlardan birini əldə etməsi göstərilə bilər 
- Node.js faylları hər hansısa effektə sahib olmaları üçün qabaqcadan serverə yerləşdirilməlidir 
- Node.js fayllarının uzantıları ".js", ".mjs", ".cjs" kimi qeyd olunur

<!-- [Next](./IlkAnlayislar.md) -->