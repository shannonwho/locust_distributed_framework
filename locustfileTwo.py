from locust import HttpUser, User, TaskSet, task, web, runners, between, tag
# from locust.runners import MasterLocustRunner
from locust.contrib.fasthttp import FastHttpUser
from locust.stats import sort_stats
from locust.util.rounding import proper_round
# import json
from itertools import chain
try:
    # >= Py3.2
    from html import escape
except ImportError:
    # < Py3.2
    from cgi import escape
import simplejson as json
import os
import random
import string
import requests
from rejson import Client, Path
from utils.sampleJSON import smallObj,bigObj,hugeObj
from faker import Faker
from faker.providers import company
from flask import jsonify
from flask import request,Response
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import date
import enum
import uuid

#pull values from env vars
environment = os.environ['ENV']
# req_timeout_value = int(os.environ['LOAD_GEN_REQUEST_TIMEOUT']) if os.environ['LOAD_GEN_REQUEST_TIMEOUT'] else 50
api_endpoint = os.environ['API_ENDPOINT']

# https://faker.readthedocs.io/en/master/
fake = Faker()
fake.add_provider(company)


"""Functions for tasks to be used in the Task set"""

def get_id(pattern):
    #use scan on the key level 
    try:
        resp = requests.get(api_endpoint + 'keys?pattern=' + pattern, verify=False)
        r = resp.json()
        keys = r.get('json')
        return keys
    except Exception as e:
        return {'error':str(e)}

fields = ['id','name','address','location']
BasicUserTestSet = get_id('basicUser')
AdvancedUserTestSet = get_id('advancedUser')
hugeObjTestSet = get_id('redisJSON')
hugeObjFields = ['damage_relations', 'moves', 'pokemon']
stringTestSet = get_id('stringJSON')

class testOnRandomGet(TaskSet):
    """ task functions to be used in the TaskSet """
    @tag('getJsonByKey')
    @task(3)
    def get_json_by_key(self):
        self.client.get('/api/v1/doc/{}'.format(random.choice(AdvancedUserTestSet)), timeout=50, name='/api/v1/getJsonByKey')
        # self.client.cookies.clear()

    @tag('getField')
    # @task(3)
    def get_json_by_key_and_field(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(BasicUserTestSet), random.choice(fields)), timeout=50, name='/api/v1/getValueByKeyAndFields')
        # self.client.cookies.clear()

    @tag('getListOfFieldsByKey')
    #@task(3)
    def get_list_of_fields_by_key(self):
        self.client.get('/api/v1/fields/{}'.format(random.choice(AdvancedUserTestSet)), timeout=50, name='/api/v1/examples/getListOfFieldsByKey')

class testOnRandomJson(TaskSet):
    @tag('add_random_small_json')
    @task(3)
    def add_random_small_json(self):
        json_doc = {
            'id':   "basicUser:" + str(uuid.uuid4()),
            'name': fake.name(),
            'age': fake.random_int(min=0, max=100),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        json_doc = json.dumps(json_doc)

        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_small_json')
        # self.client.cookies.clear()
    
    @tag('add_random_big_json')
    @task(3)
    def add_random_big_json(self):
        nested_json = {
            'id': "advancedUser:" + str(uuid.uuid4()),
            'name': fake.name(),
            'activeStatus': False,
            'age': str(fake.random_int(min=0, max=100)),
            'contract':
                {
                    'name': fake.company(),
                    'occupation': 'Solution Architect',
                    'zipCode': "92603"
                },
            'location':[
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                },
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                },
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                }],
            'address': [
                fake.street_address(), 
                fake.street_address(), 
                fake.street_address()]
            }
        self.client.post('/api/v1/redisjson',
            data=json.dumps(nested_json,use_decimal=True),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_big_json')
        # self.client.cookies.clear()

    @tag('add_static_big_json')
    @task(3)
    def add_static_big_json(self):
        json_doc = json.dumps(bigObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_static_big_json')
        # self.client.cookies.clear()

class testOnPutRandom(TaskSet):
    @tag('updateField_json')
    #@task(2)
    def update_field(self):
        update = {
            'key': random.choice(AdvancedUserTestSet),
            'field': 'name',
            'str': 'Albert Z'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField')

    @tag('update_nested_field_json')
    @task(2)
    def update_field_nested(self):
        update = {
            'key': random.choice(AdvancedUserTestSet),
            'field': 'contract.name',
            'str': 'Redis Lab'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/update_field_nested')

    @tag('appendString')
    # @task(1)
    def append_string(self):
        append = {
            'key': random.choice(AdvancedUserTestSet),
            'field': 'name',
            'str': ' Hu'
        }
        self.client.put('/api/v1/redisjson/append',
            data=json.dumps(append),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/appendString')
        # self.client.cookies.clear()

    @tag('NumIncrby')
    @task(1)
    def num_incr_by(self):
        fieldNum = {
            'key': random.choice(BasicUserTestSet),
            'field': 'age',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/increby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numbIncryBy')
        # self.client.cookies.clear()

    @tag('NumMultiby')
    #@task(1)
    def num_multi_by(self):
        fieldNum = {
            'key': random.choice(BasicUserTestSet),
            'field': 'age',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/multiby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numMultiBy')
        # self.client.cookies.clear()

class simpleTest(TaskSet):
    @tag('simpleTest')
    @task(2)
    def simpleTest(self):
        self.client.get('/api/v1/hash/get',
            name='/api/v1/get')



""" Generate the load """

class GenerateLoad(FastHttpUser):
    # connection_timeout=100
    # network_timeout=50
    tasks = [simpleTest]
    # min_wait = 5000
    # max_wait = 20000

