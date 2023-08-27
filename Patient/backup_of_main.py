# started on 2023-08-23
# 19 classes allocated

from datetime import datetime
from typing import Union, Optional, List
import os
import uuid
import random
import lorem


class AddressPeriod:
    start: Union[datetime, int]

    def __init__(self, start: Union[datetime, int]) -> None:
        self.start = start


class Address:
    use: str
    type: str
    text: Optional[str]
    line: List[str]
    city: str
    district: str
    state: str
    postal_code: int
    period: AddressPeriod

    def __init__(self, use: str, type: str, text: Optional[str], line: List[str], city: str, district: str, state: str, postal_code: int, period: AddressPeriod) -> None:
        self.use = use
        self.type = type
        self.text = text
        self.line = line
        self.city = city
        self.district = district
        self.state = state
        self.postal_code = postal_code
        self.period = period


class BirthDateExtension:
    url: str
    value_date_time: datetime

    def __init__(self, url: str, value_date_time: datetime) -> None:
        self.url = url
        self.value_date_time = value_date_time


class BirthDate:
    extension: List[BirthDateExtension]

    def __init__(self, extension: List[BirthDateExtension]) -> None:
        self.extension = extension


class FamilyExtension:
    url: str
    value_string: str

    def __init__(self, url: str, value_string: str) -> None:
        self.url = url
        self.value_string = value_string


class Family:
    extension: List[FamilyExtension]

    def __init__(self, extension: List[FamilyExtension]) -> None:
        self.extension = extension


class ContactName:
    name_family: str
    family: Family
    given: List[str]

    def __init__(self, name_family: str, family: Family, given: List[str]) -> None:
        self.name_family = name_family
        self.family = family
        self.given = given


class Coding:
    system: str
    code: str

    def __init__(self, system: str, code: str) -> None:
        self.system = system
        self.code = code


class TypeElement:
    coding: List[Coding]

    def __init__(self, coding: List[Coding]) -> None:
        self.coding = coding


class ContactTelecom:
    system: str
    value: str

    def __init__(self, system: str, value: str) -> None:
        self.system = system
        self.value = value


class Contact:
    relationship: List[TypeElement]
    name: ContactName
    telecom: List[ContactTelecom]
    address: Address
    gender: str
    period: AddressPeriod

    def __init__(self, relationship: List[TypeElement], name: ContactName, telecom: List[ContactTelecom], address: Address, gender: str, period: AddressPeriod) -> None:
        self.relationship = relationship
        self.name = name
        self.telecom = telecom
        self.address = address
        self.gender = gender
        self.period = period


class Assigner:
    display: str

    def __init__(self, display: str) -> None:
        self.display = display


class Identifier:
    use: str
    type: TypeElement
    system: str
    value: int
    period: AddressPeriod
    assigner: Assigner

    def __init__(self, use: str, type: TypeElement, system: str, value: int, period: AddressPeriod, assigner: Assigner) -> None:
        self.use = use
        self.type = type
        self.system = system
        self.value = value
        self.period = period
        self.assigner = assigner


class ManagingOrganization:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference


class NamePeriod:
    end: int

    def __init__(self, end: int) -> None:
        self.end = end


class NameElement:
    use: str
    family: Optional[str]
    given: List[str]
    period: Optional[NamePeriod]

    def __init__(self, use: str, family: Optional[str], given: List[str], period: Optional[NamePeriod]) -> None:
        self.use = use
        self.family = family
        self.given = given
        self.period = period


class PatientTelecom:
    use: str
    system: Optional[str]
    value: Optional[str]
    rank: Optional[int]
    period: Optional[NamePeriod]

    def __init__(self, use: str, system: Optional[str], value: Optional[str], rank: Optional[int], period: Optional[NamePeriod]) -> None:
        self.use = use
        self.system = system
        self.value = value
        self.rank = rank
        self.period = period


class Text:
    status: str
    div: str

    def __init__(self, status: str, div: str) -> None:
        self.status = status
        self.div = div


class Patient:
    resource_type: str
    id: str
    text: Text
    identifier: List[Identifier]
    active: bool
    name: List[NameElement]
    telecom: List[PatientTelecom]
    gender: str
    Patient_birth_date: datetime
    birth_date: BirthDate
    deceased_boolean: bool
    address: List[Address]
    contact: List[Contact]
    managing_organization: ManagingOrganization

    def __init__(self, resource_type: str, id: str, text: Text, identifier: List[Identifier], active: bool, name: List[NameElement], telecom: List[PatientTelecom], gender: str, Patient_birth_date: datetime, birth_date: BirthDate, deceased_boolean: bool, address: List[Address], contact: List[Contact], managing_organization: ManagingOrganization) -> None:
        self.resource_type = resource_type
        self.id = id
        self.text = text
        self.identifier = identifier
        self.active = active
        self.name = name
        self.telecom = telecom
        self.gender = gender
        self.Patient_birth_date = Patient_birth_date
        self.birth_date = birth_date
        self.deceased_boolean = deceased_boolean
        self.address = address
        self.contact = contact
        self.managing_organization = managing_organization


# trying to work with this class ----------------------------------------------------------------------------------------
# https://jsonformatter.org/json-to-python#Sample
# https://validator.fhir.org
# https://fshschool.org/FSHOnline/#/share/3LH920m
# http://build.fhir.org/ig/HL7/fhir-shorthand/

os.system("clear")

# functions
def generate_random_guids():
    return [str(uuid.uuid4()) for _ in range(random.randint(1, 3))]

def generate_random_guid():
    return [str(uuid.uuid4()) for _ in range(1)]


# initializing other classes


p=Patient(
    resource_type = 'Patient',
    id = generate_random_guid(),
    text = lorem.sentence(),
    identifier = generate_random_guids(),
    active = True,
    name = [],
    telecom = [],
    gender = 'M',
    Patient_birth_date = '1967-01-01',
    birth_date = '1967-01-01',
    deceased_boolean = False,
    address = [],
    contact = [],
    managing_organization = []
    )







#for x in range(len(p.identifier)):
    #print (p.identifier[x])

for key, value in vars(p).items():
    print(f"{key}: {value}")


