#!/usr/bin/env python
"""
Script to migrate data from SQLite to PostgreSQL
"""
import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from expenses.models import Expense, PocketMoney
from django.contrib.auth.models import User
from decouple import config

def migrate_data():
    print("🔄 Starting data migration from SQLite to PostgreSQL...")
    
    # Check if we're using PostgreSQL
    if 'postgresql' not in settings.DATABASES['default']['ENGINE']:
        print("❌ Not using PostgreSQL. Please set up PostgreSQL environment variables first.")
        return
    
    # Check if data already exists in PostgreSQL
    expense_count = Expense.objects.count()
    pocket_money_count = PocketMoney.objects.count()
    user_count = User.objects.count()
    
    print(f"📊 Current PostgreSQL data:")
    print(f"  - Users: {user_count}")
    print(f"  - Expenses: {expense_count}")
    print(f"  - Pocket Money entries: {pocket_money_count}")
    
    if expense_count > 0 or pocket_money_count > 0:
        print("⚠️  PostgreSQL already has data. Skipping migration.")
        return
    
    # Try to import from the data file
    try:
        print("📥 Importing data from data_for_upload.json...")
        from django.core.management import call_command
        call_command('import_all_data')
        print("✅ Data import completed!")
        
        # Show final counts
        final_expense_count = Expense.objects.count()
        final_pocket_money_count = PocketMoney.objects.count()
        final_user_count = User.objects.count()
        
        print(f"📊 Final PostgreSQL data:")
        print(f"  - Users: {final_user_count}")
        print(f"  - Expenses: {final_expense_count}")
        print(f"  - Pocket Money entries: {final_pocket_money_count}")
        
    except Exception as e:
        print(f"❌ Error importing data: {e}")
        print("💡 You can manually import data using:")
        print("   python manage.py import_all_data")

if __name__ == "__main__":
    migrate_data()
