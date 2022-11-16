#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests

if !argv[1]:
    q=""
else:
    q=argv[1]

req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
try:
    json_response = req.json()
    id = json_response.get('id')
    name = json_response.get('name')
    if len(json_response) == 0 or not id or not name:
        print("No result")
    else:
        print("[{}] {}".format(id, name)
except:
    print("Not a valid JSON")
