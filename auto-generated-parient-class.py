from typing import List
from typing import Any
from dataclasses import dataclass
import json
import pandas

@dataclass
class Telecom:
    system: str
    value: str
    use: str

    @staticmethod
    def from_dict(obj: Any) -> 'Telecom':
        _system = str(obj.get("system"))
        _value = str(obj.get("value"))
        _use = str(obj.get("use"))
        return Telecom(_system, _value, _use)

@dataclass
class Address:
    use: str
    type: str
    line: List[str]
    city: str
    state: str
    postalCode: str

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _use = str(obj.get("use"))
        _type = str(obj.get("type"))
        _line = [from_dict(y) for y in obj.get("line")]
        _city = str(obj.get("city"))
        _state = str(obj.get("state"))
        _postalCode = str(obj.get("postalCode"))
        return Address(_use, _type, _line, _city, _state, _postalCode)

@dataclass
class Coding:
    system: str
    code: str
    display: str

    @staticmethod
    def from_dict(obj: Any) -> 'Coding':
        _system = str(obj.get("system"))
        _code = str(obj.get("code"))
        _display = str(obj.get("display"))
        return Coding(_system, _code, _display)
    

@dataclass
class Relationship:
    coding: List[Coding]
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Relationship':
        _coding = [Coding.from_dict(y) for y in obj.get("coding")]
        _text = str(obj.get("text"))
        return Relationship(_coding, _text)    

@dataclass
class Contact:
    relationship: List[Relationship]
    name: str
    telecom: List[Telecom]

    @staticmethod
    def from_dict(obj: Any) -> 'Contact':
        _relationship = [Relationship.from_dict(y) for y in obj.get("relationship")]
        _name = Name.from_dict(obj.get("name"))
        _telecom = [Telecom.from_dict(y) for y in obj.get("telecom")]
        return Contact(_relationship, _name, _telecom)

@dataclass
class Identifier:
    system: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Identifier':
        _system = str(obj.get("system"))
        _value = str(obj.get("value"))
        return Identifier(_system, _value)

@dataclass
class MaritalStatus:
    coding: List[Coding]

    @staticmethod
    def from_dict(obj: Any) -> 'MaritalStatus':
        _coding = [Coding.from_dict(y) for y in obj.get("coding")]
        return MaritalStatus(_coding)

@dataclass
class Name:
    use: str
    family: str
    given: List[str]
    prefix: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        _use = str(obj.get("use"))
        _family = str(obj.get("family"))
        _given = [from_dict(y) for y in obj.get("given")]
        _prefix = [from_dict(y) for y in obj.get("prefix")]
        return Name(_use, _family, _given, _prefix)



@dataclass
class Root:
    resourceType: str
    id: str
    identifier: List[Identifier]
    active: bool
    name: List[Name]
    telecom: List[Telecom]
    gender: str
    birthDate: str
    address: List[Address]
    maritalStatus: MaritalStatus
    contact: List[Contact]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _resourceType = str(obj.get("resourceType"))
        _id = str(obj.get("id"))
        _identifier = [Identifier.from_dict(y) for y in obj.get("identifier")]
        _active = ''
        _name = [Name.from_dict(y) for y in obj.get("name")]
        _telecom = [Telecom.from_dict(y) for y in obj.get("telecom")]
        _gender = str(obj.get("gender"))
        _birthDate = str(obj.get("birthDate"))
        _address = [Address.from_dict(y) for y in obj.get("address")]
        _maritalStatus = MaritalStatus.from_dict(obj.get("maritalStatus"))
        _contact = [Contact.from_dict(y) for y in obj.get("contact")]
        return Root(_resourceType, _id, _identifier, _active, _name, _telecom, _gender, _birthDate, _address, _maritalStatus, _contact)



# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

root=Root(
resourceType='Patient',
id= 'my id',
identifier=['1','2','3'],
active= True,
name= ['name 1','name 2'],
telecom= ['phone1','email 1'],
gender= 'M',
birthDate= '2003-10-01',
address=['address 1','address 2'],
maritalStatus= 'never married',
contact=['contact 1', 'contact 2']
)

print(root)


