from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from expenses.models import Expense, PocketMoney
import json
import os

class Command(BaseCommand):
    help = 'Quick import all data from JSON files'

    def handle(self, *args, **options):
        self.stdout.write("🚀 Starting quick data import...")
        
        # First, create the SamarthYR user
        try:
            user, created = User.objects.get_or_create(
                username='SamarthYR',
                defaults={
                    'email': 'samarthyr@gmail.com',
                    'first_name': 'SAMARTH',
                    'last_name': 'Y R',
                    'is_staff': True,
                    'is_superuser': True,
                }
            )
            
            if created:
                user.set_password('admin@1234')
                user.save()
                self.stdout.write(
                    self.style.SUCCESS('✅ User SamarthYR created!')
                )
            else:
                user.set_password('admin@1234')
                user.save()
                self.stdout.write(
                    self.style.SUCCESS('✅ User SamarthYR password updated!')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creating user: {str(e)}')
            )
        
        # Try to import data from JSON files
        data_files = ['local_data.json', 'data_for_upload.json']
        
        for data_file in data_files:
            if os.path.exists(data_file):
                try:
                    self.stdout.write(f"📁 Importing from {data_file}...")
                    call_command('loaddata', data_file)
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Data imported from {data_file}!')
                    )
                    break  # Stop after first successful import
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'❌ Error importing from {data_file}: {str(e)}')
                    )
        
        # If no JSON files found, create sample data
        if not any(os.path.exists(f) for f in data_files):
            self.stdout.write("📝 Creating sample data...")
            self.create_sample_data()
        
        # Print final summary
        self.print_summary()
        
        self.stdout.write(
            self.style.SUCCESS('\n🎉 Quick import complete!')
        )
        self.stdout.write('Login with: SamarthYR / admin@1234')

    def create_sample_data(self):
        """Create sample expense data"""
        try:
            # Get the SamarthYR user
            user = User.objects.get(username='SamarthYR')
            
            # Sample expenses
            sample_expenses = [
                {'amount': 30.0, 'category': 'Food', 'date': '2025-07-08', 'note': 'samosa and coffee'},
                {'amount': 17.0, 'category': 'Transport', 'date': '2025-07-08', 'note': 'Auto from Qspiders to PG'},
                {'amount': 120.0, 'category': 'Other', 'date': '2025-07-08', 'note': 'Hair Cut'},
                {'amount': 19.17, 'category': 'Food', 'date': '2025-07-08', 'note': 'Zepto Offer food'},
                {'amount': 50.0, 'category': 'Food', 'date': '2025-07-09', 'note': 'Lunch'},
                {'amount': 25.0, 'category': 'Transport', 'date': '2025-07-09', 'note': 'Bus fare'},
                {'amount': 200.0, 'category': 'Shopping', 'date': '2025-07-10', 'note': 'Groceries'},
                {'amount': 15.0, 'category': 'Food', 'date': '2025-07-10', 'note': 'Tea and snacks'},
                {'amount': 100.0, 'category': 'Entertainment', 'date': '2025-07-11', 'note': 'Movie ticket'},
                {'amount': 35.0, 'category': 'Food', 'date': '2025-07-11', 'note': 'Dinner'},
            ]
            
            # Create expenses
            for expense_data in sample_expenses:
                Expense.objects.create(
                    user=user,
                    **expense_data
                )
            
            # Sample pocket money
            sample_pocket_money = [
                {'amount': 1000.0, 'date_received': '2025-07-01', 'source': 'Monthly Allowance'},
                {'amount': 500.0, 'date_received': '2025-07-15', 'source': 'Part-time Work'},
            ]
            
            # Create pocket money records
            for pm_data in sample_pocket_money:
                PocketMoney.objects.create(
                    user=user,
                    **pm_data
                )
            
            self.stdout.write(
                self.style.SUCCESS('✅ Sample data created successfully!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creating sample data: {str(e)}')
            )

    def print_summary(self):
        """Print summary of current data"""
        try:
            users = User.objects.all()
            expenses = Expense.objects.all()
            pocket_money = PocketMoney.objects.all()
            
            self.stdout.write(f'\n📊 Final Summary:')
            self.stdout.write(f'Users: {users.count()}')
            self.stdout.write(f'Expenses: {expenses.count()}')
            self.stdout.write(f'Pocket Money Records: {pocket_money.count()}')
            
            if expenses.count() > 0:
                self.stdout.write(f'\n💰 Recent Expenses:')
                for expense in expenses[:5]:
                    self.stdout.write(f'  - ₹{expense.amount} ({expense.category}) - {expense.date}')
            
        except Exception as e:
            self.stdout.write(f'❌ Error printing summary: {str(e)}') 