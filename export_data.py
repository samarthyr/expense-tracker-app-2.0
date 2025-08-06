#!/usr/bin/env python
import os
import sys
import django
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from django.core.management import call_command
from django.core.serializers import serialize
from expenses.models import Expense, PocketMoney
from django.contrib.auth.models import User

def export_data():
    # Export users
    users = User.objects.all()
    users_data = serialize('json', users, indent=2)
    
    # Export expenses
    expenses = Expense.objects.all()
    expenses_data = serialize('json', expenses, indent=2)
    
    # Export pocket money
    pocket_money = PocketMoney.objects.all()
    pocket_money_data = serialize('json', pocket_money, indent=2)
    
    # Combine all data
    all_data = []
    
    # Add users
    all_data.extend(json.loads(users_data))
    
    # Add expenses
    all_data.extend(json.loads(expenses_data))
    
    # Add pocket money
    all_data.extend(json.loads(pocket_money_data))
    
    # Write to file with UTF-8 encoding
    with open('local_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(users)} users, {len(expenses)} expenses, and {len(pocket_money)} pocket money records")

if __name__ == '__main__':
    export_data() 