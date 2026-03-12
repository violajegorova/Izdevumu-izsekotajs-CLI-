# Izstrādes žurnāls
Šajā failā tiek aprakstīti soļi projekta "Izdevumu izsēkotājs" izstrādes laikā

## 07.03.2026 
### 1. solis (plānošana)
1. Izveidoju projekta mapi ar struktūru atbilstoši projekta prasībām
2. Uzrakstīju projekta sākotnējo plānu, iekļaujot tajā programmas aprakstu, datu struktūru, moduļu plānu, dažus lietotāja scenārijus, iekļaujot dažus robežgadījumus

### 2. solis (datu slānis un pamata darbības)
Sāku strādāt ar storage.py failu un izveidoju tajā šādas funkcijas:
- "load_expenses()", kura nolasa attiecīgo JSON failu un gadījumā, ja fails neeksistē, tad atgriež []
- "save_expeenses(expenses)", kura saglābā sarakstu JSON failā

## 08.03.2026
### 2. soļa turpinājums
1. Sāku strādāt ar logic.py failu, kurā ierakstīju izdevumu kategorijas. Pievienoju failā šādas funkcijas:
   - "sum_total(expenses)", kura aprēķina izdevumu kopējo summu
   - "add_expenses(expenses)", kura ļauj pievienot izdevumu
   - "list_expenses(expenses)", kura parāda visus ievadītus izdevumus
2. Failā app.py pievienoju funkcijas:
   - "show_menu()", kura ir programmas galvenā izvelne ar pieejamām darbībām:
     * "1. Pievienot izdevumu"
     * "2. Parādīt izdevumus"
     * "3. Iziet"
   - "main()", kura ir galvenais programmas cikls. Uz šo brīdi ir izveidots cikls ar 3 darbībām:
     * Pievienot izdevumu
     * Parādīt izdevumus, atgriežot tos tabulas veidā. 
     * Iziet no programmas
3. Notestēju programmu. Konstatēju, ka:
   - Visi izdevumi nepārādās tā kā gribēju (tabulas veidā). Palūdzu MI palīdzību, lai saprastu kā parādīt izdevumus tabulas veidā. Nevarēju saprast kāpēc man nemainās kolonnas platumi (izvēloties garāko kategorijas nosaukumu pie izdevumu ievades saskaros ar to, ka nosaukums ielīst nākamajā kolonnā) līdz izgāju no programmas un sāku no jauna. Noskaidroju, ka \n nozīmē izvada atstarpi starp rindām.
   - ievadot negatīvu summu kļūda parādas tikai pēc visu 4 datu ievades un piedāvā izvēlēties jaunu darbību. Tās nav lietotājam draudzīgi, jo viss jāsāk no jauna. app.py papildināju ar validācijām, lai kļūdas parādītos uzreiz un var ievadīt derīgu summu. To pašu izdarīju aī attiecībā uz citiem datiem.

### 3. solis (Filtrēšana, kopsavilkums un dzēšana)
Atbilstoši uzdevuma noteikumiem papildināju šādus failus ar šādam funkcijām:
- logic.py:
  * "filter_by_month", kura piedāvā lietotājam filtrēt izdevumus pa mēnešiem;
  * "sum_by_category", kura piedāvā saskaitīt visus izdevumus kategorijas ietvaros;
  * "get_available_months", kura parāda, kuros mēnešos tika reģistrēti izdevumi.
- app.py:
  * Filtrēt pēc mēneša
  * Kopsavilkums pa kategorijām
  * Dzēst izdevumus 

## 11.03.2026
### 3. soļa turpinājums
1. Beidzot tiku līdz testēšanai. Testēšana parāda, ka jaunās funkcijas strādā. Taču konstatēju ka pēc kāda izdevuma dzēšanas programma atgriežas uz galveno izvelni, kas nav ērti, ja jādzēš vairāki izdevumi. Šo vajadzētu izlabot, lai programma pajautātu, vai vēlos dzēst vēl kādu izdevumu. Izlaboju. Papildināju, ka pēc izdevuma dzēšanasparādas atjaunots izdevumu saraksts un tiek jautāt, vai vēlos dzēst vēl kādus izdevumus. Tai pat laikā pazuda izdevumu numerācija, ka tiek izvadīts izdevuma saraksts. Man arī nepatika, ka izvadītajā tabulā ieraksti un kolonnu nosaukumiem atšķiras pēc izmēriem, attiecīgi palīdzu MI to pielagot, jo pašai nesanāca (pamainīt kolonnu garumus nepalīdzēja.) Tā rezultātāMI izveidoja jaunu funkciju app.py failā, kura izvada izdevumus tabulas formātā. 
2. Rindu skaits app.py uz šo brīdi rādās vairāk nekā 200, palūdzu MI nedaudz optimizēt vietu, kas tika veiksmīgi izdarīts.
3. Nolēmu arī pie izdevumu pievienošanai pierakstīt klāt, ka pēc to ievades programma jautā vai vēlos vēl pievienot izdevumus

## 12.03.2026
### 4. solis (CSV eksports un dokumentācija)
Tika izveidots jauns fails export.py, kurā tika izveidota funkcija export_to_csv, kas ļauj izdevumus eksportēt uz .csv failu. Ņemot vērā šo jaunu funkciju tika papildināts fails app.py ar jaunu izvēli galvenajā izvēlnē “Eksportēt uz CSV”.
Iztestēju jaunu funkciju. Konstatēju, ka tiek eksportēti visi izdevumi. Manuprāt, vajadzētu piedāvāt eksportēt uz .csv, piemēram, izdevumus noteiktā mēneša ietvaros vai arī noteiktajā kategorijā. Papildināju export.py ar funkcijām, kuras ļautu eksportēt izdevumus pa mēnešiem vai kopsavilkumu pa kategorijām. Attiecīgi arī papildināju app.py ar šīm funkcijām un tagad rīks jautā vai vēlos eksportēt izdevumus pa mēnešiem/ kopsavilkumu pa kategorijām. 
