# openstack-api-monitoring

Initial Commit:
_______________

- These are python modules to monitor basic OpenStack APIs.
- Every script is independent of each other except keystone_client.
- KeyStone_client is common to all scripts to generate auth tokens to interact with APIs
- The scripts expect the following
    * Username
    * Password
    * Keystone Auth URL
    * Region
    * Tenant
