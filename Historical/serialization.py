import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            # Define how to serialize the Person object
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

# Create an instance of the class
person = Person("John Doe", 30)

# Serialize the instance to JSON using the custom encoder
json_data = json.dumps(person, cls=PersonEncoder, indent=4)

# Print the JSON data
print(json_data)
