import json
from dataclasses import dataclass, asdict
import dataclasses
import os
import uuid
import random
from faker import Faker
from typing import List
import fhir
from fhir.resources.patient import Patient
import orjson
import jsonpickle
from json import JSONEncoder
import time


start_time = time.time()
     
us_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]







patient = Patient()
patient.fhir_comments='this is the value of the data element fhir_comments'
patient.id=str(uuid.uuid4())

#patient.text=[{"status" : "generated", "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p style=\"border: 1px #661aff solid; background-color: #e6e6ff; padding: 10px;\"><b>Jim </b> male, DoB: 1974-12-25 ( Medical record number: 12345\u00a0(use:\u00a0USUAL,\u00a0period:\u00a02001-05-06 --&gt; (ongoing)))</p><hr/><table class=\"grid\"><tr><td style=\"background-color: #f3f5da\" title=\"Record is active\">Active:</td><td>true</td><td style=\"background-color: #f3f5da\" title=\"Known status of Patient\">Deceased:</td><td colspan=\"3\">false</td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Alternate names (see the one above)\">Alt Names:</td><td colspan=\"3\"><ul><li>Peter James Chalmers (OFFICIAL)</li><li>Peter James Windsor (MAIDEN)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Ways to contact the Patient\">Contact Details:</td><td colspan=\"3\"><ul><li>-unknown-(HOME)</li><li>ph: (03) 5555 6473(WORK)</li><li>ph: (03) 3410 5613(MOBILE)</li><li>ph: (03) 5555 8834(OLD)</li><li>534 Erewhon St PeasantVille, Rainbow, Vic  3999(HOME)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Nominated Contact: Next-of-Kin\">Next-of-Kin:</td><td colspan=\"3\"><ul><li>Bénédicte du Marché  (female)</li><li>534 Erewhon St PleasantVille Vic 3999 (HOME)</li><li><a href=\"tel:+33(237)998327\">+33 (237) 998327</a></li><li>Valid Period: 2012 --&gt; (ongoing)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Patient Links\">Links:</td><td colspan=\"3\"><ul><li>Managing Organization: <a href=\"organization-example-gastro.html\">Organization/1</a> &quot;Gastroenterology&quot;</li></ul></td></tr></table></div>"}]
patient.text='{"status":"generated", "div":"div"}'

patient.identifier = [{"system": "http://example.org/fhir/ids", "value": "14456464564646464646456462345"}]
patient.name = [{"use": "official", "family": "Doe", "given": ["John"]}]
patient.gender = "male"
patient.birthDate = "1970-01-01"
patient.telecom=[{"system": "email", "value": "123", "use": "work", "rank": "2"}]










#print(jsonpickle.encode(patient, unpicklable=False, make_refs=False, keys = False) )
out=jsonpickle.encode(patient, unpicklable=False, make_refs=False, keys = False)
with open('/Users/romankhmaladze/Documents/Websites/wd43/p.output.json', "w") as f:
    f.write(out)
print("--- %s seconds ---" % (time.time() - start_time))
