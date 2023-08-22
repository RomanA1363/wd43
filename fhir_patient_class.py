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






a1=Address()
a1.city='Westminster'

a2=Address()
a2.city='Owings Mills'

p=FHIRPatient()
p.name='Roman'
p.address=[a1,a2]




print(p.address)
