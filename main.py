import json
from dataclasses import dataclass
import dataclasses
import os
import uuid
import random
from faker import Faker


@dataclass
class Address:
    street_address: str
    city: str
    state: str
    zip_code: str

@dataclass
class Person:
    id: str
    name: str
    ssn: str
    age: int
    address: Address



# class EnhancedJSONEncoder(json.JSONEncoder):
#         def default(self, o):
#             if dataclasses.is_dataclass(o):
#                 return dataclasses.asdict(o)
#             return super().default(o)
# 

os.system("clear")
fake = Faker()

for i in range (3):
  x=Person(
     str(uuid.uuid4()),
        fake.last_name(),
        '000-00-0001',
        random.randint(10, 99),
        address = Address(
           '','','',''
                         )
        )
  j=json.dumps(dataclasses.asdict(x), indent=4)
  print(j)


