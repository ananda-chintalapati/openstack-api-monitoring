import logging

import keystone_client

log = logging(__name__)

log.info("Neutron API Validation - Begin")
parser = argparse.ArgumentParser(description='Check OpenStack Neutron API for availability.')
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
    endpoint = keystone_client.get_public_endpoint('neutron')
    url = endpoint + '/v2.0/networks'
    response = request.get(url, headers=headers)
    if response.status_code != 201:
        log.info('Neutron call failed with error code %s ' % response.status_code)
    else:
        log.info('Successfully retrieved server details for %s ' % tenant_id)
else:
    log.info('Auth token null. Skipping Neutron calls')
log.info("Neutron API Validation - End")