from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Expense, PocketMoney
from datetime import date

class Command(BaseCommand):
    help = 'Create sample data for SamarthYR'

    def handle(self, *args, **options):
        self.stdout.write("🚀 Creating sample data for SamarthYR...")
        
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
        
        # Create sample expenses (based on your original data)
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
            {'amount': 45.0, 'category': 'Food', 'date': '2025-07-12', 'note': 'Breakfast'},
            {'amount': 80.0, 'category': 'Transport', 'date': '2025-07-12', 'note': 'Taxi fare'},
            {'amount': 150.0, 'category': 'Shopping', 'date': '2025-07-13', 'note': 'Clothes'},
            {'amount': 22.0, 'category': 'Food', 'date': '2025-07-13', 'note': 'Snacks'},
            {'amount': 75.0, 'category': 'Entertainment', 'date': '2025-07-14', 'note': 'Game tickets'},
        ]
        
        # Create expenses
        for expense_data in sample_expenses:
            Expense.objects.create(user=user, **expense_data)
        
        # Create pocket money records
        sample_pocket_money = [
            {'amount': 1000.0, 'date_received': '2025-07-01', 'source': 'Monthly Allowance'},
            {'amount': 500.0, 'date_received': '2025-07-15', 'source': 'Part-time Work'},
            {'amount': 300.0, 'date_received': '2025-07-20', 'source': 'Freelance'},
        ]
        
        for pm_data in sample_pocket_money:
            PocketMoney.objects.create(user=user, **pm_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Created {len(sample_expenses)} expenses and {len(sample_pocket_money)} pocket money records!')
        )
        
        # Print summary
        total_expenses = Expense.objects.filter(user=user).count()
        total_pocket_money = PocketMoney.objects.filter(user=user).count()
        
        self.stdout.write(f'\n📊 Summary:')
        self.stdout.write(f'Expenses: {total_expenses}')
        self.stdout.write(f'Pocket Money Records: {total_pocket_money}')
        
        self.stdout.write(
            self.style.SUCCESS('\n🎉 Data creation complete!')
        )
        self.stdout.write('Login with: SamarthYR / admin@1234') 