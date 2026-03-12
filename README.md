# Izdevumu Izsekotājs (CLI)

Satura rādītājs:
[Projekta apraksts](#projekta-apraksts)
[Uzstādīšana](#-uzstādīšana)
[Funkcionalitāte](#-funkcionalitātes)

## Projekta apraksts
Vienkāršs komandrindas rīks personīgo izdevumu uzskaitei.  
Lietotājs var pievienot jaunus izdevumus, apskatīt sarakstu un redzēt kopējo summu.  
Dati tiek glabāti JSON failā ("expenses.json"), un programma automātiski to veido un atjaunina.

Izstrādāts Python valodā

## 📦 Uzstādīšana

1)	Klonē repozitoriju:
-	Ar GitHub CLI: gh repo clone violajegorova/Izdevumu-izsekotajs-CLI-; vai
-	Ar Git: git clone https://github.com/violajegorova/Izdevumu-izsekotajs-CLI-.git
``
2)	Atver lejupielādēto mapi savā datorā un Nospied labo peles taustiņu mapes tukšajā vietā un izvēlies “Open in Terminal”
 (Windows / macOS / Linux – atkarībā no OS nosaukums var nedaudz atšķirties).
3)	Izveido virtuālo vidi (ieteicams): 
-	python -m venv venv
-	Aktivizēšana:
o	Windows: venv\Scripts\activate
``
o	macOS / Linux: source venv/bin/activate
4)	Instalē nepieciešamās Python pakotnes: pip install -r requirements.txt
5)	Palaid programmu: python app.py

## 📦 Funkcionalitātes

### ✔ Izdevumu pievienošana
-	Datuma ievade (DD-MM-YYYY, tukšs → šodienas datums)
-	Summas validācija (pozitīvs skaitlis)
-	Kategorijas izvēle no piedāvātā saraksta
-	Ne-tukšs apraksts
-	Iespēja turpināt ievadi bez atgriešanās izvēlnē

### ✔ Izdevumu parādīšana
-	Skaista tabula ar: 
    o	datumu,
    o	summu (EUR),
    o	kategoriju,
    o	aprakstu.
-	Kopsummas aprēķins.

### ✔ Filtrēšana pēc mēneša
-	Pieejamo mēnešu saraksts
-	Parāda tikai konkrētā mēneša izdevumus
-   Eksportēšana uz .csv failu

### ✔ Kopsavilkums pa kategorijām
-   Parāda visus izdevumus izvēlētajā kategorijā
-   Eksportē uz .csv failu

### ✔ Izdevuma dzēšana
-	Parāda visu izdevumu sarakstu
-	Lietotājs ievada dzēšamā ieraksta ID
-	Saraksts pēc dzēšanas tiek automātiski atjaunots
-	Iespēja dzēst vairākus pēc kārtas

### ✔ Eksportēšana uz .csv failu
Izdevumu eksports CSV formātā

### ✔ Iziet no programmas

## Zināmie ierobežojumi
-   Programma darbojas tikai komandrindā (CLI), bez grafiskā interfeisa.
-   Dati tiek glabāti lokāli JSON failā, tāpēc nav lietotāju kontu vai sinhronizācijas starp ierīcēm.
-   CSV eksports izveido failu ar norādīto nosaukumu; ja izmanto to pašu nosaukumu, iepriekšējais fails var tikt pārrakstīts. 
-   Projektam pašlaik nav automatizētu testu, tāpēc validācija veikta ar manuālu pārbaudi.

Autors: Violeta Jegorova