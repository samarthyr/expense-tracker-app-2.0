#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from expenses.models import Expense, PocketMoney

def check_data():
    print("📊 Current Database Status:")
    print("=" * 40)
    
    # Check users
    users = User.objects.all()
    print(f"👤 Users: {users.count()}")
    for user in users:
        print(f"  - {user.username} ({user.email})")
    
    # Check expenses
    try:
        expenses = Expense.objects.all()
        print(f"\n💰 Expenses: {expenses.count()}")
        if expenses.count() > 0:
            for expense in expenses[:5]:  # Show first 5
                print(f"  - {expense.amount} ({expense.category}) - {expense.date}")
            if expenses.count() > 5:
                print(f"  ... and {expenses.count() - 5} more")
    except Exception as e:
        print(f"❌ Error checking expenses: {e}")
    
    # Check pocket money
    try:
        pocket_money = PocketMoney.objects.all()
        print(f"\n💵 Pocket Money Records: {pocket_money.count()}")
        if pocket_money.count() > 0:
            for pm in pocket_money[:3]:  # Show first 3
                print(f"  - {pm.amount} - {pm.date_received}")
            if pocket_money.count() > 3:
                print(f"  ... and {pocket_money.count() - 3} more")
    except Exception as e:
        print(f"❌ Error checking pocket money: {e}")
    
    print("\n" + "=" * 40)

if __name__ == '__main__':
    check_data() 