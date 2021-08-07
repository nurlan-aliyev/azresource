/*
JavaScript dili üzrə kod nümunələri - müəllif Nurlan Aliyev,  07/08/2021
Kod №4 - Ədədin bölənlərinin tapılması
Kopyalayıb kodu test edə bilərsiniz
Və yaxud bu link vasitəsilə yoxlaya bilərsiniz  https://replit.com/@NurlanAliyev/4KartPaylayici#index.js
*/

// Ədədin istifadəçi tərəfindən daxil edilməsi
const eded = prompt('0-dan böyük bir ədəd daxil edin: ');

console.log(`${eded} ədədinin bölənləri aşağıdakılardır: `);

// 1-dən ədədə qədər tək artan dövr
for(let i = 1; i <= eded; i++) {

    // Ədədin böləninin doğruluğunun yoxlanması
    if(eded % i == 0) {
        console.log(i);
    }
}
