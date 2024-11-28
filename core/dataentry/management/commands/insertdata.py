from django.core.management.base import BaseCommand
from ...models import Student





class Command(BaseCommand):
    help = "It will insert data to the database"
    
    """
    Add some data to the database using the custom command
    """
    
    
    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': '1002', 'name': 'Doe', 'age': 21},
            {'roll_no': '1003', 'name': 'John', 'age': 23},
            {'roll_no': '1004', 'name': 'Mike', 'age': 25},
            {'roll_no': '1005', 'name': 'Joseph', 'age': 22},

        ]
        
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_record: 
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
                self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))

            else:
                self.stdout.write(self.style.WARNING(f'Student with roll number {roll_no} already exists!\n'))
 
