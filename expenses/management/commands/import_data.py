from django.core.management.base import BaseCommand
from django.core.management import call_command
import json
import os

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        if not os.path.exists(json_file):
            self.stdout.write(
                self.style.ERROR(f'File {json_file} does not exist')
            )
            return
        
        try:
            # Load the JSON data
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Import the data
            call_command('loaddata', json_file)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully imported data from {json_file}')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            ) 