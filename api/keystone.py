import argparse
import json
import request
import logging

import keystone_client

log = logging(__name__)

log.info("Keystone API Validation - Begin")
parser = argparse.ArgumentParser(description='Check OpenStack Keystone API for availability.')
parser.add_argument('--auth_url', metavar='URL', type=str,
                    required=True,
                    help='Keystone URL')
parser.add_argument('--username', metavar='username', type=str,
                    required=True,
                    help='username to use for authentication')
parser.add_argument('--password', metavar='password', type=str,
                    required=True,
                    help='password to use for authentication')
parser.add_argument('--tenant', metavar='tenant', type=str,
                    required=True,
                    help='tenant name to use for authentication')
args = parser.parse_args()

token = None
headers = {'Content-type' : 'application/json'}

log.info("Generating token for user %s " % args.username)
try:
    response = keystone_client.call_keystone(args.username, args.password,
                               args.tenant, args.auth_url)
    
    if response.status_code != 200:
        log.info("Token generation Failed")
        raise Exception("Keystone call failed with HTTP error code %s " 
                        % response.status_code)
    else:
        token = response.json()['access']['token']['id']
        if token is None:
            log.info("Token generation Failed")
            raise Exception("Received Null Auth token with error code %s " 
                        % response.status_code) 
        else:
            log.info("Auth token generated successfully")
except Exception as e:
    log.debug("Exception while generating token %r " % e)
    log.info("Token generation Failed")
    raise Exception("Keystone call failed with HTTP error code %s " 
                    % response.status_code)

log.info("Keystone API Validation - End")