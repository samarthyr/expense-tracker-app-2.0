#!/usr/bin/env python
"""
Script to check database tables and data
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

from django.db import connection
from expenses.models import Expense, PocketMoney

def check_database():
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("✅ Database connection successful!")
            print(f"Database engine: {settings.DATABASES['default']['ENGINE']}")
            print(f"Database name: {settings.DATABASES['default']['NAME']}")
            
            # Check if tables exist
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cursor.fetchall()
            print(f"\n📋 Database tables:")
            for table in tables:
                print(f"  - {table[0]}")
            
            # Check expense count
            try:
                expense_count = Expense.objects.count()
                print(f"\n💰 Total expenses: {expense_count}")
                
                if expense_count > 0:
                    latest_expense = Expense.objects.latest('date')
                    print(f"📅 Latest expense: {latest_expense.description} on {latest_expense.date}")
            except Exception as e:
                print(f"⚠️  Could not check expenses: {e}")
            
            # Check pocket money count
            try:
                pocket_money_count = PocketMoney.objects.count()
                print(f"💵 Total pocket money entries: {pocket_money_count}")
            except Exception as e:
                print(f"⚠️  Could not check pocket money: {e}")
                
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

if __name__ == "__main__":
    check_database()
