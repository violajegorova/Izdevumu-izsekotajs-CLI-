from storage import load_expenses
import csv

def export_to_csv():
    """Eksportē izdevumus CSV failā ar lietotāja izvēlētu nosaukumu."""
    expenses = load_expenses()
    default_filename = "izdevumi.csv"
    user_filename = input(f"Faila nosaukums [{default_filename}]: > ").strip()
    if not user_filename:
        filename = default_filename
    elif "." not in user_filename:
        filename = f"{user_filename}.csv"
    else:
        filename = user_filename

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {filename}")

def export_expenses_to_csv(expenses, filename, total=None):
    """Eksportē izdevumus CSV failā ar norādīto nosaukumu un opciju pievienot kopējo summu."""
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
        if total is not None:
            writer.writerow({"date": "", "amount": total, "category": "Kopā", "description": ""})
    print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {filename}")   

def export_category_totals_to_csv(category_totals, filename):
    """Eksportē kategoriju kopumus CSV failā ar norādīto nosaukumu."""
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["category", "total"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for category, total in category_totals.items():
            writer.writerow({"category": category, "total": total})
    print(f"✓ Eksportēts kategoriju kopsavilkums: {len(category_totals)} kategorijas -> {filename}")


def main():
    """Ieejas punkts CSV eksporta palaišanai no komandrindas."""
    export_to_csv()
    export_expenses_to_csv(load_expenses(), "izdevumi_kopsavilkums.csv", total=sum(expense["amount"] for expense in load_expenses()))
    category_totals = {}    
    for expense in load_expenses():
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount
    export_category_totals_to_csv(category_totals, "kategoriju_kopsavilkums.csv")
    
if __name__ == "__main__":
    main()