# trying classes here

from faker import Faker
import os
import random
import uuid

adt_hl7_types = ["ADT_A01", "ADT_A02", "ADT_A03", "ADT_A04", "ADT_A05", "ADT_A06", "ADT_A08", "ADT_A12", "ADT_A15", "ADT_A16"]


class Telemetry:
  def __init__(self, 
               name, 
               age, 
               doctor, 
               disease,
               root_id
               ):
    self.name = name
    self.age = age
    self.doctor = doctor
    self.disease = disease
    self.root_id = root_id

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_doctor(self):
    return self.doctor

  def get_disease(self):
    return self.disease
  
  def get_root_id(self):
    return self.root_id
  
os.system("clear")
fake = Faker()
for i in range(3):  

 file = Telemetry(fake.first_name(), random.randint(25, 99), "Dr."+fake.last_name(), random.choice(adt_hl7_types), str(uuid.uuid4()))
 print(file.get_name())
 print(file.get_age())
 print(file.get_doctor())
 print(file.get_disease())
 print(file.get_root_id())
 print('___________________')



