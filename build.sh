#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Import data if PostgreSQL is empty or if we're using SQLite
if [ "$DB_NAME" = "" ]; then
    # Import ALL original data for SamarthYR (only for SQLite/development)
    python manage.py import_all_data
else
    # For PostgreSQL, check if data exists and import if empty
    python manage.py shell -c "
from expenses.models import Expense, PocketMoney
from django.contrib.auth.models import User

# Create admin user
try:
    admin_user, created = User.objects.get_or_create(
        username='SamarthYR',
        defaults={
            'email': 'samarth@example.com',
            'first_name': 'Samarth',
            'last_name': 'YR',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        admin_user.set_password('admin@1234')
        admin_user.save()
        print('✅ Admin user SamarthYR created successfully!')
    else:
        admin_user.set_password('admin@1234')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print('✅ Admin user SamarthYR password updated!')
except Exception as e:
    print(f'❌ Error creating admin user: {e}')

# Import data if empty
if Expense.objects.count() == 0 and PocketMoney.objects.count() == 0:
    print('No data found in PostgreSQL, importing sample data...')
    from django.core.management import call_command
    call_command('import_all_data')
    print('Data import completed!')
else:
    print('PostgreSQL already has data, skipping import.')
"
fi 