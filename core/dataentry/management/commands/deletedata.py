from django.core.management.base import BaseCommand, CommandError
from ...models import CSVDate
from django.apps import apps





class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name you want remove data from.')
        
    
    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        
        model = None
        for app in apps.get_app_configs():
            try:
                model = apps.get_model(app.label, model_name)
                break
            except LookupError:
                continue
        
        if not model: 
            raise CommandError(f'The model "{model_name}" is not found in any app! ')
        else:
            count = model.objects.all().count()
            model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'The Model has {count} object and the data deleted successfully.'))
   
                
          