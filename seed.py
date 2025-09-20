from faker import Faker
fake=Faker()
import random
from .models import *

def student_marks_create(n):
     students=Student.objects.all()
     for student in students:
          subjects=Subject.objects.all()
          for subject in subjects:
               Student_marks.objects.create(
                   student=student,
                   subject=subject,
                   marks=random.randint(0,100)
                

               )
          
def seed_db(n=10) ->None:
    for i in range(n):
         dep_obj=Department.objects.all()
         rand_indx=random.randint(0,len(dep_obj)-1)
         department=dep_obj[rand_indx]
         
         student_id=f'STU={random.randint(50,100)}'
         student_name=fake.name()
         student_email=fake.email()
         student_age=random.randint(20,25)
         student_address=fake.address()

         student_id_obj=Student_id.objects.create(student_id=student_id)

         student_obj=Student.objects.create(
               
         
              student_name=student_name,
              student_email=student_email,
              student_age=student_age,
              student_address=student_address,
              student_id=student_id_obj,
              department=department,

         )