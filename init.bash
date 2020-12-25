#!/bin/bash

python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
TEST_API_TOKEN=$1 python server.py
