from django.core.management.base import BaseCommand,CommandError
from django.apps import apps



class Command(BaseCommand):
    help = 'Show count of objects model'
    
    
    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='model name')
        
        
    
    def handle(self, *args, **options):
        model_name = options['model'] 
        
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue # model not found in this app, countinue searching in next app
        
        if not model:
            raise CommandError(f'Model "{model}" not found in any app!')
        objects = model.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Model objects count is: "{objects}" '))   