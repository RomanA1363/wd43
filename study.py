import os
import uuid
import random
import json
from datetime import datetime, timedelta
from faker import Faker

# https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html


os.system("clear")

SendingOrg = ['Sending Organization 1','Sending Organization 2','Sending Organization 3','Sending Organization 4','Sending Organization 5']
ReceivingOrg = ['Receiving Organization 1','Receiving Organization 2','Receiving Organization 3','Receiving Organization 4','Receiving Organization 5']
CommPoint = ['Comm Point 1','Comm Point  2','Comm Point  3','Comm Point  4','Comm Point  5']
PayloadType = ['HL7','CCDA','FHIR','CSV']
verato_exception = ['','','','','','','exception 1','','','','','','','','','','','','','','','','','','','','','exception 2','','','','','','','','','',]

adt_hl7_types = ["ADT_A01", "ADT_A02", "ADT_A03", "ADT_A04", "ADT_A05", "ADT_A06", "ADT_A08", "ADT_A12", "ADT_A15", "ADT_A16"]
gender = ['M','F']
TF = ['T','F']
medical_facilities_types = ["ER", "Hospital", "Clinic", "Ambulance", "Urgent Care", "Doctor's Office", "Dentist's Office", "Optometrist's Office", "Pharmacy", "Physical Therapy Clinic", "Mental Health Clinic"]

# generate random dts in a range
def gen_datetime(min_year, max_year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

# generate random string of the desire lenght
def generate_random_alphanumeric_string(length):
  characters = "abcdefghijklmnopqrstuvwxyz0123456789".upper()
  random_string = ""
  for _ in range(length):
    random_character = random.choice(characters)
    random_string += random_character
  return random_string

fake = Faker()

telemetry = {
  "root_id": ''+str(uuid.uuid4())+'',
  "verato_id": ''+str(uuid.uuid4())+'',
  "msh_7": ''+str(gen_datetime(2023, 2023))+'',
  "msh_4": ''+random.choice(SendingOrg)+'', # MSH.4 - Sending Facility
  "msh_6": ''+random.choice(ReceivingOrg)+'', #  MSH.6 - Receiving Facility
  "msh_9_1": "ADT",
  "msh_9_2": ''+random.choice(adt_hl7_types)+'',
  "msh_10": ''+generate_random_alphanumeric_string(15)+'',
  "msh_22_10 ": ''+ generate_random_alphanumeric_string(15)+'',
  "pv1_3_4 ": ''+random.choice(medical_facilities_types)+'',
  "pid_3_1 ": ''+generate_random_alphanumeric_string(15)+'',
  "pid_5_1": ''+fake.last_name()+'',
  "pid_5_2": ''+fake.first_name()+'',
  "pid_7": ''+fake.date()+'',
  "pid_19 ": ''+fake.ssn()+'',
  "pid_8": ''+random.choice(gender)+'',
  "obr_2": ''+generate_random_alphanumeric_string(10)+'',
  "obr_3": ''+generate_random_alphanumeric_string(10)+'',
  "obr_24": ''+generate_random_alphanumeric_string(10)+'',
  "Part2": ''+random.choice(TF)+'',
  "SDOH": ''+random.choice(TF)+'',
  "inbound_comm_point": ''+random.choice(CommPoint)+'',
  "verato_exception": ''+random.choice(verato_exception)+'',
  "original_file_name": ''+str(uuid.uuid4())+'.hl7',
  "archived_file_name": ''+str(uuid.uuid4())+'',
  "payload_type": ''+random.choice(PayloadType)+''
}



print(json.dumps(telemetry))
print('--------------------------------------------------------------------------------------------------------------------------------------------')
for key, value in telemetry.items():
  print(key, value)

