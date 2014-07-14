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
