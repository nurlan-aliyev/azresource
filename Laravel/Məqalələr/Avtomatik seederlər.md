# Laraveldə avtomatik seed faylların yaradılması.

orangehill/iseed

Bu gün yeni paket haqqında öyrəndim. İlk imkan yaranan kimi həmin paketi yoxlamaq qərarına gəldim. Səmimi olsaq həmin paketə ehtiyacım var idi. Böyük ehtimal Voyager istifadə edənlər bu paket haqqında eşidiblər. Mənim isə gözlənilmədən Laravel Daily kanalından qarşıma çıxdı. Paket verilənlər bazasında olan cədvələ əsasən yeni seeder yaradır. Daha ətraflı buradan oxuya bilərsiniz.

Nəyə görə Voyager istifadə edən bu paketə ehtiyac duysun?

Voyager admin panel yaradır. Həmin admin panel köməyi ilə verilənlər bazasında cədvəl yaradıb, həmin cədvələ məlumatları əlavə edib, silmək mümkündür. Developer saytın admin panelini yaxşı qurub sonra kontenti doldurduqdan sonra fikirləşir bunu serverə və ya hostigə yerləşdirim. Elə bunu fikirləşir ki, arada bir çətinlik yaranır: “axı verilənlər bazasında olanları da ora keçirtməliyəm…”. İndi məlumatları verilənlər bazasından export və import edim? Əlbəttə bunu etmək mümkündür. Amma daha rahatı Seederlərdən istifadə etməkdir, əgər onlar tez və rahat yaradıla bilərsə. Əks halda hər cədvəl üçün düzgün Seed faylı yaratmaq da çox vaxt alar. İseed paketindən yüngül istifadə edib test elədim. Vaxt tapdıqda video hazırlayıb [AyTi Qaqaş youtube kanalımızda](https://www.youtube.com/c/AyTiQaqa%C5%9F/videos) paylaşacam. Hələlik bir iki kəlmə ilə yazım.

Tutaq ki sizin verilənlər bazanızda “posts” cədvəli var. Həmin cədvəlin daxilində paylaşımlara aid məlumatlarınız saxlanılır. Siz bu paylaşımları productiona da çıxarmaq istərdiniz. O zaman siz iseed paketinin yaratdığı artisan əmrindən istifadə etməklə avtomatik seeder faylını qurmuş olursuz. Seeder faylı laravelin standarlarına uyğun adlandırılır.

`php artisan iseed posts`

![Avtomatik generasiya olunan kod](https://miro.medium.com/max/875/1*XbItbyFY7O-gyDqVPl5shg.png)


Mənbə: [AytiQaqaş Medium](https://aytiqaqash.medium.com/laraveld%C9%99-avtomatik-seed-fayllar%C4%B1n-yarad%C4%B1lmas%C4%B1-d0d66378efe8)