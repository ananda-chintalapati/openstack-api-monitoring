import request
import json
import logging

log = logging.getLogger(__name__)

response = None
def call_keystone(username, password, tenant, auth_url):
    try:
        auth_req = {"auth": {
                             "tenantName": tenant,
                             "passwordCredentials": {
                                                     "username": username,
                                                     "password": password
                                                     }
                              }
                    }
    
    
        url = auth_url
        if url.endswith('/'):
            url = url + 'tokens'
        else:
            url = url + '/tokens'
        
        log.debug("Request post to URL %s " % url)
        log.debug("POST call payload %s " % json.dumps(auth_req))
        
        return request.post(url, data=auth_req, headers=headers)
    except Exception as e:
        log.info("Exception while calling Keystone %s " % e)
        raise Exception(e)


def get_auth_token(username, password, tenant, auth_url):
    response = call_keystone(username, password, tenant, auth_url)
    token = None
    if response is not None:
        token = response.json()['access']['id']['token']
    return token

def get_public_endpoint(component, region=None):
    if response is not None:
        service_list = response.json()['access']['serviceCatalog']
        for service in service_catalog:
            if service['name'] == component:
                endpoint_list = service['endpoints']
                if region is None:
                    return endpoint[0]['publicURL']
                else:
                    for endpoint in endpoint_list:
                        if endpoint['region'] == region:
                            return endpoint['publicURL']
    return None

def get_current_tenant_id():
    if response is not None:
        tenant_id = response.json()['access']['token']['tenant']['id']
        return tenant_id
    return None