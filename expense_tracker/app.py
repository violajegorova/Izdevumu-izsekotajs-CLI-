import export
import logic
from datetime import datetime

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Mājoklis", "Apģērbs", "Veselība", "Izglītība", "Hobiji", "Ceļojumi", "Citas kategorijas"]

def print_expenses_table(expenses, include_id=False):
    """Izdrukā izdevumus tabulas formātā ar vienādiem kolonnu platumiem."""
    if include_id:
        id_values = [str(i) for i in range(1, len(expenses) + 1)]
        w_id = max(len("ID"), max((len(v) for v in id_values), default=0))

    date_values = [str(exp.get("date", "")) for exp in expenses]
    amount_values = [f"{float(exp.get('amount', 0)):.2f} EUR" for exp in expenses]
    category_values = [str(exp.get("category", "")) for exp in expenses]

    w_date = max(len("Datums"), max((len(v) for v in date_values), default=0))
    w_amount = max(len("Summa"), max((len(v) for v in amount_values), default=0))
    w_category = max(len("Kategorija"), max((len(v) for v in category_values), default=0))

    if include_id:
        header = f"{'ID':<{w_id}} | {'Datums':<{w_date}} | {'Summa':>{w_amount}} | {'Kategorija':<{w_category}} | Apraksts"
    else:
        header = f"{'Datums':<{w_date}} | {'Summa':>{w_amount}} | {'Kategorija':<{w_category}} | Apraksts"

    print(header)
    print("-" * len(header))

    for idx, exp in enumerate(expenses, 1):
        amount_text = f"{float(exp.get('amount', 0)):.2f} EUR"
        if include_id:
            print(
                f"{idx:<{w_id}} | "
                f"{str(exp.get('date', '')):<{w_date}} | "
                f"{amount_text:>{w_amount}} | "
                f"{str(exp.get('category', '')):<{w_category}} | "
                f"{str(exp.get('description', ''))}"
            )
        else:
            print(
                f"{str(exp.get('date', '')):<{w_date}} | "
                f"{amount_text:>{w_amount}} | "
                f"{str(exp.get('category', '')):<{w_category}} | "
                f"{str(exp.get('description', ''))}")

def show_menu():
    # Galvenā izvēlne ar darbībām
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt uz CSV")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")

