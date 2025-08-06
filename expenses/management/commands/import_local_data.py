from django.core.management.base import BaseCommand
from django.core.management import call_command
import json
import os

class Command(BaseCommand):
    help = 'Import local data from JSON file'

    def handle(self, *args, **options):
        # Try to load data from the local_data.json file
        data_files = ['local_data.json', 'data_for_upload.json']
        
        for data_file in data_files:
            if os.path.exists(data_file):
                try:
                    self.stdout.write(f"📁 Found data file: {data_file}")
                    call_command('loaddata', data_file)
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Data imported successfully from {data_file}!')
                    )
                    
                    # Print summary
                    from django.contrib.auth.models import User
                    from expenses.models import Expense, PocketMoney
                    
                    users = User.objects.all()
                    expenses = Expense.objects.all()
                    pocket_money = PocketMoney.objects.all()
                    
                    self.stdout.write(f'\n📊 Import Summary:')
                    self.stdout.write(f'Users: {users.count()}')
                    self.stdout.write(f'Expenses: {expenses.count()}')
                    self.stdout.write(f'Pocket Money Records: {pocket_money.count()}')
                    
                    return
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'❌ Error importing from {data_file}: {str(e)}')
                    )
        
        self.stdout.write(
            self.style.WARNING('⚠️ No data files found to import')
        )
        self.stdout.write('Available files:')
        for file in os.listdir('.'):
            if file.endswith('.json'):
                self.stdout.write(f'  - {file}') 