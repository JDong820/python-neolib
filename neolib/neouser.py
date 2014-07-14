from __future__ import print_function
from getpass import getpass
import requests
import urls

try:
    input = raw_input
except NameError:
    pass

class ActivityNotFound(Exception):
    def __init__(self, activity):
        self.activity = activity
    def __str__(self):
        return repr(self.activity)

class AccountTooYoung(Exception):
    def __init__(self, age_req):
        self.req = age_req
    def __str__(self):
        return repr(self.req)

class InvalidLogin(Exception):
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return repr(self.username)

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
        return "Logout" in self.session.get("http://www.neopets.com/index.phtml").text

    def _login(self, credentials, headers={}):
        """Login using a credentials dict, optionally supplying headers."""
        self.session.post('http://www.neopets.com/login.phtml',
                          data=credentials, headers=headers)
        if not self.logged_in:
            raise InvalidLogin(credentials['username'])

    def get_monthly_freebie(self):
        response = self.session.get(urls.urls['monthly_freebie'])
        if 'Freebies For You!' not in response.text:
            raise ActivityNotFound("Monthly Freebie")
        if 'your account must be at least 30 days old' in response.text:
            raise AccountTooYoung(30)
