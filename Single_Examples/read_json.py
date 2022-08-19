import json

with open('season.json', 'r') as f:
    season = json.load(f)
    print(f"Four seasons are: {season}")