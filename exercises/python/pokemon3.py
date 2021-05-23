import json

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

grass_type_pokemon = [
  pokemon for pokemon in pokemons if "grass" in pokemon["type"]
]

with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dump(grass_type_pokemon)
    file.write(json_to_write)
