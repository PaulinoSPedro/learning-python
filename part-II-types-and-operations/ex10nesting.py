data_info = {
    "name":[
        {
        "first": "John",
        "middle": "Super",
        "last": "Doe"
        }
    ],
    "job": "Software Engineer",
    "address": [
            ("Information, 15 Street - WorldEarth")
    ],
    "email": "email@test.com",
    "phone": 9913214231
}

print(data_info["name"])
print(data_info["name"][0]["first"], end=" ")
print(data_info["name"][0]["middle"], end=" ")
print(data_info["name"][0]["last"])
print(data_info["job"])
print(data_info["address"][0])
print(data_info["email"])
print(data_info["phone"])
