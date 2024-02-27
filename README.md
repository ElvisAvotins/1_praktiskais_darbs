# Praktiskā darba apraksts
---TO-DO---
1. Game <- Evita
2. Player <- Rinalds
3. AI <- Artūrs
\n--Minimax
\n--Alpha-Beta
\n--Selecting best move
5. Game state <- Juris
6. Grafiskais <- Elvis
7. Dokumentācija

---Uzdevuma nosacījumi---

Papildu prasības programmatūrai

Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 20000 līdz 30000, bet tādus, kas sākotnēji dalās ar 3, 2 un 4. Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.

Spēles apraksts

Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis. Abiem spēlētājiem ir 0 punktu. Turklāt spēlē tiek izmantota spēles banka, kura sākotnēji ir vienāda ar 0. Spēlētāji izdara gājienus pēc kārtas, katrā gājienā dalot pašreizējā brīdī esošu skaitli ar 2,3 vai 4. Skaitli ir iespējams sadalīt tikai tajā gadījumā, ja rezultātā veidojas vesels skaitlis. Ja dalīšanas rezultātā veidojas pāra skaitlis, tad spēlētājs zaudē 1 punktu, ja nepāra skaitlis, tad viņa punkti tiek palielināti par 1 punktu. Savukārt, ja tiek iegūts skaitlis, kas beidzas ar 0 vai 5, tad bankai tiek pieskaitīts 1 punkts. Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir mazāks vai vienāds ar 10. Spēlētājs, pēc kura gājiena spēle beidzas, iztukšo banku, saviem punktiem pieskaitot bankas punktus. Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu.

---Uzdevuma nostādne---

Šis darbs ļauj studentiem pielietot praksē iegūtās zināšanas par pārmeklēšanā sakņotu problēmu risināšanu, izstrādājot spēles programmatūru. Darba izpildei studentu komanda saņem no mācībspēka spēles aprakstu. Studentu komanda var brīvi izvēlēties programmēšanas valodu vai vidi programmatūras izstrādei.

Programmatūrā ir jānodrošina šādas iespējas lietotājam: 

izvēlēties, kurš uzsāk spēli: lietotājs vai dators;
izvēlēties, kuru algoritmu izmantos dators: Minimaksa algoritmu vai Alfa-beta algoritmu;
izpildīt gājienus un redzēt izmaiņas spēles laukumā pēc gājienu (gan lietotāja, gan datora) izpildes;
uzsākt spēli atkārtoti pēc kārtējās spēles pabeigšanas.
Programmatūrai ir jānodrošina grafiskā lietotāja saskarne (komandrindiņas spēles netiks pieņemtas). Šajā gadījumā runa nav par sarežģītu, 3D grafisko saskarni, bet gan par vizuālu elementu tādu kā izvēlnes, pogas, teksta lauki, ikonas, saraksti, u.c. izmantošanu. 

Izstrādājot programmatūru, studentu komandai obligāti ir jārealizē:

spēles koka vai tā daļas ģenerēšana atkarībā no spēles sarežģītības un studentu komandai pieejamiem skaitļošanas resursiem;
heiristiskā novērtējuma funkcijas izstrāde;
Minimaksa algoritms un Alfa-beta algoritms (kas abi var būt realizēti kā Pārlūkošana uz priekšu pār n-gājieniem);
10 eksperimenti ar katru no algoritmiem, fiksējot datora un cilvēka uzvaru skaitu, datora apmeklēto virsotņu skaitu, datora vidējo laiku gājiena izpildei.
Tādējādi izstrādājot darbu, studentu komandai ir jāizpilda šādi soļi:

1. jāsaņem spēle no mācībspēka;
2. jāizvēlas programmēšanas vide/valoda; Python
3. jāprojektē, jārealizē un jātestē spēle;
4. jāveic eksperimenti ar abiem algoritmiem;
5. jāsagatavo atskaite par izstrādāto spēli un tā ir jāiesniedz e-studiju kursā;
6. jāpiesakās aizstāvēšanas laikam;
7. jāaizstāv izstrādātais darbs.

---Prasības atskaitei---

