import getpass
from password import User, Credentials


def create_user(user_name, password):
    new_user = User(user_name, password)
    return new_use
def save_users(user):
    user.save_user()


def find_user(name):
    return User.find_by_name(name)


def check_user_exists(user_name, password):
    if_user_exist = Credentials.user_exist(user_name,password)
    return if_user_exist

def create_credential(account_name,account_password):
    new_credential = Credentials(account_name,account_password)

    return new_credential    
