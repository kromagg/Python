import json

file = 'season.json'
with open(file, 'w') as f:
    season = input("Enter the four seasons: ")
    json.dump(season, f)