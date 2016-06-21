#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_escalation_policies():
    url = 'https://{0}.pagerduty.com/api/v1/escalation_policies'.format(SUBDOMAIN)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.json()
