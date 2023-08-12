
import random
import os
from datetime import datetime, timedelta

os.system("clear")

min_year=2023
max_year=datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)

for i in range(10):
    random_date = start + (end - start) * random.random()
    print(random_date)

#done

# or a function
def gen_datetime(min_year, max_year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

 
x
