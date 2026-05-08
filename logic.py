from PySide6.QtCore import QObject, Signal
import requests

class PokeLogic(QObject):
    dataLoaded = Signal(list)
    detailLoaded = Signal(dict)

    def __init__(self):
        super().__init__()

    def load_pokemon(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        data = requests.get(url).json()

        pokemon_list = []

        for index, p in enumerate(data["results"], start=1):
            pokemon_list.append({
                "name": p["name"].capitalize(),
                "id": index,
                "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{index}.png"
            })

        self.dataLoaded.emit(pokemon_list)

    def load_detail(self, pokemon_id):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        data = requests.get(url).json()

        detail = {
            "name": data["name"].capitalize(),
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }

        self.detailLoaded.emit(detail)