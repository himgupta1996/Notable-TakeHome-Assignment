import requests
import json

def test_get_index():
    response = requests.get('http://127.0.0.1:5000/')
    print("I am here")
    print(response.__dict__)

    assert response.status_code == 200

def test_post_index():
    response = requests.post('http://127.0.0.1:5000/', json = {'firstname': 'Medha', 'lastname': 'Katehara', 'email': 'mk@gmail.com'})
    print("I am here")
    print(response.__dict__)

    assert response.status_code == 200
    # assert response.data.decode('utf-8') == 'Testing, Flask!'