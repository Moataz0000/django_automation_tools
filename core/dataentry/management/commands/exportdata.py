import csv 
from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
import datetime
from django.apps import apps
from ...utils import generate_csv_file


# Propsed command --> python3 manage.py exportdata model_name


class Command(BaseCommand):
    help = 'Export data from database to a CSV file'
    
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name you want to export data from as CSV file.')

    
    
    def handle(self, *args ,**kwargs):
        # fetch the data from database
        model_name = kwargs['model_name']
        
        # search on the model in our app
        model = None
        for app in apps.get_app_configs():
            try:
                model = app.get_model(model_name)
                break
            except LookupError:
                pass
        
        if not model:
            raise CommandError(f'Model {model_name} is not found!')
            
        
        
        data = model.objects.all() 


        # generate csv file path
        file_path = generate_csv_file(model_name)

        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
 
            
            # write the CSV header
            writer.writerow([field.name for field in model._meta.fields])
            
            # write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS('Date Exported Successfully.'))    