from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage import CloudStorageAccount
from azure.storage.blob.models import ContentSettings

from azure.graphrbac import GraphRbacManagementClient

import os


class Auth:
    def __init__(self, email, passwd, sid):
        self.email = email
        self.passwd = passwd
        self.sid = sid

    def set_credentials(self, resource=None):
        params = {}
        if resource:
            params["resource"] = resource
        self.credentials = UserPassCredentials(email, passwd, **params)
        self.subscription_id = sid

    def get_user_client(self):
        self.set_credentials(resource='https://graph.windows.net')
        return GraphRbacManagementClient(self.credentials, os.environ["AD_DOMAIN"])
