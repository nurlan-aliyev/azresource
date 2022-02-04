[comment]: <> ( @TODO linkləri yoxlamaq lazımdır bitirdikdən sonra.)

> linklər tam düz işləmir, bu fayl ilə işləri bitirəndə linkləri bir daha yoxlayacağıq

# Mündəricat

- [X] [Instalyasiya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya) [EN](https://laravel.com/docs/8.x/installation)
- [ ] [Ayarlama](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#ayarlama---configuration) [EN](https://laravel.com/docs/8.x/configuration)
- [ ] [Direktiv strukturası](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#direktiv-strukturu) [EN](https://laravel.com/docs/8.x/structure)
- [ ] [Başlanğıc dəstləri](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#ba%C5%9Flan%C4%9F%C4%B1c-d%C9%99stl%C9%99ri) [EN](https://laravel.com/docs/8.x/starter-kits)
- [ ] [Yerləşdirmə](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#Yerləşdirmə) [EN](https://laravel.com/docs/8.x/deployment)

# İnstalyasiya

- [X] [Meet Laravel - Laraveli Qarşıla](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#laraveli-qar%C5%9F%C4%B1la)
  - [X] [Why Laravel? - Niyə Laravel?](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#niy%C9%99-laravel)
- [X] [Your First Laravel Project - İlk Laravel Proyektin](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87lk-laravel-proyektin)
  - [X] [Getting Started On macOS - MacOS sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#macos-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [X] [Getting Started On Windows - Windows sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#windows-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [X] [Getting Started On Linux - Linux sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#linux-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [X] [Choosing Your Sail Services - Öz Sail servislərini seçmək]()
  - [X] [Installation Via Composer - Composer ilə quraşdırma]()
- [X] [Initial Configuration]()
  - [X] [Environment Based Configuration]()
  - [X] [Directory Configuration]()
- [X] [Next Steps]()
  - [X] [Laravel The Full Stack Framework]()
  - [X] [Laravel The API Backend]()

## Laraveli Qarşıla

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Laravel ifadəli, zərif sintaksisli veb üzərində işləyən tədbiqin çərçivəsidir. Çərçivə tətbiqin başlanğıc strukturasını
və başlanğıc nöqtəsini verir ki, siz maraqlı nəsə yaratmağa fokuslanasınız.

Laravel hərtərəfli asılılıq inyeksiyası, ifadəli (expressive) verilənlər bazası abstraksiya təbəqəsi, növbələr və
planlaşdırılmış işlər, vahid və inteqrasiya sınağı və s. kimi güclü xüsusiyyətləri təmin etməklə, heyrətamiz inkişaf
etdirici təcrübə təqdim edir.

Fərqi yoxdur siz PHPnın çərçivələrindən yeni istifadə etməyə başlamısınız vəya illərin təcrübəsi var, Laravel sizinlə
böyüyə biləcək bir çərçivədir. Biz sizə ilk addımlarını atmağa və veb developer kimi inkişaf etməyə kömək edəcəyik.
Düzəldəcəyiniz tədbiqləri səbirsizliklə gözləyirik.

## Niyə Laravel?

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Veb tətbiqini qurarkən siz mövcud müxtəlif alətlər və çərçivələr istifadə edə bilərsiniz. Lakin, biz inanırıq ki,
Laravel müasir, tam funksionallı veb tətbiqlər yaratmaq üçün ən yaxşı seçimdir.

### Proqressiv Çərçivə

Biz Laravel'i "proqressiv" çərçivə adlandırmağı xoşlayırıq. Bununla Laravelin sizinlə birlikdə böyüdüyünü nəzərdə
tuturuq. Əgər veb proqramlaşdırmada ilk addımlarınızı atırsınızsa, Laravel-in dokumentasiyası, bələdçiləri
və [video dərsləri](https://youtube.com/playlist?list=PLNsaNn9HVbgutA_O9o57z9Oodwx9Pmha8) sizə həddən artıq yüklənmədən
əsasları öyrənməyə kömək edəcək.

Əgər siz yüksək səviyyəli tərtibatçısınızsa, Laravel sizə asılılıq inyeksiyası, unit sınağı, növbələr, real vaxt
hadisələri və s. üçün möhkəm alətlər təqdim edir. Laravel peşəkar veb proqramlar yaratmaq üçün mükəmməl şəkildə
tənzimlənib və müəssisənin iş yüklərini idarə etməyə hazırdır.

### Genişləndirilən Çərçivə

Laravel inanılmaz dərəcədə genişləndirilə bilər. PHPnın miqyasa uyğunluğu və Redis kimi sürətli, paylanmış keş
sistemləri üçün Laravelin dəstəyi sayəsində üfüqi genişlənmə Laravel üçün çox rahatdır. Əslində, Laravel tətbiqləri ayda
yüz milyonlarla sorğunu idarə etmək üçün asanlıqla miqyaslanıb.

Həddindən artıq miqyas lazımdır? Laravel Vapor kimi platformalar sizə Laravel tətbiqinizi AWS-in ən son serversiz
texnologiyasında demək olar ki, sonsuz miqyasda işlətməyə imkan verir.

### İcma Çərçivəsi

Laravel PHP ekosistemindəki ən yaxşı paketləri birləşdirir və mövcud olan ən möhkəm və tərtibatçılara uyğun çərçivə
təklif edir. Bundan əlavə, dünyanın hər yerindən minlərlə istedadlı tərtibatçı bu çərçivəyə öz töhfəsini verdi. Kim
bilir, bəlkə siz hətta Laravel əməkdaşı (töhfə verən) olacaqsınız.

### İlk Laravel Proyektin

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Biz istəyirik ki, Laravel ilə işə başlamaq mümkün qədər asan olsun. Laravel layihəsini öz kompüterinizdə hazırlamaq və
həyata keçirmək üçün müxtəlif variantlar var. Müxtəlif variantları yoxlamaq və bilmək istəsəniz belə, Laravel sizə Sail
təklif edir. Sail [Docker](https://www.docker.com/) -ə əlavə olunan Laravel proyektini işlətmək üçün lazım olan həlldir.

Docker şəxsi kompüterinizin quraşdırılmış proqram təminatına və ya konfiqurasiyasına mane olmayan kiçik, yüngülçəkili "
qablarda" tətbiqlər və xidmətlərin idarə edilməsi üçün bir vasitədir. Bu o deməkdir ki, şəxsi kompüterinizdə veb
serverlər və verilənlər bazası kimi mürəkkəb inkişaf alətlərini konfiqurasiya etmək və ya quraşdırmaqdan narahat olmaq
lazım deyil. Başlamaq üçün yalnız [Docker Desktop](https://www.docker.com/products/docker-desktop) quraşdırmalısınız.

Laravel Sail Laravelin Dockerdə olan susmaya görə ayarlarına uyğun gələn yüngül əmr-xətt (command-line) görünüşdür (
interface). Sail sizə Docker təcrübəniz olmadan PHP, MySQL və Redis ilə Laravel tətbiqini yığmağa başlanğıc nöqtəsini
verir.

> Docker mütəxəssisən? Narahat olma! Sail ayarlana bilir istəyinizə uyğun. Sadəcə Laravelə daxil olan `docker-compose.yml` faylına nəzər yetirin.

### MacOS sistemində başlamaq üçün

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Əgər Mac istifadə edirsinizsə və Docker Desktop artıq quraşdırılıbsa, sadə terminal əmri istifadə edərək, yeni Laravel
proyekti yarada bilərsiz. Misal üçün, "example-app" direktivində yeni Laravel tətbiqini yaratmaq üçün, növbəti əmrdən
istifadə etmək lazımdır:

`curl -s "https://laravel.build/example-app" | bash`

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür
adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır.

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin
narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək.

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə
brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz

### Windows sistemində başlamaq üçün

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Windows maşınınızda yeni Laravel proqramı yaratmazdan əvvəl Docker Desktop quraşdırdığınızdan əmin olun. Sonra, Linux
2 (WSL2) üçün Windows Subsystem for Linux 2 (WSL2) quraşdırıldığını və aktiv olduğundan əmin olmalısınız. WSL sizə
Windows 10-da Linux ikili icra sənədlərini yerli olaraq işə salmağa imkan verir. WSL2-nin quraşdırılması və
aktivləşdirilməsi haqqında
məlumatı [Microsoft-un tərtibatçı mühiti sənədlərində](https://docs.microsoft.com/en-us/windows/wsl/install) tapa
bilərsiniz.

> WSL2-ni quraşdırdıqdan və işə saldıqdan sonra [Docker Desktop-un WSL2 backendindən](https://docs.docker.com/desktop/windows/wsl/) istifadə etmək üçün ayarlandığından əmin olmalısınız.

Sonra, ilk Laravel layihənizi yaratmağa
hazırsınız. [Windows Terminalını](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab)
işə salın və WSL2 Linux əməliyyat sisteminiz üçün yeni terminal sessiyasına başlayın. Sonra, yeni Laravel layihəsi
yaratmaq üçün sadə terminal əmrindən istifadə edə bilərsiniz. Məsələn, "example-app" adlı qovluqda yeni Laravel proqramı
yaratmaq üçün terminalınızda aşağıdakı əmri işlədə bilərsiniz:

```
curl -s https://laravel.build/example-app | bash
```

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür
adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır.

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin
narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək.

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə
brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz

**WSL2 vasitəsi ilə tətbiqetmə**

Əlbəttə ki, siz WSL2 quraşdırmanızda yaradılmış Laravel proqram fayllarını dəyişdirə bilməlisiniz. Bunu həyata keçirmək
üçün [Microsoft-un Visual Studio Code](https://code.visualstudio.com/) redaktorundan və
onların [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
üçün birinci tərəf genişləndirməsindən istifadə etməyi tövsiyə edirik.

> Visual Studio Code [quraşdırma qaydası](https://youtu.be/-jMBdw1WtSs) Azərbaycan dilində

Bu alətlər quraşdırıldıqdan sonra istənilən Laravel layihəsini Windows Terminalından istifadə edərək proqramınızın kök
kataloqundan `code .` əmrini icra etməklə aça bilərsiniz.

### Linux sistemində başlamaq üçün

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Əgər Linux sistemindən istifadə edirsinizsə və Docker Desktop artıq quraşdırılıbsa, sadə terminal əmri istifadə edərək,
yeni Laravel proyekti yarada bilərsiz. Misal üçün, "example-app" direktivində yeni Laravel tətbiqini yaratmaq üçün,
növbəti əmrdən istifadə etmək lazımdır:

`curl -s "https://laravel.build/example-app" | bash`

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür
adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır.

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin
narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək.

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə
brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz

### Öz Sail servislərini seçmək

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Sail vasitəsilə yeni Laravel proqramı yaradarkən, siz yeni tətbiqinizin docker-compose.yml faylında hansı xidmətlərin
konfiqurasiya edilməsini seçmək üçün ``with`` sorğusundan istifadə edə bilərsiniz. Mövcud xidmətlərə mysql, pgsql,
mariadb, redis, memcached, meilisearch, minio, selenium və mailhog daxildir:

```
curl -s "https://laravel.build/example-app?with=mysql,redis" | bash
```

Əgər xidmətləri özünüz təyin etməsəniz, susmaya görə növbəti xidmətlər olacaq: mysql, redis, meilisearch, mailhog və
selenium

### Composer ilə quraşdırma

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Əgər kompüterinizdə artıq PHP və Composer quraşdırılıbsa, siz birbaşa Composer-dən istifadə etməklə yeni Laravel
layihəsi yarada bilərsiniz. Tətbiq yaradıldıqdan sonra siz Artisan CLI-nin xidmət əmrindən istifadə edərək Laravel-in
yerli serverini işə sala bilərsiniz:

```
composer create-project laravel/laravel example-app

cd example-app

php artisan serve
```

### Laravel quraşdırma (Installer)

Laraveli quraşdırmaq üçün Composer ilə xüsusi paket quraşdırıb, sonra onun vasitəsi ilə də quraşdıra bilərsiz:

```
composer global require laravel/installer

laravel new example-app

cd example-app

php artisan serve
```

Kompozerin (Composer) bin direktivini ``$PATH`` dəyişkəninə əlavə edin ki, laravel (əmri) sizin sistemə yerləşdirilsin.
Direktiv Əməliyyat sistemindən asılı olaraq fərqli lokasiyalar da olur:

- macOS: ```$HOME/.composer/vendor/bin```
- Windows: ```%USERPROFILE%\AppData\Roaming\Composer\vendor\bin```
- GNU / Linux Distributions: ```$HOME/.config/composer/vendor/bin or $HOME/.composer/vendor/bin```

Proyektin git repositoriya olaraq yaradılmasını istəyirsinizsə " ```--git``` " əlavə edin:

```laravel new example-app --git```

Qeyd olunan əmr preoyekti və git reporitoriyanı yaratmaqla, ilk commiti də avtomatik Laravelin ilkin strukturunu edir.
Git bayrağının qoyulması nəzərdə tutur ki, siz Git sistemini kompüterinizə quraşdırmısınız və
ayarlamısız. ```--branch``` bayrağını da ilkin budağın adını qeyd etmək üçün əlavə edə bilərsiniz.

```laravel new example-app --git --branch="main"```

```--git``` bayrağından istifadə etmək əvəzinə, siz Git repozitoriyası yaratmaq üçün ```--github``` bayrağından da
istifadə edə və həmçinin GitHub-da müvafiq şəxsi repozitoriya yarada bilərsiniz:

```laravel new example-app --github```

Yaradılan repositoriya ``https://github.com/<your-account>/example-app`` linkdə əlçatan olacaq. ``--github`` bayrağını
əlavə etməyiniz nəzərdə tutur ki, siz [GitHub CLI](https://cli.github.com/) düzgün quraşdırıb, ayarlamısınız. Əlbəttə
git də düzgün quraşdırılmış və ayarlanmış olmalıdır. Ehtiyac olarsa GitHub CLI dəstəylədiyi digər bayraqları da əlavə
edə bilərsiniz:

``laravel new example-app --github="--public"``

``--organization`` bayrağından istifadə edərək repositoriyanızı müəyyən orqanizasiya altında yarada bilərsiz

`` laravel new example-app --github="--public" --organization="laravel" ``

## Ilkin ayarlar

Laravel çərçivəsində bütün ayar faylları ``config`` direktivində yerləşir. Bütün ayarlama varianları ayrı fayllardır,
ona görə rahat hamısı ilə tanış ola bilərsiniz.

Demək olar Laravelə əlavə ayar lazım deyil. Siz rahat kodlaşdırmağa başlaya bilərsiniz. Hərhalda sizə ``config/app.php``
faylı daha maraqlı olar. Onun daxilində siz vaxt (timezone) və geolokasiya ayarlarını tətbiqiniz üçün dəyişə bilərsiniz.

### Mühit ayarları

Nəzərə alsaq ki Laravelin ayarlanması istifadə olunacaq mühitdən asılıdır, tətbiqiniz şəxsi kompüterinizdə və ya
istehsal (production) serverdə işlədəcəksiniz, sizə mütləq lazım olacaq ayarları proyektinizin kökündə yerləşən ``.env``
faylında tapa bilərsiniz.

Sizin ``.env`` faylınız versiyanın idarə sisteminə commit olunmalı deyil, çünki hər tərtibatçı (server) öz ayarlarını
qeyd edəcək mühitdən asılı olaraq. Əlavə olaraq nəzərə alın ki, təhlükəsizlik baxımından da commit etmək olmaz. ``.env``
faylında sizin gizli saxlanılası məlumatlarınız olacaq.

> ``.env`` faylı haqqında daha çox və ətraflı oxumaq istəyirsinizsə [Ingilis dilində](https://laravel.com/docs/8.x/configuration#environment-configuration) [Azərbaycan dilində](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#m%C3%BChitin-ayarlanmas%C4%B1--point_up_2-) oxuya bilərsiniz.

### Direktiv ayarları

Laravel həmişə veb serveriniz üçün konfiqurasiya edilmiş "veb kataloqunun" kökündən xidmət göstərməlidir. Siz "veb
kataloqunun" alt kataloqundan Laravel proqramına xidmət göstərməyə çalışmamalısınız. Bunu etməyə cəhd tətbiqinizdə
mövcud olan həssas faylları ifşa edə bilər.

### Növbəti addımlar

Proyektinizi yaratdıqdan sonra, onun üzərində necə işləməli və ümumiyyətlə növbəti addımlar necə olmalıdır sualı yarana
bilər. İlk öncə növbəti mövzuları diqqətlə oxumağı və Laravelin necə işlədiyini başa düşməyi tövsiyə edirik:

- :
  clipboard: [Sorğunun Yaşam Dövrü](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Arxitektura%20Konsepti.md#sor%C4%9Funun-ya%C5%9Fam-d%C3%B6vr%C3%BC)
  - [Request Lifecycle](https://laravel.com/docs/8.x/lifecycle)
- :
  clipboard: [Ayarlama](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#ayarlama---configuration--point_up_2-)
  - [Configuration](https://laravel.com/docs/8.x/configuration)
- :
  clipboard: [Direktiv Strukturu](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#direktiv-strukturu--point_up_2-)
  - [Directory Structure](https://laravel.com/docs/8.x/structure)
- :
  clipboard: [Xidmət konteyneri](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Arxitektura%20Konsepti.md#xidm%C9%99t-konteyneri)
  - [Service Container](https://laravel.com/docs/8.x/container)
- :
  clipboard: [Facades](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Arxitektura%20Konsepti.md#fasadlar)
  - [Facades](https://laravel.com/docs/8.x/facades)

Laraveli necə istifadə edəcəyinizdən asılı olaraq sizin növbəti addımlarınız dəyişə bilər. Biz iki əsas istifadə növünə
vurğulanacağıq.

### Laravel The Full Stack Framework

Laravel Full Stack çərçivə kimi fəaliyət göstərə bilər. Full Stack dedikdə "Back End"dən əlavə "Front End" üçün Blade və
ya İnertia.js istifadə edə bilməyinizi nəzərdə tuturuq. Full Stack Laravel çərçivəsinin ən çox istifadə edilmə
yollarından biridir.

Əgər siz Full Stack olaraq istifadəni planlaşdırırsınızsa, o zaman sizə dokumentasiyadan növbəti mövzuları nəzərdən
keçirməyi tövsiyyə edərdim: ``routing, views`` və ya ``the Eloquent ORM``

Əlavə olaraq CSS və Javascript kodlarını Laravel Mix ilə kompilyasiyanı bilmək
üçün [Laravel Mix](https://laravel.com/docs/8.x/mix) [Laravel Mix Az]() haqqında oxumağı da məsləhət görürük.

> Bir başa tətbiqinizi qurmağa başlamaq istəyirsinizsə [application starter kits]() [Başlanğıc dəstlərinə]()

### Laravel The API Backend

Laravel həmçinin API xidməti kimi, JavaScript bir-səhifəlik tətbiqlər üçün və ya mobil tətbiqlər üçün də istifadə oluna
bilər. Məsələn Laraveli [Next.js](https://nextjs.org/) tətbiqinin bəkendini qurmağa istifadə edə bilərsiniz. Bu halda
Laraveli [autentifikasiya]() - ([Ingilis dilində](https://laravel.com/docs/8.x/sanctum)) və məlumatın saxlanılması və
fronta geri qaytarması üçün, eyni zamanda Laravelin növbələr, e-poçtlar, bildirişlər və s. kimi xidmətlərindən istifadə
oluna bilər.

Əgər siz Laraveli API bekend kimi istifadə etmək istəyirsinizsə o zaman dokumentasiyamızdan növbəti mövzuları məsləhət
görə bilərik [marşrutlaşdırma](), [Laravel Sanctum]() və [Eloquent ORM]()
.  [routing](https://laravel.com/docs/8.x/routing), [Laravel Sanctum](https://laravel.com/docs/8.x/sanctum)
və [Eloquent ORM](https://laravel.com/docs/8.x/eloquent).

> Laraveli bekend və Next.js frontend kimi istifadə edərək tətbiqinizə başlamaq istəyirsiz? Sizə Laravel Breeze təklif edirik, [API stek](https://laravel.com/docs/8.x/starter-kits#breeze-and-next) və [Next.js frontendin implementasiyası](https://github.com/laravel/breeze-next) ilə bir neçə dəqiqəyə başlaya bilərsiniz.

# Ayarlama - Configuration

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

- [ ] [Giriş]() [Introduction](https://laravel.com/docs/8.x/configuration#introduction)
- [ ] [Mühit Ayarları]() [Environment Configuration](https://laravel.com/docs/8.x/configuration#environment-configuration)
- [ ] [Mühit dəyişkənlərinin ayarları]() [Environment Variable Types](https://laravel.com/docs/8.x/configuration#environment-variable-types)
- [ ] [Mühit dəyişkənlərinin istifadəsi]() [Retrieving Environment Configuration](https://laravel.com/docs/8.x/configuration#retrieving-environment-configuration)
- [ ] [Mövcud mühitin müəyyən edilməsi]() [Determining The Current Environment](https://laravel.com/docs/8.x/configuration#determining-the-current-environment)
- [ ] [Ayar dəyərlərinə daxil olmaq]() [Accessing Configuration Values](https://laravel.com/docs/8.x/configuration#accessing-configuration-values)
- [ ] [Ayarların keşlənməsi]() [Configuration Caching](https://laravel.com/docs/8.x/configuration#configuration-caching)
- [ ] [Sazlama rejimi]() [Debug Mode](https://laravel.com/docs/8.x/configuration#debug-mode)
- [ ] [Baxım rejimi]() [Maintenance Mode](https://laravel.com/docs/8.x/configuration#maintenance-mode)

## Giriş

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Laravel üçün bütün ayar faylları ``config`` direktivində saxlanılır. Bütün ayarlama varianları ayrı fayllardır, ona görə
rahat hamısı ilə tanış ola bilərsiniz.

Bu ayar faylları ilə siz verilənlər bazası ilə əlaqə üçün, mail server üçün və digər tarix vaxt ayalarını, enkript
ayarlarını quraşdıra bilərsiniz.

## Mühitin ayarlanması

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Mühitə görə ayarların dəyərləri dəyişə bilər, fərqli ayar dəyərlərinin olması adətən yaxşı olur. Məsələn öz
kompüterinizdə və istehsal (production) serverində fərqli keş ayarları istifadə etmiş ola bilərsiniz.

Bunu asanlaşdırmaq üçün Laravel [DotEnv](https://github.com/vlucas/phpdotenv) PHP kitabxanasından istifadə edir.
Laraveli quraşdırdıqdan sonra onun direktivinin kökündə ``.env.example`` faylı olacaq, həmin faylda əsas mühit ayarları
yerləşdirilib. Laraveli quraşdıran zaman həmin fayl avtomatik ``.env`` faylı kimi kopyalanacaq.

Laravel'in susmaya görə ``.env`` faylı tətbiqinizin yerli və ya istehsal (production) veb serverində işləməsinə görə
fərqlənə bilən bəzi ümumi ayarlar dəyərlərini ehtiva edir. Həmin ayarlar sonradan müxtəlif ayar fayllarından, ``config``
direktivində olan, env funksiyası vasitəsi ilə çağırılır və istifadə olunur.

Əgər siz komandanızla tətbiq hazırlayırsınızsa, o zaman ``.env.example`` faylına mühit ayarlarınızı əlavə edə bilərsiniz
ki, komanda yoldaşlarınız sizin tədbiqdə hansı ayarlar istifadə olunmalı olduğunu bilsinlər.

> .env faylında olan mühit dəyişkənlərinin qiyməti server və ya sistem səviyyəsində olan mühit dəyişkəni tərəfindən dəyişdirilə bilər.

## Mühitin Fayl TƏhlükəsizliyi

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Sizin ```.env``` faylınız versiyanın idarə edilmə sisteminə əlavə olunmalı deyil, çünki hər tətbiqi istifadə edən
tərtibatçı/server öz mühit ayarlanmasını tələb edə bilər. Əlavə olaraq təhlükəsizlik baxımından düzgün addım sayılmır.

## Əlavə mühit faylları

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Tətbiqinizin mühit dəyişənlərini yükləməzdən əvvəl Laravel ya ``APP_ENV`` mühit dəyişəninin xaricdən təmin
edilib-edilmədiyini və ya ``--env`` CLI arqumentinin təyin edilib-edilmədiyini müəyyən edir. Əgər belədirsə, əgər varsa,
Laravel ```.env.[APP_ENV]``` faylını yükləməyə çalışacaq. Əgər o, mövcud deyilsə, standart .env faylı yüklənəcək.

## Mühitin Dəyişənlərinin Növləri

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

``.env`` fayllarınızdakı bütün dəyişənlər adətən sətirlər (Strings) kimi təhlil edilir, buna görə də ``env()``
funksiyasından daha geniş çeşidləri qaytarmağa imkan vermək üçün bəzi ehtiyat dəyərlər yaradılmışdır:

![Laravel env növləri](https://github.com/aytiqaqash/azresource/tree/main/assets/Laravel/Dokumentasiya/8.x/Laravel_env_types.jpg)

Əgər siz boşluqları daxilində boşluq olan dəyərlə mühit dəyişənini təyin etməlisinizsə, bunu dəyəri qoşa dırnaq işarəsi
ilə daxil etməklə edə bilərsiniz:

> ``APP_NAME``="Mənim tətbiqim"

## Mühit dəyişənlərinin istifadəsi

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Tətbiqiniz sorğu qəbul etdikdə bu faylda sadalanan bütün dəyişənlər $_ENV PHP super-global-a yüklənəcək. Bununla belə,
siz ayar fayllarınızdakı bu dəyişənlərdən dəyərləri əldə etmək üçün ``env`` köməkçisindən istifadə edə bilərsiniz.
Əslində, Laravel ayar fayllarını nəzərdən keçirsəniz, bir çox variantın artıq bu köməkçidən istifadə etdiyini
görəcəksiniz:

> ```'debug' => env('APP_DEBUG', false),```

``env`` funksiyasına ötürülən ikinci dəyər susmaya görə olan dəyərdir. Verilmiş açar üçün heç bir mühit dəyişəni
yoxdursa, bu dəyər qaytarılacaq.

## Mövcud mühitin müəyyən edilməsi

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Cari tətbiq mühiti ``.env`` faylınızdan ``APP_ENV`` dəyişəni ilə müəyyən edilir. Siz bu dəyərə ``mühit``
metodu ``App facade`` ilə daxil ola bilərsiniz:
>

```injectablephp
 use Illuminate\Support\Facades\App;
 
 $environment = App::environment();
```

Siz həmçinin mühitin verilmiş dəyərə uyğun olub-olmadığını müəyyən etmək üçün arqumentləri mühit metoduna ötürə
bilərsiniz. Mühit verilmiş dəyərlərdən hər hansı birinə uyğun gələrsə, metod doğru qaytaracaq:

```injectablephp
if (App::environment('local')) {
    // The environment is local
}

if (App::environment(['local', 'staging'])) {
    // The environment is either local OR staging...
}
```

> Cari tətbiq mühitinin aşkarlanması server səviyyəli APP_ENV mühit dəyişənini təyin etməklə ləğv edilə bilər.

## Ayar dəyərlərinə daxil olmaq

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Direktiv strukturu

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Başlanğıc dəstləri

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Yerləşdirmə

[ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)
