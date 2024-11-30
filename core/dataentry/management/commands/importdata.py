from django.core.management.base import BaseCommand, CommandError
from ...models import Student, CSVDate
import csv
from django.apps import apps
from django.db import DataError


# Proposed command - python manage.py importdata file_path model_name



class Command(BaseCommand):
    help = "Import data from CSV file to the model"
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Model name you want add data in')
        
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        # search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue # model not found in this app, countinue searching in next app
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
                
        # get all the field name of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id'] 
        print(model_fields)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file) # return every line in the csv file as a dict
            csv_header = reader.fieldnames
            # compare csv header with model's field names
            if csv_header != model_fields:
                raise DataError(f'CSV file\'s data doesn\'t match with the model {model_name} table fields.')
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully!'))

    