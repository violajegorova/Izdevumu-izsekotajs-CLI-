
from datetime import datetime
import re
import storage


CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Mājoklis un komunālie pakalpojumi", "Apģērbs", "Veselība", "Izglītība", "Hobiji", "Ceļojumi", "Citas kategorijas"]

def sum_total(expenses):
    """Saskaita visus izdevumus un atgriež kopējo summu."""
    return sum(expenses.values())

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
        return expenses, sum_total({e['description']: e['amount'] for e in expenses})
    