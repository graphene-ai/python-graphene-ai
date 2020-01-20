#!/usr/bin/env python
"""Python SDK for Graphene NLU API"""

__version__ = "0.0.1"

import logging, json, os, requests

from urllib.parse import urljoin

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENDPOINTS = {
    'analyze': 'language/phrase/analyze',
    'context': 'language/phrase/context',
    'business_context': 'language/phrase/context/business',
    'entities': 'language/phrase/entities',
    'business_entities': 'language/phrase/entities/business',
    'similar': 'language/phrase/similar'
}

class Graphene:
    def __init__(self, api_key, endpoint_url=None):
        ''' Constructor for this class. '''
        if endpoint_url is None:
           self.endpoint_url = "https://graphene.indigoresearch.xyz/"
        else:
            self.endpoint_url = endpoint_url   
        self.api_key = api_key

    def request(self, method, session_id, payload=None):
        base = urljoin(self.endpoint_url, 'api/v1/')
        url = urljoin(base, ENDPOINTS[method])
        if method == "context":
            params = {'api_key': self.api_key, 'session_id': session_id }
        else:
            params = {'api_key': self.api_key, 'session_id': session_id, 'payload': payload}

        req = requests.get(url, params = params)
        r = json.loads(req.text)
        if not (("errors" in r) and len(r["errors"])):
            logging.error(r['errors'])
        return r["payload"]


        