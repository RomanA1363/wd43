import json, os

os.system("clear")




class FHIRPatient:
    def __init__(self):
        self.resourceType = "Patient"
        self.id = None
        self.identifier = []  # List of Identifier objects
        self.active = True
        self.name = []  # List of HumanName objects
        self.telecom = []  # List of ContactPoint objects
        self.gender = None
        self.birthDate = None
        self.address = []  # List of Address objects
        self.maritalStatus = None
        self.multipleBirthBoolean = None
        self.deceasedBoolean = None
        self.generalPractitioner = []  # List of Reference objects (Practitioner)
        self.managingOrganization = None  # Reference object (Organization)

class Identifier:
    def __init__(self):
        self.use = None
        self.system = None
        self.value = None

class HumanName:
    def __init__(self):
        self.use = None
        self.text = None
        self.family = None
        self.given = []  # List of given names
        self.prefix = []  # List of name prefixes
        self.suffix = []  # List of name suffixes

class ContactPoint:
    def __init__(self):
        self.system = None  # phone | fax | email | pager | other
        self.value = None
        self.use = None  # home | work | temp | old | mobile
        self.rank = None  # int
        self.period = None  # Period object

class Address:
    def __init__(self):
        self.use = None  # home | work | temp | old
        self.type = None  # postal | physical | both
        self.text = None
        self.line = []  # List of address lines
        self.city = None
        self.district = None
        self.state = None
        self.postalCode = None
        self.country = None

class Reference:
    def __init__(self):
        self.reference = None  # Reference URL
        self.display = None  # Display name for the referenced resource



telecom = [
    {
        "system": "phone",
        "value": "555-333-3344",
        "use": "home",
        "rank": "1",  
        "period" : {
            "start":"2023-01-01", 
                    "end":"2023-08-01"
                    }
    },
    {
        "system": "email",
        "value": "johndoe@example.com",
        "use": "work",
        "rank": "2",
         "period" : {
             "start":"2023-02-04", 
                     "end":"2023-04-06"
                     }
    }
]


a1=Address()
a1.city='Westminster'

a2=Address()
a2.city='Owings Mills'

a3=Address()
a3.city='Annapolis'

p=FHIRPatient()
p.name='Roman'
p.deceasedBoolean=True
p.gender='M'
p.telecom=telecom
p.address=[a1,a2,a3]



#https://sparkbyexamples.com/python/print-object-properties-and-values-in-python/#:~:text=You%20can%20use%20the%20python,in%20a%20human%2Dreadable%20format.
#https://json-generator.com
# Method 1: Using vars() mixed with pprint()
#obj_vars = vars(p)
#print(obj_vars)

# Method 2: Using dir()
for attr in dir(p):
    print(f"{attr}: {getattr(p, attr)}")

# Print the JSON representation of the FHIR Patient resource
#print(json.dumps(p, default=str))

for x in range(len(p.address)):
    print (p.address[x].city)
