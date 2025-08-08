#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Only import data if we're using SQLite (development) or if explicitly requested
if [ "$DB_NAME" = "" ] && [ "$SKIP_DATA_IMPORT" != "true" ]; then
    # Import ALL original data for SamarthYR (only for SQLite/development)
    python manage.py import_all_data
fi 