# Dəyişənlər (Variables)

Çox vaxt JavaScript proqramları məlumatla işləyir. 

Misal üçün:

Onlayn mağaza - satılacaq məhsul haqqında məlumat.
Söhbət Proqramı – İstifadəçi və mesaj məlumatları.

Bu məlumatı saxlamaq üçün dəyişənlərdən istifadə olunur. Dəyişən "adlandırılmış yaddaş" adlanır. Dəyişənlərlə biz istifadəçiləri, məhsulları və digər məlumat növlərini saxlaya bilərik.

JavaScript-də dəyişən let sözü ilə yaradılır.

Məsələn message adında bir dəyişən yaradaq:

let message;

İndi isə biz artıq bu dəyişənə məlumat yerləşdirə bilərik. Bunu etmək üçün =  operatorunu istifadə edirik.

let message; 

message = "Salam Dünya"

Artıq biz bir dəyişən yaratdıq və ona biz məlumat yerləşdirdik. Bundan sonra həmin məlumatı istifadə etmək istəsək sadəcə message yazmağımız kifayət olacaq.
Həmçinin dəyişənlər bu formada da təyin oluna bilər:

let mesaj = "Salam Dünya"; 

Birdən daha çox dəyişən yaratmaq üçün isə:

let name = 'Istifadəçi', age = 25, message = 'Salam';

Eyni zamanda burada bir dəyişənə məlumat təyin etdikdən sonra həmin məlumatı dəyişə bilərik. Məsələn biz yuxarıda name adında dəyişən yaratdıq və ona 'İstifadəçi'(burada dırnaqcıqlardan istifadə etmək lazımdır) məlumatını verdik.İndi isə onu dəyişmək istəsək, belə yaza bilərik:

name = "Dəyişdi"

Artıq burada name adında dəyişənə verdiyimiz məlumatı dəyişmiş olduq.

### Dəyişənlərin adlandırılması

JavaScript dilində dəyişənlər yaratarkən bəzi məhdudiyyətlər var.

1. Dəyişən adında yalnız hərflər, rəqəmlər, $ və _ simvolları ola bilər.
2. Birinci simvol rəqəm ola bilməz.

Məsələn bu formada dəyişənlər yarada bilərsiniz:
let userName;

let test123;

Əgər dəyişənin adında birdən çox sözdən istifadə olunursa, birinci sözün birinci hərfi hər kiçik hərflə yazılır onda sonrakı sözlərin birinci hərfi isə böyük hərflə yazılır.

Məsələn: let thisIsExampleVariable;

Bu adlandırma üsulu CamelCase deyilir

'$' işarəsi və '_' işarəsi də dəyişənlərin adında istifadə edilə bilər. Onların hər hansı bir fərqli mənası yoxdur. Yəni aşağıdakı formalarda dəyişən təyin edə bilərsiniz.

let $ = 5;

let _ = true

let $test = 15;

Həmçinin qeyd etmək lazımdır ki, dəyişən adları rəqəm ilə başlaya bilməz və qeyd etdiyimiz iki işarədən başqa simvolları istifadə etmək olmaz.


### Sabit dəyişənlər və ya Sabitlər
Biz qeyd etdik ki, dəyişən təyin etmək üçün let ifadəsindən istifadə olunur lakin bundan başqa ifadələr də var.
Dəyişənlərin bir növü də sabit dəyişənlər və ya sabitlər adlanır. OSabiti təyin etmək üçün let əvəzinə const istifadə olunur.

const name = "Test";

Const ilə təyin olunan dəyişənlər "sabitlər" kimi müəyyən edilir. Onları dəyişdirmək mümkün deyil, onları dəyişdirmək istəyərkən xəta alınır:
Əgər mən bu const ilə təyin etdiyimiz name adlı dəyişəni dəyişmək istəsək, xəta baş verəcək

name = "User"; // xəta, sabitin dəyəri dəyişdirilə bilməz!

const name = 'User'; // xəta, sabitin dəyəri dəyişdirilə bilməz!


Əgər təyin etdiyiniz dəyişənin qiymətini dəyişməyəcəksinizsə, const ilə dəyişən təyin edə bilərsiniz.

