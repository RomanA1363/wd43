import numpy as np  
import pandas as pd 
import json
from datetime import date
#from tqdm.auto import tqdm
#tqdm.pandas()
# Python 3.10.9

from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
from fhir.resources.condition import Condition
from fhir.resources.observation import Observation
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.procedure import Procedure
from fhir.resources.encounter import Encounter
from fhir.resources.claim import Claim
from fhir.resources.immunization import Immunization

import os

# Define the path to the FHIR bundle JSON file
bundle_file_path = 'Historical/Parsing/source/Adolph80_Turcotte120_52b1b75f-2b8a-4319-9542-7abc39502cab.json'

# Create a directory to store the individual FHIR resources
output_directory = 'output_resources'
os.makedirs(output_directory, exist_ok=True)

# Load the FHIR bundle from the JSON file
with open(bundle_file_path, 'r') as bundle_file:
    bundle_data = json.load(bundle_file)

#print(bundle_data)    

# Create a FHIR Bundle resource from the JSON data

bundle = Bundle.parse_obj(bundle_data)

# Iterate through the entries in the bundle
for entry in bundle.entry:
    if entry.resource:
        resource = entry.resource
        # Generate a unique filename based on the resource type and ID
        resource_type = resource.resource_type
        resource_id = resource.id
        output_filename = f"{resource_type}_{resource_id}.json"

        # Write the individual FHIR resource to a separate file
        output_file_path = os.path.join(output_directory, output_filename)
        with open(output_file_path, 'w') as output_file:
            json.dump(resource.as_json(), output_file, indent=2)

        print(f"Split {resource_type} resource {resource_id} into {output_file_path}")
