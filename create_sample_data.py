#!/usr/bin/env python
"""
Script to create sample data that matches your original data.
This will help you manually recreate your expenses.
"""

import json
from datetime import datetime, date

def create_sample_data():
    """Create sample data based on your original data"""
    
    try:
        with open('local_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("📊 Your Original Data Summary:")
        print("=" * 50)
        
        # Count by type
        users = [item for item in data if item['model'] == 'auth.user']
        expenses = [item for item in data if item['model'] == 'expenses.expense']
        pocket_money = [item for item in data if item['model'] == 'expenses.pocketmoney']
        
        print(f"👤 Users: {len(users)}")
        print(f"💰 Expenses: {len(expenses)}")
        print(f"💵 Pocket Money Records: {len(pocket_money)}")
        
        print("\n📋 Sample Expenses to Add Manually:")
        print("=" * 50)
        
        # Show first 10 expenses
        for i, expense in enumerate(expenses[:10]):
            fields = expense['fields']
            print(f"{i+1}. Amount: ₹{fields['amount']}")
            print(f"   Category: {fields['category']}")
            print(f"   Date: {fields['date']}")
            print(f"   Note: {fields['note']}")
            print()
        
        if len(expenses) > 10:
            print(f"... and {len(expenses) - 10} more expenses")
        
        print("\n📋 Sample Pocket Money Records:")
        print("=" * 50)
        
        # Show pocket money records
        for i, pm in enumerate(pocket_money[:5]):
            fields = pm['fields']
            print(f"{i+1}. Amount: ₹{fields['amount']}")
            print(f"   Date: {fields['date_received']}")
            print(f"   Source: {fields.get('source', 'N/A')}")
            print()
        
        print("\n💡 Instructions:")
        print("1. Go to your app admin interface")
        print("2. Click on 'Expenses'")
        print("3. Click 'Add expense'")
        print("4. Add the expenses listed above")
        print("5. Do the same for Pocket Money records")
        
    except Exception as e:
        print(f"❌ Error reading data: {e}")

if __name__ == '__main__':
    create_sample_data() 