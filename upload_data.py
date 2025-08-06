#!/usr/bin/env python
"""
Script to help restore data to the deployed app.
Run this locally to prepare the data for upload.
"""

import json

def prepare_data_for_upload():
    """Read the local data and prepare it for manual upload"""
    
    try:
        with open('local_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filter out the SamarthYR user (since we'll create it manually)
        filtered_data = []
        for item in data:
            if item['model'] == 'auth.user' and item['fields']['username'] == 'SamarthYR':
                continue  # Skip this user, we'll create it manually
            filtered_data.append(item)
        
        # Save filtered data
        with open('data_for_upload.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
        
        print("✅ Data prepared for upload!")
        print("📁 File 'data_for_upload.json' created")
        print("📊 Contains:")
        
        # Count items by type
        users = [item for item in filtered_data if item['model'] == 'auth.user']
        expenses = [item for item in filtered_data if item['model'] == 'expenses.expense']
        pocket_money = [item for item in filtered_data if item['model'] == 'expenses.pocketmoney']
        
        print(f"  - {len(users)} users (excluding SamarthYR)")
        print(f"  - {len(expenses)} expenses")
        print(f"  - {len(pocket_money)} pocket money records")
        
        print("\n📋 Next steps:")
        print("1. Upload 'data_for_upload.json' to your Render app")
        print("2. Run: python manage.py loaddata data_for_upload.json")
        print("3. Create SamarthYR user manually in admin")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    prepare_data_for_upload() 