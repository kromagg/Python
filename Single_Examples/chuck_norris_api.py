import requests

response = requests.get('https://api.chucknorris.io/jokes/random')

# # raw response
# print(response)

# print(type(response.json()))
print("*** RAW ***")
print(response.json())


print()
print("*** PRETTY ***")
dict_obj = response.json()
# for key,value in dict_obj.items():
#     print('{} = {}'.format(key,value))
print("Here it goes: " + dict_obj['value'])


