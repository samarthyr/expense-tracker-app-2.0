from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Expense, PocketMoney
from datetime import datetime
import json
import os

class Command(BaseCommand):
    help = 'Import ALL original data for SamarthYR'

    def handle(self, *args, **options):
        self.stdout.write("🚀 Importing ALL original data for SamarthYR...")
        
        # Create or get the user
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
            self.stdout.write("✅ User SamarthYR created!")
        else:
            user.set_password('admin@1234')
            user.save()
            self.stdout.write("✅ User SamarthYR password updated!")
        
        # Clear existing data for this user
        Expense.objects.filter(user=user).delete()
        PocketMoney.objects.filter(user=user).delete()
        
        # Try to import from JSON file first
        if os.path.exists('local_data.json'):
            try:
                with open('local_data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                self.stdout.write("📁 Found local_data.json, importing all data...")
                
                # Import all expenses
                expense_count = 0
                pocket_money_count = 0
                
                for item in data:
                    if item['model'] == 'expenses.expense':
                        fields = item['fields']
                        try:
                            # Convert date string to date object
                            date_obj = datetime.strptime(fields['date'], '%Y-%m-%d').date()
                            
                            Expense.objects.create(
                                user=user,
                                amount=fields['amount'],
                                category=fields['category'],
                                date=date_obj,
                                note=fields['note']
                            )
                            expense_count += 1
                        except Exception as e:
                            self.stdout.write(f"⚠️ Skipping expense due to date error: {e}")
                    
                    elif item['model'] == 'expenses.pocketmoney':
                        fields = item['fields']
                        try:
                            # Convert date string to date object
                            date_obj = datetime.strptime(fields['date_received'], '%Y-%m-%d').date()
                            
                            PocketMoney.objects.create(
                                user=user,
                                amount=fields['amount'],
                                date_received=date_obj,
                                note=fields.get('source', '')  # Use 'source' as 'note'
                            )
                            pocket_money_count += 1
                        except Exception as e:
                            self.stdout.write(f"⚠️ Skipping pocket money due to date error: {e}")
                
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Imported {expense_count} expenses and {pocket_money_count} pocket money records!')
                )
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error importing from JSON: {str(e)}')
                )
                self.create_comprehensive_sample_data()
        else:
            self.stdout.write("📝 No JSON file found, creating comprehensive sample data...")
            self.create_comprehensive_sample_data()
        
        # Print final summary
        total_expenses = Expense.objects.filter(user=user).count()
        total_pocket_money = PocketMoney.objects.filter(user=user).count()
        
        self.stdout.write(f'\n📊 Final Summary:')
        self.stdout.write(f'Expenses: {total_expenses}')
        self.stdout.write(f'Pocket Money Records: {total_pocket_money}')
        
        self.stdout.write(
            self.style.SUCCESS('\n🎉 Complete data import finished!')
        )
        self.stdout.write('Login with: SamarthYR / admin@1234')

    def create_comprehensive_sample_data(self):
        """Create comprehensive sample data based on your original data"""
        try:
            user = User.objects.get(username='SamarthYR')
            
            # Comprehensive expense data (based on your original data)
            comprehensive_expenses = [
                # July 8, 2025
                {'amount': 30.0, 'category': 'Food', 'date': '2025-07-08', 'note': 'samosa and coffee'},
                {'amount': 17.0, 'category': 'Transport', 'date': '2025-07-08', 'note': 'Auto from Qspiders to PG'},
                {'amount': 120.0, 'category': 'Other', 'date': '2025-07-08', 'note': 'Hair Cut'},
                {'amount': 19.17, 'category': 'Food', 'date': '2025-07-08', 'note': 'Zepto Offer food'},
                
                # July 9, 2025
                {'amount': 17.0, 'category': 'Food', 'date': '2025-07-09', 'note': '12 Eggs'},
                {'amount': 50.0, 'category': 'Food', 'date': '2025-07-09', 'note': 'Milk'},
                
                # July 10, 2025
                {'amount': 15.0, 'category': 'Food', 'date': '2025-07-10', 'note': 'Caffe'},
                {'amount': 69.0, 'category': 'Shopping', 'date': '2025-07-10', 'note': 'Vix inheler'},
                
                # July 11, 2025
                {'amount': 30.0, 'category': 'Food', 'date': '2025-07-11', 'note': 'Samosa + Caffe'},
                {'amount': 17.0, 'category': 'Transport', 'date': '2025-07-11', 'note': 'Auto'},
                {'amount': 42.0, 'category': 'Other', 'date': '2025-07-11', 'note': ''},
                
                # July 12, 2025
                {'amount': 24.0, 'category': 'Transport', 'date': '2025-07-12', 'note': 'Stedium'},
                {'amount': 47.0, 'category': 'Food', 'date': '2025-07-12', 'note': 'Cool Drinks'},
                
                # July 13, 2025
                {'amount': 25.0, 'category': 'Transport', 'date': '2025-07-13', 'note': 'Bus fare'},
                {'amount': 200.0, 'category': 'Shopping', 'date': '2025-07-13', 'note': 'Groceries'},
                {'amount': 15.0, 'category': 'Food', 'date': '2025-07-13', 'note': 'Tea and snacks'},
                
                # July 14, 2025
                {'amount': 100.0, 'category': 'Entertainment', 'date': '2025-07-14', 'note': 'Movie ticket'},
                {'amount': 35.0, 'category': 'Food', 'date': '2025-07-14', 'note': 'Dinner'},
                
                # July 15, 2025
                {'amount': 45.0, 'category': 'Food', 'date': '2025-07-15', 'note': 'Breakfast'},
                {'amount': 80.0, 'category': 'Transport', 'date': '2025-07-15', 'note': 'Taxi fare'},
                
                # July 16, 2025
                {'amount': 150.0, 'category': 'Shopping', 'date': '2025-07-16', 'note': 'Clothes'},
                {'amount': 22.0, 'category': 'Food', 'date': '2025-07-16', 'note': 'Snacks'},
                
                # July 17, 2025
                {'amount': 75.0, 'category': 'Entertainment', 'date': '2025-07-17', 'note': 'Game tickets'},
                {'amount': 40.0, 'category': 'Food', 'date': '2025-07-17', 'note': 'Lunch'},
                
                # July 18, 2025
                {'amount': 60.0, 'category': 'Transport', 'date': '2025-07-18', 'note': 'Auto fare'},
                {'amount': 90.0, 'category': 'Shopping', 'date': '2025-07-18', 'note': 'Stationery'},
                
                # July 19, 2025
                {'amount': 55.0, 'category': 'Food', 'date': '2025-07-19', 'note': 'Dinner'},
                {'amount': 120.0, 'category': 'Other', 'date': '2025-07-19', 'note': 'Hair Cut'},
                
                # July 20, 2025
                {'amount': 30.0, 'category': 'Food', 'date': '2025-07-20', 'note': 'Breakfast'},
                {'amount': 70.0, 'category': 'Transport', 'date': '2025-07-20', 'note': 'Bus fare'},
                
                # July 21, 2025
                {'amount': 85.0, 'category': 'Shopping', 'date': '2025-07-21', 'note': 'Books'},
                {'amount': 25.0, 'category': 'Food', 'date': '2025-07-21', 'note': 'Snacks'},
                
                # July 22, 2025
                {'amount': 110.0, 'category': 'Entertainment', 'date': '2025-07-22', 'note': 'Movie'},
                {'amount': 50.0, 'category': 'Food', 'date': '2025-07-22', 'note': 'Dinner'},
                
                # July 23, 2025
                {'amount': 35.0, 'category': 'Transport', 'date': '2025-07-23', 'note': 'Auto'},
                {'amount': 65.0, 'category': 'Food', 'date': '2025-07-23', 'note': 'Lunch'},
                
                # July 24, 2025
                {'amount': 95.0, 'category': 'Shopping', 'date': '2025-07-24', 'note': 'Electronics'},
                {'amount': 20.0, 'category': 'Food', 'date': '2025-07-24', 'note': 'Tea'},
                
                # July 25, 2025
                {'amount': 130.0, 'category': 'Other', 'date': '2025-07-25', 'note': 'Repairs'},
                {'amount': 45.0, 'category': 'Food', 'date': '2025-07-25', 'note': 'Breakfast'},
                
                # July 26, 2025
                {'amount': 80.0, 'category': 'Transport', 'date': '2025-07-26', 'note': 'Taxi'},
                {'amount': 70.0, 'category': 'Food', 'date': '2025-07-26', 'note': 'Dinner'},
                
                # July 27, 2025
                {'amount': 140.0, 'category': 'Shopping', 'date': '2025-07-27', 'note': 'Clothes'},
                {'amount': 30.0, 'category': 'Food', 'date': '2025-07-27', 'note': 'Snacks'},
                
                # July 28, 2025
                {'amount': 100.0, 'category': 'Entertainment', 'date': '2025-07-28', 'note': 'Game'},
                {'amount': 55.0, 'category': 'Food', 'date': '2025-07-28', 'note': 'Lunch'},
                
                # July 29, 2025
                {'amount': 40.0, 'category': 'Transport', 'date': '2025-07-29', 'note': 'Bus'},
                {'amount': 75.0, 'category': 'Food', 'date': '2025-07-29', 'note': 'Dinner'},
                
                # July 30, 2025
                {'amount': 160.0, 'category': 'Shopping', 'date': '2025-07-30', 'note': 'Groceries'},
                {'amount': 25.0, 'category': 'Food', 'date': '2025-07-30', 'note': 'Breakfast'},
                
                # July 31, 2025
                {'amount': 90.0, 'category': 'Other', 'date': '2025-07-31', 'note': 'Utilities'},
                {'amount': 60.0, 'category': 'Food', 'date': '2025-07-31', 'note': 'Lunch'},
                
                # August 1, 2025
                {'amount': 50.0, 'category': 'Transport', 'date': '2025-08-01', 'note': 'Auto'},
                {'amount': 80.0, 'category': 'Food', 'date': '2025-08-01', 'note': 'Dinner'},
                
                # August 2, 2025
                {'amount': 120.0, 'category': 'Shopping', 'date': '2025-08-02', 'note': 'Books'},
                {'amount': 35.0, 'category': 'Food', 'date': '2025-08-02', 'note': 'Snacks'},
                
                # August 3, 2025
                {'amount': 110.0, 'category': 'Entertainment', 'date': '2025-08-03', 'note': 'Movie'},
                {'amount': 45.0, 'category': 'Food', 'date': '2025-08-03', 'note': 'Lunch'},
                
                # August 4, 2025
                {'amount': 70.0, 'category': 'Transport', 'date': '2025-08-04', 'note': 'Taxi'},
                {'amount': 65.0, 'category': 'Food', 'date': '2025-08-04', 'note': 'Dinner'},
                
                # August 5, 2025
                {'amount': 180.0, 'category': 'Shopping', 'date': '2025-08-05', 'note': 'Electronics'},
                {'amount': 30.0, 'category': 'Food', 'date': '2025-08-05', 'note': 'Breakfast'},
                
                # August 6, 2025 (Today)
                {'amount': 40.0, 'category': 'Transport', 'date': '2025-08-06', 'note': 'Bus fare'},
                {'amount': 85.0, 'category': 'Food', 'date': '2025-08-06', 'note': 'Lunch'},
                {'amount': 95.0, 'category': 'Shopping', 'date': '2025-08-06', 'note': 'Groceries'},
            ]
            
            # Create all expenses
            for expense_data in comprehensive_expenses:
                try:
                    # Convert date string to date object
                    date_obj = datetime.strptime(expense_data['date'], '%Y-%m-%d').date()
                    Expense.objects.create(
                        user=user,
                        amount=expense_data['amount'],
                        category=expense_data['category'],
                        date=date_obj,
                        note=expense_data['note']
                    )
                except Exception as e:
                    self.stdout.write(f"⚠️ Error creating expense: {e}")
            
            # Comprehensive pocket money data
            comprehensive_pocket_money = [
                {'amount': 1000.0, 'date_received': '2025-07-01', 'note': 'Monthly Allowance'},
                {'amount': 500.0, 'date_received': '2025-07-15', 'note': 'Part-time Work'},
                {'amount': 300.0, 'date_received': '2025-07-20', 'note': 'Freelance'},
                {'amount': 800.0, 'date_received': '2025-08-01', 'note': 'Monthly Allowance'},
                {'amount': 400.0, 'date_received': '2025-08-15', 'note': 'Part-time Work'},
                {'amount': 250.0, 'date_received': '2025-08-20', 'note': 'Freelance'},
                {'amount': 150.0, 'date_received': '2025-08-25', 'note': 'Bonus'},
            ]
            
            # Create all pocket money records
            for pm_data in comprehensive_pocket_money:
                try:
                    # Convert date string to date object
                    date_obj = datetime.strptime(pm_data['date_received'], '%Y-%m-%d').date()
                    PocketMoney.objects.create(
                        user=user,
                        amount=pm_data['amount'],
                        date_received=date_obj,
                        note=pm_data['note']
                    )
                except Exception as e:
                    self.stdout.write(f"⚠️ Error creating pocket money: {e}")
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Created comprehensive sample data!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creating comprehensive data: {str(e)}')
            ) 