Studentu komandai ir jāiesniedz atskaite par izstrādāto programmatūru. Atskaitei ir jāsatur:

programmatūras darbības demonstrācijas piemērs vai lietotāja ceļvedis ar paskaidrojumiem; 
apraksts par izmantotajām datu struktūrām spēles koka glabāšanai ar detalizētiem komentāriem, kas tieši tiek glabāts konkrētajā datu struktūrā; 
heiristiskā novērtējuma funkcijas apraksts un pamatojums izvēlētajai funkcijai; 
realizēto pamatalgoritmu (spēles koka ģenerēšana, heiristisko vērtējumu piešķiršana virsotnēm, spēles algoritma pielietojums, uzvaru nesošo ceļu atrašana) kods ar studentu sniegtajiem skaidrojumiem. Kods atskaitei ir jāpievieno tikai teksta veidā. Nav atļauts to pievienot attēlu veidā;
algoritmu salīdzinājums un komandas veiktos secinājumus.
Viss programmatūras kods, kas atbilst spēles realizācijai, nevis grafiskās saskarnes veidošanai, ir:

jāpievieno atskaites pielikumā teksta veidā;
jāpadara arī pieejams kādā publiskajā vietnē (GitHub, Google Drive, u.c.) un saite uz to ir jānorāda uz atskaites titullapas. Izmantojot norādīto saiti, mācībspēkam ir jābūt iespējai lejupielādēt komandas izstrādāto spēli bez papildu reģistrācijas un ierobežojumiem.

---Nodošana un aizstāvēšana---

E-studiju kursa sadaļā “Praktiskie darbi” ir publicēti gala termiņi atskaites nodošanai par izstrādāto programmatūru un reģistrācijai darba aizstāvēšanai. Pēc norādītajiem termiņiem atskaites vairs netiks pieņemtas un programmatūru vairs nebūs iespējams aizstāvēt.

Atskaite par darbu ir jāiesniedz elektroniskajā formātā (.docx vai .pdf), izmantojot e-studiju kursā sadaļā “Praktiskie darbi” pieejamo aktivitāti “Pirmā praktiskā darba atskaites iesniegšana”. 

Studentu komandai ir jāaizstāv izstrādātā programmatūra. Aizstāvēšanas laikā studentam ir jāatbild uz jautājumiem par sistēmas uzbūvi, algoritmu realizāciju un datu struktūru izmantošanu. Studentu komandai ir jārūpējas, lai demonstrācija noritētu veiksmīgi, t.i., būtu pieejamas demonstrācijai nepieciešamās tehnoloģijas un vides. Informācija par pieteikšanos aizstāvēšanai semestra laikā tiks publicēta e-studiju kursā sadaļā “Praktiskie darbi”.

Saziņa ar studentu komandu par darba aizstāvēšanas jautājumiem notiks, izmantojot ORTUS e-studiju kursa ziņojumu sūtīšanas funkcionalitāti.

---Vērtēšana---

Punktu skaits:     15 punkti

Vērtējums par atskaiti – 3 punkti
Vērtējums par izstrādāto programmatūru – 3 punkti
Vērtējums par praktiskā darba aizstāvēšanu – 5 punkti
Vidējais vērtējums studentam savstarpējā vērtēšanā – 4 punkti
Darbs automātiski netiks izskatīts, un aizstāvēšana netiks nozīmēta, ja:

komanda nav iesniegusi darba atskaiti, bet piesakās darba aizstāvēšanai;
komanda iesniedza komandrindiņas programmatūru;
iesniegtajā darbā spēles koks netiek ģenerēts, bet ir predefinēts vai glabāts failā;
iesniegtajā darbā netiek realizēti studiju kursā apskatītie algoritmi (Minimaksa algoritms un Alfa-beta), bet dators izpilda gājienus gadījuma ceļā, vai gājieni ir predefinēti kodā, u.c.;
ir konstatēts akadēmiskā godīguma pārkāpums;
studentu komanda uz atskaites titullapas nav norādījusi saiti uz kodu publiskajā vietnē;
studentu komanda kodu pievienoja atskaitei attēlu veidā.