def main():
    print("══════════════════════════════════")
    print("Laipni lūdzam izdevumu izsekotājā!")
    print("══════════════════════════════════")
    while True:
        choice = show_menu()
        if choice == "1":
            continue_adding = True
            while continue_adding:
                date = input("Ievadi datumu (DD-MM-YYYY) vai atstāj tukšu šodienai: ").strip()
                while date:
                    try:
                        datetime.strptime(date, "%d-%m-%Y")
                        break
                    except ValueError:
                        print("Nederīgs datuma formāts. Lūdzu ievadiet datumu DD-MM-YYYY formātā.")
                        date = input("Ievadi datumu (DD-MM-YYYY) vai atstāj tukšu šodienai: ").strip()

                while True:
                    amount_input = input("Ievadi izdevuma summu (EUR): ").strip()
                    try:
                        amount = float(amount_input)
                    except ValueError:
                        print("Nederīga summa. Lūdzu ievadiet skaitli.")
                        continue
                    if amount <= 0:
                        print("Izdevuma summa jābūt lielākai par 0.")
                        continue
                    break

                print("\nKategorijas:")
                for i, cat in enumerate(CATEGORIES, 1):
                    print(f"{i}) {cat}")

                while True:
                    category_input = input(f"Izvēlies kategoriju (1-{len(CATEGORIES)}): ").strip()
                    try:
                        category = int(category_input)
                    except ValueError:
                        print("Nederīga ievade. Lūdzu ievadiet skaitli.")
                        continue
                    if not (1 <= category <= len(CATEGORIES)):
                        print(f"Izdevuma kategorijai jābūt no 1 līdz {len(CATEGORIES)}.")
                        continue
                    break

                while True:
                    description = input("Ievadi izdevuma aprakstu: ").strip()
                    if description:
                        break
                    print("Izdevuma apraksts nedrīkst būt tukšs.")

                try:
                    logic.add_expense(expense_date=date, amount=amount, category=category, description=description)
                    print("✓ Pievienots: {date} | {category} | {amount:.2f} | {description}".format(
                    date=date if date else "Šodien",
                    category=CATEGORIES[category - 1],
                    amount=amount,
                    description=description))
                except ValueError as e:
                    print(f"Kļūda: {e}")
            
                while True:
                    response = input("Pievienot vēl? (Jā/nē): ").strip().lower()
                    if response in ["jā", "ja", "j"]:
                        break
                    if response in ["nē", "ne", "n"]:
                        continue_adding = False
                        break
                    else:
                        print("Nederīga ievade. Lūdzu ievadiet 'Jā' vai 'nē'.")
        elif choice == "2":
            try:
                expenses, total = logic.list_expenses()
                if not expenses:
                    print("Nav pievienotu izdevumu.")
                    continue

                print_expenses_table(expenses)

                print(f"Kopējā summa: {total:.2f}")
            except ValueError as e:
                print(f"Kļūda: {e}")
        elif choice == "3":
            try:
                available_months = logic.get_available_months()

                if not available_months:
                    print("Nav pieejamu mēnešu ar izdevumiem.")
                    continue

                print("\nPieejamie mēneši:")
                for idx, (month, year) in enumerate(available_months, 1):
                    print(f"{idx}) {month:02d}-{year}")

                while True:
                    try:
                        month_choice = int(input(f"Izvēlies mēnesi (1-{len(available_months)}): ").strip())
                        if not (1 <= month_choice <= len(available_months)):
                            print(f"Izvēlei jābūt no 1 līdz {len(available_months)}.")
                            continue
                        break
                    except ValueError:
                        print("Nederīga ievade. Lūdzu ievadiet skaitli.")

                month, year = available_months[month_choice - 1]
                filtered, filtered_total = logic.list_expenses_by_month(month, year)
                if not filtered:
                    print(f"Nav izdevumu par {month:02d}-{year}.")
                else:
                    print(f"Izdevumi par {month:02d}-{year}:")
                    print_expenses_table(filtered)
                    print(f"Kopējā summa: {filtered_total:.2f}")

                    while True:
                        export_choice = input("Vai vēlies eksportēt šo mēneša sarakstu uz CSV? (Jā/nē): ").strip().lower()
                        if export_choice in ["jā", "ja", "j"]:
                            export.export_expenses_to_csv(filtered, f"izdevumi_{month:02d}_{year}.csv", total=filtered_total)
                            break
                        if export_choice in ["nē", "ne", "n"]:
                            break
                        print("Nederīga ievade. Lūdzu ievadiet 'Jā' vai 'nē'.")

            except ValueError as e:
                print(f"Kļūda: {e}")            
        elif choice == "4":
            category_totals = logic.sum_by_category()

            if not category_totals:
                print("Nav izdevumu, ko grupēt pa kategorijām.")
                continue

            print("\nKopsavilkums pa kategorijām:")
            for category_name, total in sorted(category_totals.items()):
                print(f"\n{category_name}: {total:.2f} EUR")

            while True:
                export_choice = input("Vai vēlies eksportēt šo kopsavilkumu uz CSV? (Jā/nē): ").strip().lower()
                if export_choice in ["jā", "ja", "j"]:
                    export.export_category_totals_to_csv(category_totals, "kategoriju_kopsavilkums.csv")
                    break
                if export_choice in ["nē", "ne", "n"]:
                    break
                print("Nederīga ievade. Lūdzu ievadiet 'Jā' vai 'nē'.")
        elif choice == "5":
            try:
                expenses, total = logic.list_expenses()
                if not expenses:
                    print("Nav pievienotu izdevumu.")
                    continue

                print_expenses_table(expenses, include_id=True)
                print(f"Kopējā summa: {total:.2f}")

                continue_deleting = True
                while continue_deleting:
                    try:
                        del_id = int(input("Ievadi dzēšamā izdevuma ID (0 lai atceltu): ").strip())
                        if del_id == 0:
                            print("Dzēšana atcelta.")
                            break

                        deleted_expense = logic.erase_expense(del_id)
                        print(f"Izdevums dzēsts: {deleted_expense}")

                        try:
                            expenses, _ = logic.list_expenses()
                        except ValueError:
                            expenses = []

                        print("Atjaunināts izdevumu saraksts:")
                        if expenses:
                            print_expenses_table(expenses, include_id=True)
                            print(f"Kopējā summa: {logic.sum_total(expenses):.2f}")
                        else:
                            print("Nav pievienotu izdevumu.")
                            continue_deleting = False
                            break

                        while True:
                            response = input("Dzēst vēl? (Jā/nē): ").strip().lower()
                            if response in ["jā", "ja", "j"]:
                                break
                            if response in ["nē", "ne", "n"]:
                                continue_deleting = False
                                break
                            else:
                                print("Nederīga ievade. Lūdzu ievadiet 'Jā' vai 'nē'.")
                    except ValueError:
                        print(f"Nederīga ievade. Lūdzu ievadiet skaitli no 1 līdz {len(expenses)}.")
            except ValueError as e:
                print(f"Kļūda: {e}")
        elif choice == "6":
            try:
                export.export_to_csv()
            except Exception as e:
                print(f"Kļūda eksportējot uz CSV: {e}")        
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle. Lūdzu izvēlies no 1 līdz 7.")   

if __name__ == "__main__":
    main()