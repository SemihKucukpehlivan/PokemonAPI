import requests
import json

pokemon_id = input("Please Enter Pokemon Id: ")
def main():
    req = requests.get(f'http://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("Pokemon Name: " + json_response['name'])

if __name__ == '__main__':
    main()