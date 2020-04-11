import json

def input_restaurant():
    with open("bot/restaurant.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data