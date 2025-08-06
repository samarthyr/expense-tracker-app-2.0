from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
import json
import os

class Command(BaseCommand):
    help = 'Restore user data and create SamarthYR user'

    def handle(self, *args, **options):
        # Create SamarthYR user if it doesn't exist
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
                    self.style.SUCCESS('✅ User SamarthYR created successfully!')
                )
            else:
                # Update password if user exists
                user.set_password('admin@1234')
                user.save()
                self.stdout.write(
                    self.style.SUCCESS('✅ User SamarthYR password updated!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creating user: {str(e)}')
            )
        
        # Try to load data if the file exists
        data_file = 'data_for_upload.json'
        if os.path.exists(data_file):
            try:
                call_command('loaddata', data_file)
                self.stdout.write(
                    self.style.SUCCESS('✅ Data imported successfully!')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error importing data: {str(e)}')
                )
        else:
            self.stdout.write(
                self.style.WARNING('⚠️ No data file found to import')
            )
        
        # Print summary
        users = User.objects.all()
        self.stdout.write(f'\n📊 Summary:')
        self.stdout.write(f'Users: {users.count()}')
        
        # Check if expenses app is available
        try:
            from expenses.models import Expense, PocketMoney
            expenses = Expense.objects.all()
            pocket_money = PocketMoney.objects.all()
            self.stdout.write(f'Expenses: {expenses.count()}')
            self.stdout.write(f'Pocket Money Records: {pocket_money.count()}')
        except:
            self.stdout.write('Expenses app not available yet')
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Restoration complete! Login with:')
        )
        self.stdout.write('Username: SamarthYR')
        self.stdout.write('Password: admin@1234') 