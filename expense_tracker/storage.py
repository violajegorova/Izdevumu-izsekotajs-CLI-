from pathlib import Path
import json
import re
import csv

BASE_DIR = Path(__file__).parent
DEFAULT_LIST_FILE = BASE_DIR / "expenses.json"

def load_expenses():
    """
    Nolasa expenses.json un atgriež sarakstu ar izdevumiem.
    Ja fails neeksistē vai ir bojāts – atgriež tukšu sarakstu [].
    """
    if not DEFAULT_LIST_FILE.exists():
        return []
    try:
        text = DEFAULT_LIST_FILE.read_text(encoding="utf-8")
        data = json.loads(text)

        # Jāpārliecinās, ka saraksts ir ar dict elementiem
        if isinstance(data, list) and all(isinstance(x, dict) for x in data):
            return data
        
        # Ja dati nav pareizā formātā, atgriež tukšu sarakstu
        return []
    except Exception:
        # Ja rodas kļūda, atgriež tukšu sarakstu
        return []
    
def save_expenses(expenses):
    """Saglabā izdevumus expenses.json failā.

    Sagaida sarakstu ar dict elementiem, piem.:
    {"date": "08-03-2026", "amount": 12.5, "category": "Ēdiens", "description": "Pusdienas"}
    """
    if not isinstance(expenses, list):
        raise ValueError("Izdevumiem jābūt sarakstam ar dict elementiem.")

    if not all(isinstance(item, dict) for item in expenses):
        raise ValueError("Katram izdevumam jābūt dict tipa ierakstam.")

    data = expenses
    DEFAULT_LIST_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8") 