#!/usr/bin/env python
import os
import sys
import django
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command
from expenses.models import Expense, PocketMoney

def restore_data():
    # First, load the data from JSON
    try:
        call_command('loaddata', 'local_data.json')
        print("✅ Data loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return
    
    # Now update the password for SamarthYR
    try:
        user = User.objects.get(username='SamarthYR')
        user.set_password('admin@1234')
        user.save()
        print("✅ Password updated for SamarthYR to 'admin@1234'")
    except User.DoesNotExist:
        print("❌ User SamarthYR not found")
    except Exception as e:
        print(f"❌ Error updating password: {e}")
    
    # Print summary
    users = User.objects.all()
    expenses = Expense.objects.all()
    pocket_money = PocketMoney.objects.all()
    
    print(f"\n📊 Data Summary:")
    print(f"Users: {users.count()}")
    print(f"Expenses: {expenses.count()}")
    print(f"Pocket Money Records: {pocket_money.count()}")
    
    print(f"\n👤 Users:")
    for user in users:
        print(f"  - {user.username} ({user.email})")
    
    print(f"\n✅ Restoration complete! You can now login with:")
    print(f"   Username: SamarthYR")
    print(f"   Password: admin@1234")

if __name__ == '__main__':
    restore_data() 