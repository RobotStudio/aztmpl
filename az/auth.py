from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient

import os


class Auth:
    def __init__(self, email=None, passwd=None, sid=None, *args, **kwargs):
        self.subscription_id = sid or os.environ["AZURE_SUBSCRIPTION_ID"]
        self.credentials = UserPassCredentials(
                                email or os.environ["AZURE_CLIENT_ID"],
                                passwd or os.environ["AZURE_CLIENT_SECRET"],
                                **kwargs)
    def get_resource_client(self):
        self.resource_client = ResourceManagementClient(self.credentials, self.subscription_id)


if __name__ == "__main__":
    a = Auth()
    client = a.resource_client
