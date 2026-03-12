# Izdevumu izsēkotājs

## A. Programmas apraksts
Šī programma palīdz lietotājam sekot līdzi saviem ikdienas tēriņiem, pierakstot un apskatot tos, kā arī redzēt visu izdevumu sarakstu.
Tā ir paredzēta personīgai finanšu uzskaitei ar vienkāršiem iestatījumiem.
Dati tiek glabāti JSON failā, kuru programma nolasa un atjauno automātiski.

## B. Datu struktūra
### Viena izdevuma ieraksta piemērs
Datums, Summa, Kategorija, Apraksts
Piemērs: 07.03.2026 | 10 EUR | Ēdiens | Pārtika

### Kāpēc šāda struktūra?
Datuma ievade palīdzēs filtrēt izdevumus pa datumiem vai arī pa periodiem.
Summas ievade palīdzēs redzēt savus tēriņus.
Kategorijas ievade palīdzēs sekot līdzi izdevumiem noteiktajā kategorijā.
Apraksta ievade ļaus pierakstīt kas tieši par izdevumiem bija.

## C. Moduļu plāns un tajos ietvertās funkcijas
1. storage.py - atbild par datu glabāšanu un lasīšanu no JSON
    - load_expenses - nolasa izdevumus no JSON faila
    - save_epenses - saglabā sarakstu JSON failā
2. logic.py - programmas loģika
    - sum_total - aprēķina kopējo summu
    - filter_by_month - filtrē izdevumus norādītā mēneša ietvaros
    - sum_by_category - saskaita katras kateorijas kopējo summu 
    - get_available_months - atgriež unikālo mēnešu skaitu
    - add_expense - pievieno izdevumus
    - list_expenses - parāda visus izdevumus
    - list_expenses_by_month - parāda visus izdevumus izvēlētajā mēnesī
    - erase_expenses - dzēš izvēlēto izdevumu
3. export.py - saglabā failu .csv formātā
    - export_to_csv - saglabā izdevumus .csv formātā
    - export_expenses_to_csv - saglabā izfiltrēta mēneša izdevumus .csv formātā
    - export_category_totals_to_csv - saglabā kopsavilkumu pa kategorijām .csv formātā
4. app.py - importē no pārējiem moduļiem un veido interaktīvu izvēlni
    - show_menu - parāda galveno izvelni un atgriež lietotāja izvēli.
    - main - programmas cikls

## D. Lietotāja scenāriji
### Scenārijs 1: Pievieno derīgu izdevumu
    1. Lietotājs izvēlas "1. Pievienot izdevumu".
    2. Ievada datumu: "07.03.2026".
    3. Ievada summu: "10 EUR", 
    4. Izvēlās kategoriju "1"
    5. Ievada izdevuma aprakstu: Pārtika
    6. Programma saglābā ievadīto izdevumu un parāda:
        → "✓ Pievienots: 07.03.2026 | 10 EUR | Ēdiens | Pārtika"

### Scenārijs 2: Ievada negatīvu summu
    1. Lietotājs izvēlas "1. Pievienot izdevumu".
    2. Ievada datumu: "07.03.2026".
    3. Ievada summu: "-5 EUR", 
    4. Izvēlās kategoriju "1"
    5. Ievada izdevuma aprakstu: Pusdienas
    6. Programma atbild:
        → "Kļūda. Summai jābūt pozitīvam skaitlim."
    7. Programma ļauj mēģināt vēlreiz.

### Scenārijs 3: Apskatās visus izdevumus, bet saraksts ir tukšs
    1. Lietotājs izvēlās "2. Parādīt izdevumus"
    2. Izdevumu sarakstā (expenses.json) nav ne viena ieraksta
    3. Programma atbild:
        → "Izdevumu saraksts ir tukšs."

## E. Robežgadījumi
    - expenses.json neeksistē: 
      load_expenses () atgriež [], programma turpina darboties.
    - Ievadīta negatīva summa:
      programma parāda kļūdas paziņojumu "Kļūda. Summai jābūt pozitīvam skaitlim." un ļauj ievadīt summu vēlreiz.
    - Ievadīts tukšs apraksts:
      Programma parāda kļūdas paziņojumu "Kļūda. Aprakstam jābūt ievadītam." un ļauj pievienot aprakstu.
    - Ievadīts nepareizs datums
      Programma parāda kļūdas paziņojumu "Kļūda. Datuma formātam jābūt DD.MM.GGGG" un ļauj ievadīt datumu atkārtoti
    - Apskatīts saraksts kurš ir tukšs
      Programma atbild "Saraksts ir tukšs"