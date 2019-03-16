import datetime
import json

import typesystem

# https://www.encode.io/typesystem/
# https://www.encode.io/typesystem/fields/

class Phone(typesystem.Schema):
	home = typesystem.String(max_length=100)
	office = typesystem.String(max_length=100)

class Person(typesystem.Schema):
    name = typesystem.String(max_length=100)
    gender = typesystem.Choice(choices=(("M", "Male"),("F", "Female")))
    age = typesystem.String(max_length=100)
    has_dues = typesystem.Boolean(default=False)
    address = typesystem.String(max_length=100)
    phone_no = typesystem.Reference(Phone)
    created_at = typesystem.Date(default=datetime.date.today)
    
person = Person.validate({
    "name": "Ankur Gupta",
    "gender": "M",
    "age": "36",
    "dues": False,
    "address": "Home Sweet Home.",
    "phone_no":{"home": "9020200202", "office":"39393993"},
})

print(person)

print(person.created_at)

print(person['created_at'])

print(dict(person))

schema = typesystem.to_json_schema(Person)
print(schema)