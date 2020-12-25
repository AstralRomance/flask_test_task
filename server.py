import os
import json

from flask import Flask, request
from flask import jsonify, abort, make_response
import numpy as np

from Distance import Distance

app = Flask(__name__)
distance_matrix = Distance()

@app.route('/', methods=['GET'])
def path_find_service():
    # REPLACE API TOKEN TO ENV VARIABLE
    if int(request.headers['X-API-KEY']) != int(os.environ.get('TEST_API_TOKEN')):
        abort(404, description={'body': 'invalid token'})
    try:
        data = json.loads(request.data)
    except json.JSONDecodeError:
        abort(501, jsonify({'body': 'Cant decode json input'}))
    try:
        if data['city_start'] == data['city_finish']:
            abort (404, description = {'body': 'no road. Start is equal to finish'})
        if (data['city_start'] < 0) or (data['city_finish'] < 0):
            abort (404, description = {'body': 'invalid input. Number lesser than 0'})
        if isinstance(data['city_start'], float) or isinstance(data['city_finish'], float):
            abort(404, jsonify({'input': data, 'body': 'invalid input. Number is not int'}))
    except KeyError:
        abort(404, description = {'body': 'invalid input'})
    valid_response = {'body':distance_matrix.length_find(data['city_start'], data['city_finish'])}
    if valid_response['body']['distance'] == 0:
        abort(jsonify({'input': input_data, 'body': 'invalid input. Number is not int'}))
    return jsonify(valid_response)


if __name__ == '__main__':
    app.run()
