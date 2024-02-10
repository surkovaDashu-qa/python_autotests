import requests
import pytest
    
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '14aaf57fe7f3f1b8f57b9bf9f5f8833c'}

def test_get_status_code():
  
    response = requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
   

def test_get_name():
  
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': '3681'}, headers=HEADER, timeout=5)
    assert response != response.json()['trainer_name'] == 'Toka'
    
