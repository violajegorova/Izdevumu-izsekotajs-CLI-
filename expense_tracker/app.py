from datetime import datetime

from storage import load_expenses, save_expenses
import logic

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Mājoklis", "Apģērbs", "Veselība", "Izglītība", "Hobiji", "Ceļojumi", "Citas kategorijas"]


def show_menu():
    # Galvenā izvēlne ar darbībām
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ")


def main():
    print("═════════════════════════════════")
    print("Laipni lūdzam izdevumu izsekotājā!")
    print("═════════════════════════════════")
    while True:
        choice = show_menu()
        if choice == "1":
            try:
                # Datuma ievade un tulitēja validācija
                while True:
                    date = input("Ievadi datumu (DD-MM-YYYY) vai atstāj tukšu šodienai: ").strip()
                    try:
                        if not date:
                            date = datetime.today().strftime("%d-%m-%Y")
                            break
                        else:
                            datetime.strptime(date, "%d-%m-%Y")
                            break
                    except ValueError:
                        print("Nederīgs datuma formāts. Lūdzu ievadiet datumu DD-MM-YYYY formātā.")
                        continue
                # Summas ievade un tulitēja validācija
                while True:
                    try:
                        amount = float(input("Ievadi izdevuma summu (EUR): ").strip())
                        if amount <= 0:
                            print("Izdevuma summa jābūt lielākai par 0.")
                            continue
                        break
                    except ValueError:
                        print("Nederīga summa. Lūdzu ievadiet skaitli.")
                        continue
                # Kategorijas izvēle un validācija   
                print("\nKategorijas:")
                for i, cat in enumerate(CATEGORIES, 1):
                    print(f"{i}) {cat}")
                while True:
                    try:
                        category = int(input("Izvēlies kategoriju (1-10): ").strip())
                        if not (1 <= category <= 10):
                            print("Izdevuma kategorijai jābūt no 1 līdz 10.")
                            continue
                        break
                    except ValueError:
                        print("Nederīga izvēle. Lūdzu ievadiet skaitli no 1 līdz 10.")
                        continue
                    continue
                # Apraksta ievade un validācija
                while True:
                    description = input("Ievadi izdevuma aprakstu: ").strip()
                    if not description:
                        print("Izdevuma apraksts nedrīkst būt tukšs.")
                        continue
                    break
                logic.add_expense(expense_date=date, amount=amount, category=category, description=description)
                print("✓ Pievienots: {date} | {category} | {amount:.2f} | {description}".format(
                    date=date if date else "Šodien",
                    category=CATEGORIES[category - 1],
                    amount=amount,
                    description=description))
                save_expenses(load_expenses())
            except ValueError as e:
                print(f"Kļūda: {e}")
        elif choice == "2":
            try:
                expenses, total = logic.list_expenses()
                if not expenses:
                    print("Nav pievienotu izdevumu.")
                    continue

                # Aprēķina kolonnu platumu no faktiskajiem datiem, lai tabula pielāgotos saturam.
                date_values = [str(exp.get("date", "")) for exp in expenses]
                amount_values = [f"{float(exp.get('amount', 0)):.2f}" for exp in expenses]
                category_values = [str(exp.get("category", "")) for exp in expenses]
                description_values = [str(exp.get("description", "")) for exp in expenses]

                min_w_date = 12
                min_w_amount = 10
                min_w_category = 45
                min_w_desc = 0

                w_date = max(min_w_date, len("Datums"), max((len(v) for v in date_values), default=0))
                w_amount = max(min_w_amount, len("Summa"), max((len(v) for v in amount_values), default=0))
                w_category = max(min_w_category, len("Kategorija"), max((len(v) for v in category_values), default=0))
                w_desc = max(min_w_desc, len("Apraksts"), max((len(v) for v in description_values), default=0))

                # Tabulas kolonnu nosaukumi
                header = f"\n{'Datums':<{w_date}} | {'Summa':>{w_amount}} | {'Kategorija':<{w_category}} | {'Apraksts':<{w_desc}}"
                footer = f"{'-' * w_date}---{'-' * w_amount}---{'-' * w_category}---{'-' * w_desc}"
                print(header)
                print("-" * len(header))
                for exp in expenses:
                    print(
                        f"{str(exp.get('date', '')):<{w_date}} | "
                        f"{float(exp.get('amount', 0)):{w_amount}.2f} | "
                        f"{str(exp.get('category', '')):<{w_category}} | "
                        f"{str(exp.get('description', '')):<{w_desc}}")
                print(footer)
                print(f"Kopējā summa: {total:.2f}")
            except ValueError as e:
                print(f"Kļūda: {e}")
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle. Lūdzu izvēlies no 1 līdz 7.")

if __name__ == "__main__":
    main()