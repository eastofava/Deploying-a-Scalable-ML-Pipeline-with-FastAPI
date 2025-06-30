import requests

# Sending GET request
r = requests.get("http://127.0.0.1:8000")

# Printing status code and welcome message
print("GET status code:", r.status_code)
print("GET response:", r.json())

# Preparing data for POST
data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Sending POST request
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# Printing status code and result
print("POST status code:", r.status_code)

print("POST resonse:", r.json())
