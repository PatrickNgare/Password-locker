import random

global user_list
class User:
    """docstring for User."""

    user_list = []

    def __init__(self, user_name, password):
        '''
        class properties
        '''

        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save user_list
        '''
        User.user_list.append(self)

    @classmethod
    def find_by_name(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return user
