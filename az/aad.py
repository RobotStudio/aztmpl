from azure.graphrbac.models import UserCreateParameters, UserCreateParametersPasswordProfile

from az.auth import Auth

import os


DEFAULT_USER_PARAMS = {
    account_enabled: True,
    #display_name: 'Test Buddy',
    #mail_nickname: 'testbuddy',
}

def gen_passwd(size):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))


class User:
    def __init__(self, username, display_name=None):
        self.default_user_params = {
            "user_principal_name": f"{username}@{os.environ['AD_DOMAIN']}",
            "mail_nickname": username
        }
        if display_name:
            self.default_user_params.update({"display_name": display_name})
        self.username = username

    def create(self, user=None, passwd=None):
        if user:
            self.default_user_params.update(user)
        if not passwd:
            passwd = gen_passwd(12)
            print("Using password: {passwd}")
            print("Please take note of this.")
        password = UserCreateParametersPasswordProfile(password=passwd)
        user_params = UserCreateParameters(
                        self.default_user_params.update({"password_profile": password}))
        self.user = graphrbac_client.user_operations.create(user_params)
        return self.user

    def find(self, _filter):
        users = graphrbac_client.user_operations.list(_filter)
        if len(users) > 0:
            self.user = users.pop()
        return self.user

    def destroy(self):
        if self.user:
            return graphrbac_client.user_operations.delete(self.user.object_id)


if __name__ == "__main__":
    u = User("karma0")
    u.create()
