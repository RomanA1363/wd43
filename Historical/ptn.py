import json
from fhir.resources.patient import Patient

patient = Patient()
patient.identifier = [{"system": "http://example.org/fhir/ids", "value": "12345"}]
patient.name = [{"use": "official", "family": "Doe", "given": ["John"]}]
patient.gender = "male"
patient.birthDate = "1970-01-01"

#json_data = json.dumps(patient)

patient.birthDate

print(patient.birthDate)