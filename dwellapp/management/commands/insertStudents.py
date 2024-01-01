# myapp/management/commands/insert_students.py
from django.core.management.base import BaseCommand
from dwellapp.models import Student, Address
import json

class Command(BaseCommand):
    help = 'Insert students data into the database'

    def handle(self, *args, **options):
        students_data = {
            "student8": {
            "full_name": "Liam Garcia",
            "first_name": "Liam",
            "last_name": "Garcia",
            "age": 16,
            "date_of_birth": "2007-02-14",
            "address": {
                "street": "456 Pine Street",
                "city": "Lakeview",
                "state": "FL",
                "zip_code": "34567"
            },
            "student_class": "10th Grade",
            "grade": "B",
            "subjects": [
                "Math",
                "Chemistry",
                "History"
            ]
        },
        "student9": {
            "full_name": "Ava Thompson",
            "first_name": "Ava",
            "last_name": "Thompson",
            "age": 18,
            "date_of_birth": "2005-12-05",
            "address": {
                "street": "789 Elm Avenue",
                "city": "Riverdale",
                "state": "GA",
                "zip_code": "45678"
            },
            "student_class": "12th Grade",
            "grade": "A-",
            "subjects": [
                "Biology",
                "Literature",
                "Art"
            ]
        },
        "student10": {
            "full_name": "Noah Hernandez",
            "first_name": "Noah",
            "last_name": "Hernandez",
            "age": 17,
            "date_of_birth": "2006-05-20",
            "address": {
                "street": "1010 Oak Street",
                "city": "Sunnyville",
                "state": "CA",
                "zip_code": "56789"
            },
            "student_class": "11th Grade",
            "grade": "B+",
            "subjects": [
                "Computer Science",
                "Geography",
                "Physical Education"
            ]
        }
        }

        for student_key, student_data in students_data.items():
            address_data = student_data.pop('address')
            address = Address.objects.create(**address_data)
            student_data['address'] = address
            Student.objects.create(**student_data)
            
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
