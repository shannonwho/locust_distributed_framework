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

# Scrape data into Prometheus
import six
from itertools import chain
from locust import stats as locust_stats, runners as locust_runners
from locust import User, task, events
from prometheus_client import Metric, REGISTRY, exposition

# This locustfile adds an external web endpoint to the locust master, and makes it serve as a prometheus exporter.
class LocustPrometheusCollector(object):
    registry = REGISTRY

    def __init__(self, environment, runner):
        self.environment = environment
        self.runner = runner

    def collect(self):
        # collect metrics only when locust runner is spawning or running.
        runner = self.runner

        if runner and runner.state in (locust_runners.STATE_SPAWNING, locust_runners.STATE_RUNNING):
            stats = []
            for s in chain(locust_stats.sort_stats(runner.stats.entries), [runner.stats.total]):
                stats.append({
                    "method": s.method,
                    "name": s.name,
                    "num_requests": s.num_requests,
                    "num_failures": s.num_failures,
                    "avg_response_time": s.avg_response_time,
                    "min_response_time": s.min_response_time or 0,
                    "max_response_time": s.max_response_time,
                    "current_rps": s.current_rps,
                    "median_response_time": s.median_response_time,
                    "ninetieth_response_time": s.get_response_time_percentile(0.9),
                    # only total stats can use current_response_time
                    #"current_response_time_percentile_95": s.get_current_response_time_percentile(0.95),
                    "avg_content_length": s.avg_content_length,
                    "current_fail_per_sec": s.current_fail_per_sec
                })

            # perhaps StatsError.parse_error in e.to_dict only works in python slave, take notices!
            errors = [e.to_dict() for e in six.itervalues(runner.stats.errors)]

            metric = Metric('locust_user_count', 'Swarmed users', 'gauge')
            metric.add_sample('locust_user_count', value=runner.user_count, labels={})
            yield metric
            
            metric = Metric('locust_errors', 'Locust requests errors', 'gauge')
            for err in errors:
                metric.add_sample('locust_errors', value=err['occurrences'],
                                  labels={'path': err['name'], 'method': err['method'],
                                          'error': err['error']})
            yield metric

            is_distributed = isinstance(runner, locust_runners.MasterRunner)
            if is_distributed:
                metric = Metric('locust_slave_count', 'Locust number of slaves', 'gauge')
                metric.add_sample('locust_slave_count', value=len(runner.clients.values()), labels={})
                yield metric

            metric = Metric('locust_fail_ratio', 'Locust failure ratio', 'gauge')
            metric.add_sample('locust_fail_ratio', value=runner.stats.total.fail_ratio, labels={})
            yield metric

            metric = Metric('locust_state', 'State of the locust swarm', 'gauge')
            metric.add_sample('locust_state', value=1, labels={'state': runner.state})
            yield metric

            stats_metrics = ['avg_content_length', 'avg_response_time', 'current_rps', 'current_fail_per_sec',
                             'max_response_time', 'ninetieth_response_time', 'median_response_time', 'min_response_time',
                             'num_failures', 'num_requests']

            for mtr in stats_metrics:
                mtype = 'gauge'
                if mtr in ['num_requests', 'num_failures']:
                    mtype = 'counter'
                metric = Metric('locust_stats_' + mtr, 'Locust stats ' + mtr, mtype)
                for stat in stats:
                    # Aggregated stat's method label is None, so name it as Aggregated
                    # locust has changed name Total to Aggregated since 0.12.1
                    if 'Aggregated' != stat['name']:
                        metric.add_sample('locust_stats_' + mtr, value=stat[mtr],
                                          labels={'path': stat['name'], 'method': stat['method']})
                    else:
                        metric.add_sample('locust_stats_' + mtr, value=stat[mtr],
                                          labels={'path': stat['name'], 'method': 'Aggregated'})
                yield metric


