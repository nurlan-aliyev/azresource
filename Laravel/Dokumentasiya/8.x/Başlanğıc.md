# İnstalyasiya

- [X] [Meet Laravel - Laraveli Qarşıla](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#laraveli-qar%C5%9F%C4%B1la)
  - [X] [Why Laravel? - Niyə Laravel?](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#niy%C9%99-laravel)
- [X] [Your First Laravel Project - İlk Laravel Proyektin](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87lk-laravel-proyektin)
  - [X] [Getting Started On macOS - MacOS sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#macos-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [X] [Getting Started On Windows - Windows sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#windows-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [ ] [Getting Started On Linux - Linux sistemində başlamaq üçün](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#linux-sistemind%C9%99-ba%C5%9Flamaq-%C3%BC%C3%A7%C3%BCn)
  - [ ] [Choosing Your Sail Services - Öz Sail servislərini seçmək]()
  - [ ] [Installation Via Composer - Composer ilə quraşdırma]()
- [ ] [Initial Configuration]()
  - [ ] [Environment Based Configuration]()
  - [ ] [Directory Configuration]()
- [ ] [Next Steps]()
  - [ ] [Laravel The Full Stack Framework]()
  - [ ] [Laravel The API Backend]()

## Laraveli Qarşıla [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Laravel ifadəli, zərif sintaksisli veb üzərində işləyən tədbiqin çərçivəsidir. Çərçivə tətbiqin başlanğıc strukturasını və başlanğıc nöqtəsini verir ki, siz maraqlı nəsə yaratmağa fokuslanasınız.

Laravel hərtərəfli asılılıq inyeksiyası, ifadəli (expressive) verilənlər bazası abstraksiya təbəqəsi, növbələr və planlaşdırılmış işlər, vahid və inteqrasiya sınağı və s. kimi güclü xüsusiyyətləri təmin etməklə, heyrətamiz inkişaf etdirici təcrübə təqdim edir.

Fərqi yoxdur siz PHPnın çərçivələrindən yeni istifadə etməyə başlamısınız vəya illərin təcrübəsi var, Laravel sizinlə böyüyə biləcək bir çərçivədir. Biz sizə ilk addımlarını atmağa və veb developer kimi inkişaf etməyə kömək edəcəyik. Düzəldəcəyiniz tədbiqləri səbirsizliklə gözləyirik.

## Niyə Laravel? [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Veb tətbiqini qurarkən siz mövcud müxtəlif alətlər və çərçivələr istifadə edə bilərsiniz. Lakin, biz inanırıq ki, Laravel müasir, tam funksionallı veb tətbiqlər yaratmaq üçün ən yaxşı seçimdir.

### Proqressiv Çərçivə

Biz Laravel'i "proqressiv" çərçivə adlandırmağı xoşlayırıq. Bununla Laravelin sizinlə birlikdə böyüdüyünü nəzərdə tuturuq. Əgər veb proqramlaşdırmada ilk addımlarınızı atırsınızsa, Laravel-in dokumentasiyası, bələdçiləri və [video dərsləri](https://youtube.com/playlist?list=PLNsaNn9HVbgutA_O9o57z9Oodwx9Pmha8) sizə həddən artıq yüklənmədən əsasları öyrənməyə kömək edəcək.

Əgər siz yüksək səviyyəli tərtibatçısınızsa, Laravel sizə asılılıq inyeksiyası, unit sınağı, növbələr, real vaxt hadisələri və s. üçün möhkəm alətlər təqdim edir. Laravel peşəkar veb proqramlar yaratmaq üçün mükəmməl şəkildə tənzimlənib və müəssisənin iş yüklərini idarə etməyə hazırdır.

### Genişləndirilən Çərçivə

Laravel inanılmaz dərəcədə genişləndirilə bilər. PHPnın miqyasa uyğunluğu və Redis kimi sürətli, paylanmış keş sistemləri üçün Laravelin dəstəyi sayəsində üfüqi genişlənmə Laravel üçün çox rahatdır. Əslində, Laravel tətbiqləri ayda yüz milyonlarla sorğunu idarə etmək üçün asanlıqla miqyaslanıb.

Həddindən artıq miqyas lazımdır? Laravel Vapor kimi platformalar sizə Laravel tətbiqinizi AWS-in ən son serversiz texnologiyasında demək olar ki, sonsuz miqyasda işlətməyə imkan verir.

### İcma Çərçivəsi

Laravel PHP ekosistemindəki ən yaxşı paketləri birləşdirir və mövcud olan ən möhkəm və tərtibatçılara uyğun çərçivə təklif edir. Bundan əlavə, dünyanın hər yerindən minlərlə istedadlı tərtibatçı bu çərçivəyə öz töhfəsini verdi. Kim bilir, bəlkə siz hətta Laravel əməkdaşı (töhfə verən) olacaqsınız.

### İlk Laravel Proyektin [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Biz istəyirik ki, Laravel ilə işə başlamaq mümkün qədər asan olsun. Laravel layihəsini öz kompüterinizdə hazırlamaq və həyata keçirmək üçün müxtəlif variantlar var. Müxtəlif variantları yoxlamaq və bilmək istəsəniz belə, Laravel sizə Sail təklif edir. Sail [Docker](https://www.docker.com/) -ə əlavə olunan Laravel proyektini işlətmək üçün lazım olan həlldir.

Docker şəxsi kompüterinizin quraşdırılmış proqram təminatına və ya konfiqurasiyasına mane olmayan kiçik, yüngülçəkili "qablarda" tətbiqlər və xidmətlərin idarə edilməsi üçün bir vasitədir. Bu o deməkdir ki, şəxsi kompüterinizdə veb serverlər və verilənlər bazası kimi mürəkkəb inkişaf alətlərini konfiqurasiya etmək və ya quraşdırmaqdan narahat olmaq lazım deyil. Başlamaq üçün yalnız [Docker Desktop](https://www.docker.com/products/docker-desktop) quraşdırmalısınız.

Laravel Sail Laravelin Dockerdə olan susmaya görə ayarlarına uyğun gələn yüngül əmr-xətt (command-line) görünüşdür (interface). Sail sizə Docker təcrübəniz olmadan PHP, MySQL və Redis ilə Laravel tətbiqini yığmağa başlanğıc nöqtəsini verir.

> Docker mütəxəssisən? Narahat olma! Sail ayarlana bilir istəyinizə uyğun. Sadəcə Laravelə daxil olan `docker-compose.yml` faylına nəzər yetirin. 

### MacOS sistemində başlamaq üçün [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya) 

Əgər Mac istifadə edirsinizsə və Docker Desktop artıq quraşdırılıbsa, sadə terminal əmri istifadə edərək, yeni Laravel proyekti yarada bilərsiz. Misal üçün, "example-app" direktivində yeni Laravel tətbiqini yaratmaq üçün, növbəti əmrdən istifadə etmək lazımdır:

`curl -s "https://laravel.build/example-app" | bash`

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır. 

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək. 

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz

### Windows sistemində başlamaq üçün [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya) 

Windows maşınınızda yeni Laravel proqramı yaratmazdan əvvəl Docker Desktop quraşdırdığınızdan əmin olun. Sonra, Linux 2 (WSL2) üçün Windows Subsystem for Linux 2 (WSL2) quraşdırıldığını və aktiv olduğundan əmin olmalısınız. WSL sizə Windows 10-da Linux ikili icra sənədlərini yerli olaraq işə salmağa imkan verir. WSL2-nin quraşdırılması və aktivləşdirilməsi haqqında məlumatı [Microsoft-un tərtibatçı mühiti sənədlərində](https://docs.microsoft.com/en-us/windows/wsl/install) tapa bilərsiniz.

> WSL2-ni quraşdırdıqdan və işə saldıqdan sonra [Docker Desktop-un WSL2 backendindən](https://docs.docker.com/desktop/windows/wsl/) istifadə etmək üçün ayarlandığından əmin olmalısınız.

Sonra, ilk Laravel layihənizi yaratmağa hazırsınız. [Windows Terminalını](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab) işə salın və WSL2 Linux əməliyyat sisteminiz üçün yeni terminal sessiyasına başlayın. Sonra, yeni Laravel layihəsi yaratmaq üçün sadə terminal əmrindən istifadə edə bilərsiniz. Məsələn, "example-app" adlı qovluqda yeni Laravel proqramı yaratmaq üçün terminalınızda aşağıdakı əmri işlədə bilərsiniz:

```
curl -s https://laravel.build/example-app | bash
```

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır.

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək.

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz

**WSL2 vasitəsi ilə tətbiqetmə**

Əlbəttə ki, siz WSL2 quraşdırmanızda yaradılmış Laravel proqram fayllarını dəyişdirə bilməlisiniz. Bunu həyata keçirmək üçün [Microsoft-un Visual Studio Code](https://code.visualstudio.com/) redaktorundan və onların [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) üçün birinci tərəf genişləndirməsindən istifadə etməyi tövsiyə edirik.

> Visual Studio Code [quraşdırma qaydası](https://youtu.be/-jMBdw1WtSs) Azərbaycan dilində

Bu alətlər quraşdırıldıqdan sonra istənilən Laravel layihəsini Windows Terminalından istifadə edərək proqramınızın kök kataloqundan `code .` əmrini icra etməklə aça bilərsiniz.

### Linux sistemində başlamaq üçün [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

Əgər Linux sistemindən istifadə edirsinizsə və Docker Desktop artıq quraşdırılıbsa, sadə terminal əmri istifadə edərək, yeni Laravel proyekti yarada bilərsiz. Misal üçün, "example-app" direktivində yeni Laravel tətbiqini yaratmaq üçün, növbəti əmrdən istifadə etmək lazımdır:

`curl -s "https://laravel.build/example-app" | bash`

Əlbəttə siz "example-app" əvəzinə istədiyiniz yaza bilərdiniz. Sadəcə o zaman proyektinizin direktivi həmin cür adlanacaq.

Laravel tətbiqiniz yaradıldıqdan sonra, həmin direktivə keçid edib Sail işlətmək lazımdır.

```
cd example-app

./vendor/bin/sail up
```

Sail-i ilk dəfə işlətmək biraz vaxtınızı alacaq ki, lazımı konteynerlər qurulsun. Bir neçə dəqiqə ala bilər. Lakin narahat olmağa heç bir səbəb yoxdur, sonrakı cəhdləriniz daha tez yerinə yetiriləcək.

Tətbiqiniz Docker konteynerləri işləməyə başladıqdan sonra siz tətbiqinizi [http://localhost](http://localhost) adresinə brauzerdən keçməklə baxa bilərsiniz.

> Laravel Sail haqqında daha çox məlumat əldə etmək üçün [buraya](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Paketl%C9%99r.md#Sail) keçid edə bilərsiniz


### Öz Sail servislərini seçmək [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)



### Composer ilə quraşdırma [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Ayarlama - Configuration [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Giriş [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Mühitin ayarlanması [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Mühitin Fayl TƏhlükəsizliyi [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Əlavə mühit faylları [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Mühitin Dəyişkənlərinin Növləri [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Retrieving Environment Configuration - Düzgün tərcüməsini hələlik dəqiq bilmirəm [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Mövcud mühitin müəyyən edilməsi [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

## Ayar dəyərlərinə daxil olmaq [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Kataloq strukturu [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Başlanğıc dəstləri [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)

# Deployment [ :point_up_2: ](https://github.com/aytiqaqash/azresource/blob/main/Laravel/Dokumentasiya/8.x/Ba%C5%9Flan%C4%9F%C4%B1c.md#i%CC%87nstalyasiya)