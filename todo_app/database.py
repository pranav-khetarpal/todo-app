import json
from typing import List, Dict

DATA_FILE = 'data.json'

def load_data() -> List[Dict]:
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data: List[Dict]):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