@events.init.add_listener
def locust_init(environment, runner, **kwargs):
    print("locust init event received")
    if environment.web_ui and runner:
        @environment.web_ui.app.route("/metrics")
        def prometheus_exporter():
            registry = REGISTRY
            encoder, content_type = exposition.choose_encoder(request.headers.get('Accept'))
            if 'name[]' in request.args:
                registry = REGISTRY.restricted_registry(request.args.get('name[]'))
            body = encoder(registry)
            return Response(body, content_type=content_type)
        REGISTRY.register(LocustPrometheusCollector(environment, runner))


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
hugeObjFields = ['damage_relations', 'move_damage_class', 'pokemon']
stringTestSet = get_id('stringJSON')
nestedFields = ['damage_relations.double_damage_from[0].name', 'names[0].language.name']

""" Build the TaskSet """
class testOnJSONSet(TaskSet):
    @tag('add_string')
    @task(3)
    def add_json_string(self):
        json_doc = json.dumps(hugeObj)
        self.client.post('/api/v1/string',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_string')

    @tag('add_json')
    @task(3)
    def add_json(self):
        json_doc = json.dumps(hugeObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_json')


class testOnJSONGet(TaskSet):
    @tag('get_string')
    @task(2)
    def get_string(self):        
        self.client.get('/api/v1/string/{}'.format(random.choice(stringTestSet)), timeout=50, name='/api/v1/get_string')

    @tag('get_json')
    @task(2)
    def get_json(self):
        self.client.get('/api/v1/doc/{}'.format(random.choice(hugeObjTestSet)), timeout=50, name='/api/v1/get_json')
        # self.client.cookies.clear()


class testOnChangeJSON(TaskSet):
    @tag('updateField_json')
    @task(2)
    def updateField_json(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'generation',
            'str': 'generation-X'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_json')


    @tag('updateField_string')
    @task(2)
    def updateField_string(self):
        update = {
            'key': random.choice(stringTestSet),
            'field': 'generation',
            'str': 'generation-X'
        }
        self.client.put('/api/v1/string/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_string')

    @tag('update_nested_Field_json')
    @task(2)
    def update_nested_Field_json(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'damage_relations.double_damage_from[0].name',
            'str': 'lightening'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/update_nested_Field_json')

    @tag('json_append_string')
    #@task(2)
    def json_append_string(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'damage_relations.double_damage_from[0].name',
            'str': ' & Jumping'}

        self.client.put('/api/v1/redisjson/append',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/json_append_string')


    @tag('NumIncrby')
    @task(1)
    ##json.numincrby hugeObj:5eb32da6-f48c-4263-9a96-013ded607f52 pokemon[0].slot 1
    def num_incr_by(self):
        fieldNum = {
            'key': random.choice(hugeObjTestSet),
            'field': 'pokemon[0].slot',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/increby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numbIncryBy')

class moreJSONTest(TaskSet):
    @tag('get_json_by_key_and_field')
    @task(2)
    def get_json_by_key_and_field(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(hugeObjTestSet), random.choice(hugeObjFields)), timeout=50, name='/api/v1/get_json_by_key_and_field')
        # self.client.cookies.clear()


    @tag('get_string_by_key_and_field')
    @task(2)
    def get_string_by_key_and_field(self):
        self.client.get('/api/v1/string/{}/{}'.format(random.choice(stringTestSet), random.choice(hugeObjFields)), timeout=50, name='/api/v1/get_string_by_key_and_field')
        # self.client.cookies.clear()

    @tag('get_nested_json_by_key_and_field')
    @task(2)
    def get_json(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(hugeObjTestSet), random.choice(nestedFields)), timeout=50, name='/api/v1/get_nested_json')
        # self.client.cookies.clear()
    



""" Generate the load """

class GenerateLoad(FastHttpUser):
    # connection_timeout=100
    # network_timeout=50
    tasks = [testOnChangeJSON]
    # min_wait = 5000
    # max_wait = 20000

