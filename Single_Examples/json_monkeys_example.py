import json

file = 'json_monkeys.json'
try:
    with open(file, 'r') as f:
        dzo = json.load(f)
        print(f"Monkeys on the bed: {dzo}")
except FileNotFoundError:
    dzongkhag = input("Enter the names of all the monkeys on the bed:")
    with open(file, 'w') as f:
        json.dump(dzongkhag, f)