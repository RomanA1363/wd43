import random
from faker import Faker



def generate_ccd(length): 
  
  fake = Faker()

  SendingOrg = ['Sending Organization 1','Sending Organization 2','Sending Organization 3','Sending Organization 4','Sending Organization 5'] 
  us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia"]

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


  return out

