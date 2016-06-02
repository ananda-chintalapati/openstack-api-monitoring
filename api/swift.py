import logging

import keystone_client

log = logging(__name__)

log.info("Swift API Validation - Begin")
parser = argparse.ArgumentParser(description='Check OpenStack Swift API for availability.')
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
parser.add_argument('--region', metavar='region', type=str,
                    required=True,
                    help='tenant name to use for authentication')
args = parser.parse_args()

token = keystone_client.get_auth_token(args.username, args.password,
                                       args.tenant, args.auth_url)

if token is not None:
    headers = {'Content-Type' : 'application/json',
               'X-Auth-Token' : token}
    endpoint = keystone_client.get_public_endpoint('swift')
    tenant_id = keystone_client.get_current_tenant_id()
    url = endpoint + '/v2/' + tenant_id +   '/volumes'
    response = request.get(url, headers=headers)
    if response.status_code != 201:
        log.info('Swift call failed with error code %s ' % response.status_code)
    else:
        log.info('Successfully retrieved server details for %s ' % tenant_id)
else:
    log.info('Auth token null. Skipping Glance calls')
log.info("Swift API Validation - End")