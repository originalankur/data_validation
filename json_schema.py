from jsonschema import validate

# https: //json-schema.org/understanding-json-schema/index.html
# https: //python-jsonschema.readthedocs.io/en/stable/

schema = {
    "properties": {
        "name": {
            "type": "string",
            "minLength": 2,
            "maxLength": 400
        },
        "gender": {
            "type": "string",
            "enum": [
                "Male",
                "Female",
                "Other"
            ]
        },
        "age": {
            "type": "number",
            "minimum": 18,
            "maximum": 126
        },
        "dues": {
            "type": "number"
        },
        "address": {
            "type": "string",
            "minLength": 0,
            "maxLength": 1000
        },
        "phones": {
            "properties": {
                "home": {
                    "type": "string"
                },
                "office": {
                    "type": "string"
                }
            },

        },

    },
}

post_data = {
    "name": "Ankur Gupta",
    "age": 36,
    "gender": "Male",
    "dues": 29.83,
    "address": "Home sweet Home",
    "phones": {
        "home": "9099999999",
        "office": "3838383838"
    }
}

validate(post_data, schema)