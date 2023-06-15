# Diccionarios
# { "key": "value", "key": "value" }

team = {
    "name": "City",
    "country": "England",
    "champions": 1,
    "players": ['Halland', 'Grealinsh']
}

print(type(team))
print(team)
print(team["name"])
print(team["players"])
team["players"].append("Kevin")
team["name"] = "Manchester City"
team["leage"] = "Premerie league"
print(team)
