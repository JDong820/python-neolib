from __future__ import print_function
from getpass import getpass
import requests
import activity
from exceptions import (
    InvalidLogin,
)

try:
    input = raw_input
except NameError:
    pass

class NeoUser(object):
    def __init__(self, username=None, password=None):
        """Create a neouser with a username and password. If any are not
        supplied, a prompt will appear.
        """
        if username and password:
            credentials = {'username': username,
                           'password': password}
        else:
            credentials = {'username': input('Username: '),
                           'password': getpass()}
        self.session = requests.session()
        self._login(credentials)

    @property
    def logged_in(self):
        """Returns True if the user is logged in, False otherwise."""
        return "Logout" in\
                self.session.get("http://www.neopets.com/index.phtml").text

    def _login(self, credentials, headers={}):
        """Login using a credentials dict, optionally supplying headers."""
        self.session.post('http://www.neopets.com/login.phtml',
                          data=credentials, headers=headers)
        if not self.logged_in:
            raise InvalidLogin(credentials['username'])

    @property
    def activity(self):
        return activity.Activity(self.session)
