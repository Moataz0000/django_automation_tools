from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "Greets the user"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies username')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hi {name}, Good morning\n'
        self.stdout.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.WARNING(greeting))
        self.stderr.write('Type any message as error!')