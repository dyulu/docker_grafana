#!/usr/bin/python3

import os
import json
import requests

grafana_host = 'localhost'
grafana_port = '3000'
grafana_user = 'admin'
grafana_password ='admin'

graphite_host = 'graphite'
graphite_port = '80'
graphite_user = 'root'
graphite_password = 'root'

datasource_name = 'GraphiteData'

grafana_url = 'http://{}:{}'.format(grafana_host, grafana_port)
session = requests.Session()
login_post = session.post(
   os.path.join(grafana_url, 'login'),
   data=json.dumps({
      'user' : grafana_user,
      'email' : '',
      'password' : grafana_password }),
   headers={'content-type' : 'application/json'})

# Get the list of datasources
datasources_get = session.get(os.path.join(grafana_url, 'api', 'datasources'))
datasources = datasources_get.json()
print("Datasource before: {}\n".format(datasources))

# Add new datasource
datasources_put = session.post(
   os.path.join(grafana_url, 'api', 'datasources'),
   data=json.dumps({
      'name' : datasource_name,
      'type' : 'graphite',
      'access' : 'proxy',
      'url' : 'http://{}:{}'.format(graphite_host, graphite_port),
      'basicAuth' : True,
      'basicAuthUser' : graphite_user,
      'basicAuthPassword' : graphite_password}),
   headers={'content-type' : 'application/json'})
print("Add datasource response: {}\n".format(datasources_put.json()))

# Get the list of datasources
datasources_get = session.get(os.path.join(grafana_url, 'api', 'datasources'))
datasources = datasources_get.json()
print("Datasource after: {}\n".format(datasources))
