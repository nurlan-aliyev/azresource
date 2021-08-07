/*
JavaScript dili üzrə kod nümunələri - müəllif Nurlan Aliyev,  07/08/2021
Kod №3 - Üçbucağın sahəsinin hesablanması
Kopyalayıb kodu test edə bilərsiniz
Və yaxud bu link vasitəsilə yoxlaya bilərsiniz  https://replit.com/@NurlanAliyev/3UcbucaqSahesi#index.js
*/


//Üçbucağın hündürlüyü və oturacağı məlum olduqda
const oturacaq = prompt('Üçbucağın oturacağını sm-lə daxil edin: ');
const hündürlük = prompt('Üçbucağın hündürlüyünü sm-lə daxil edin: ');

// Sahənin hesablanması, sahə oturacaq ilə hündürlük hasilinin yarısına bərabərdir
const sahe = (oturacaq * hündürlük) / 2;

console.log(
  `Üçbucağın sahəsi ${sahe} kvadrat santimetrdir`
);


//İkinci variant, istifadə etmək üçün yuxarıdakı sətrləri şərh blokuna çevirin və yaxud silin

//Üçbucağın sahəsinin Heron düsturu ilə tapılması

const teref1 = parseInt(prompt('Birinci tərəfi daxil edin: '));
const teref2 = parseInt(prompt('İkinci tərəfi daxil edin: '));
const teref3 = parseInt(prompt('Üçüncü tərəfi daxil edin:  '));

// Yarım perimetrin hesablanması
const yarımPerimetr = (teref1 + teref2 + teref3) / 2;

//Sahənin hesablanması
const saheHeron = Math.sqrt(
  yarımPerimetr * (yarımPerimetr - teref1) * (yarımPerimetr - teref2) * (yarımPerimetr - teref3)
);

console.log(
  `Üçbucağın sahəsi ${sahe} kvadrat santimetrdir`
);
