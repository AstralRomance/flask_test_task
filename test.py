import json
import pytest
import requests

def request_form(token, start, finish, url='http://127.0.0.1:5000'):
    headers={'X-API-KEY': token}
    data = {'city_start': start, 'city_finish': finish}
    test_request = requests.get(url=url, data=json.dumps(data), headers=headers)
    return test_request

def test_token():
    test_request = request_form('123', 2, 5)
    assert test_request.status_code == 404

def test_equal_target():
    test_request = request_form('123321', 2, 2)
    assert test_request.status_code == 404

def test_negative_target():
    test_request = request_form('123321', -2, 5)
    assert test_request.status_code == 404

def test_float_target():
    test_request = request_form('123321', 2.5, 5)
    assert test_request.status_code == 404

def test_valid_response():
    test_request = request_form('123321', 3, 5)
    print(test_request.json())
    assert (test_request.status_code != 404)

def test_valid_data_format():
    test_request = request_form('123321', 3, 5)
    response_data = test_request.json()
    assert ('path' in response_data['body']) and ('distance' in response_data['body'])

def test_valid_data_types():
    test_request = request_form('123321', 3, 5)
    response_data = test_request.json()
    assert (isinstance(response_data['body']['distance'], int)) and (isinstance(response_data['body']['path'], list))
