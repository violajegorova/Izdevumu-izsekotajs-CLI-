
from datetime import datetime
import storage


CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Mājoklis un komunālie pakalpojumi", "Apģērbs", "Veselība", "Izglītība", "Hobiji", "Ceļojumi", "Citas kategorijas"]

def sum_total(expenses):
    """Saskaita visus izdevumus un atgriež kopējo summu."""
    return sum(float(exp.get("amount", 0)) for exp in expenses)

def filter_by_month(month, year, expenses=None):
    """Atgriež izdevumus, kas atbilst konkrētam mēnesim un gadam."""
    if expenses is None:
        expenses = storage.load_expenses()

    filtered = []
    for exp in expenses:
        try:
            exp_date = datetime.strptime(exp.get("date", ""), "%d-%m-%Y")
            if exp_date.month == month and exp_date.year == year:
                filtered.append(exp)
        except ValueError:
            # Izlaiž ierakstus ar bojātu datuma formātu
            continue
    return filtered

def sum_by_category(expenses=None):
    """Atgriež summas pa visām kategorijām, kurās ir vismaz viens izdevums."""
    if expenses is None:
        expenses = storage.load_expenses()

    totals = {}
    for exp in expenses:
        category = exp.get("category")
        if not category:
            continue
        amount = float(exp.get("amount", 0))
        totals[category] = totals.get(category, 0.0) + amount
    return totals

def get_available_months(expenses=None):
    """Atgriež visus mēnešus un gadus, kuros ir vismaz viens izdevums."""
    if expenses is None:
        expenses = storage.load_expenses()

    available = set()
    for exp in expenses:
        try:
            exp_date = datetime.strptime(exp.get("date", ""), "%d-%m-%Y")
            available.add((exp_date.month, exp_date.year))
        except ValueError:
            # Izlaiž ierakstus ar bojātu datuma formātu
            continue
    return sorted(available, key=lambda x: (x[1], x[0]), reverse=True)

def add_expense(expense_date, amount, category, description):
    """Pievieno jaunu izdevumu un saglabā to storage.
    Argumenti:
        expense_date (str): Izdevuma datums DD-MM-YYYY formātā.
        amount (float): Izdevuma summa (>0).
        category (int): Izdevuma kategorija no 1 līdz 10.
        description (str): Izdevuma apraksts.
    Atgriež pievienotā izdevuma datus kā tuple (expense_date, amount, category, description).
    """
    # Validācija
    if not expense_date:
        expense_date = datetime.today().strftime("%d-%m-%Y")
    try:
        datetime.strptime(expense_date, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Nederīgs datuma formāts. Lūdzu ievadiet datumu DD-MM-YYYY formātā.")
    if amount <= 0:
        raise ValueError("Izdevuma summa jābūt lielākai par 0.")
    if not (1 <= category <= 10):
        raise ValueError("Izdevuma kategorijai jābūt no 1 līdz 10.")  
    if not description.strip():
        raise ValueError("Izdevuma apraksts nedrīkst būt tukšs.") 
    category_name = CATEGORIES[category - 1]
    # Ielādē esošus izdevumus, pievieno jauno un saglabā atpakaļ
    expenses = storage.load_expenses()
    # Pievieno jauno izdevumu
    expenses.append({
        "date": expense_date,
        "amount": amount,
        "category": category_name,
        "description": description})
    # Saglabā izmaiņas
    storage.save_expenses(expenses)
    return expense_date, amount, category, description
 
def list_expenses():
    """Parāda visus izdevumus un kopējo summu.
    Izdevumi tiek parādīti formātā: datums | kategorija | summa | apraksts.
    Pēc izdevumu saraksta tiek parādīta kopējā summa."""
    expenses = storage.load_expenses()
    if not expenses:
        raise ValueError("Nav pievienotu izdevumu.")
    else:
        return expenses, sum_total(expenses)

def list_expenses_by_month(month, year):
    """Atgriež izdevumus par izvēlēto mēnesi un gada kopējo summu."""
    if not (1 <= month <= 12):
        raise ValueError("Mēnesim jābūt no 1 līdz 12.")

    filtered = filter_by_month(month, year)
    return filtered, sum_total(filtered)
    
def erase_expense(expense_id):
    """Dzēš izdevumu pēc 1-bāzēta ID un atgriež dzēsto ierakstu."""
    expenses = storage.load_expenses()
    if not expenses:
        raise ValueError("Nav pievienotu izdevumu.")

    if not isinstance(expense_id, int):
        raise ValueError("Izdevuma ID jābūt veselam skaitlim.")

    if not (1 <= expense_id <= len(expenses)):
        raise ValueError(f"ID jābūt no 1 līdz {len(expenses)}.")

    deleted_expense = expenses.pop(expense_id - 1)
    storage.save_expenses(expenses)
    return deleted_expense
    