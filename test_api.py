import requests

def select_pet(pet_id, pet_json):
    print ("select_pet starting")
    get_response = requests.get('https://petstore.swagger.io/v2/pet/'+str(pet_id))
    pet_json_2 = get_response.json()
    print(str(pet_json_2))
    assert get_response.status_code == 200
    assert get_response.headers['content-type'] in "application/json"
    get_response.headers
    if sorted(pet_json.items()) == sorted(pet_json_2.items()):
        print ("Jsons are same.")
    else:
        print ("Jsons are not same.")
    return pet_json_2["id"]

def delete_pet_with_id(pet_id):
    print ("Deleting Pet")
    get_response = requests.delete('https://petstore.swagger.io/v2/pet/'+str(pet_id))
    pet_selected_pet = get_response.json()
    print(str(pet_selected_pet))
    assert get_response.status_code == 200
    assert get_response.headers['content-type'] in "application/json"
    if get_response.headers['date']:
        print ("Date: "+get_response.headers['date'])
    else:
        print ("Response does not have date value.")
    assert pet_selected_pet["message"] in str(pet_id)
    assert pet_selected_pet["type"] in "unknown"

def create_pet():
    data = {
        "category": {
        "id": 0,
        "name": "Pets"
        },
        "name": "MES",
        "photoUrls": [
        "MES.png"
        ],
        "tags": [
        {
        "id": 0,
        "name": "MES"
        }
        ],
        "status": "available"
    }
    get_response = requests.post('https://petstore.swagger.io/v2/pet', json=data)
    
    assert get_response.status_code == 200
    assert get_response.headers['content-type'] in "application/json"
    
    if get_response.headers['date']:
        print ("Date: "+get_response.headers['date'])
    else:
        print ("Response does not have date value.")

    pet = get_response.json()
    if pet["id"]:
        print ("ID: "+str(pet["id"]))
    else :
        print ("ID could not found.")

    assert pet["name"] in "testMES"

    print(str(pet))
    return pet["id"], pet
    

def test_pet_api():
    pet_id, pet_json1 = create_pet()
    pet_id = select_pet(pet_id, pet_json1)
    delete_pet_with_id(pet_id)