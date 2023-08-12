import os
import uuid
import random
from datetime import datetime, timedelta




# or a function
def gen_datetime(min_year, max_year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


os.system("clear")
telemetry = {
  "id": uuid.uuid4(),
  "transaction_dts": gen_datetime(2023, 2023),
  "age": 300,
  "skills": ["coding", "language modeling", "natural language processing"]
}
telemetry['age']=1555
#print(ts)
for key, value in telemetry.items():
  print(key, value)