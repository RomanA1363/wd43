import random
from faker import Faker
import json
import itertools


def generate_ccd(plt):   
  fake = Faker()
  
  SendingOrg = ['Sending Organization 1','Sending Organization 2','Sending Organization 3','Sending Organization 4','Sending Organization 5'] 
  us_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]


  out = {
      "authorInstitution": ''+random.choice(SendingOrg)+'',
      "custodian": {
           "name": ''+fake.company()+'',
           "phone": ''+fake.phone_number()+'',
           "streetAddressLine": ''+fake.street_address()+'',
           "city": ''+fake.city()+'',
           "state": ''+random.choice(us_states)+'',
           "postalCode": ''+fake.postcode()+'',
           "country": "USA"
      }
  }

  if plt == 'CCD': 
     out
  else :
     out="None" 
  return out


# def steps():
#   data='{'
#   for i in range(random.randint(1, 5)): 
#    data=data+'x'
#   data=data+'}'
#   return data




data_dict = {"first_photo" : "PHOTO_1", "second_photo" : "PHOTO_2", "Thrid" : "PHOTO_3"}
result = {"Requests":[]}

for pair in sorted(itertools.permutations(data_dict.values(), 2)):
    result["Requests"].append({"photo":{"photoId":{"id": pair[0]},
                                        "connections":{"target":{"id": pair[1]}}},"updateData": "connections"})

print(json.dumps(result, indent=4))




#print(json.dumps(steps(), indent=4))
#print(steps())

