class InsideUser(object):
    def __init__(self, name):
        self.friends_set = set()
        self.name = name
        self.external_friends_set = set()
        self.inside_friends_set = set()
        self.friends_domain = dict()

    def add_friend(self, name):
        friend = ExternalUser(name)
        self.friends_set.add(friend)
        if not self.friends_domain.keys().__contains__(friend.domain):
            self.friends_domain[friend.domain] = set([name])
        else:
            self.friends_domain[friend.domain].add(name)
        if friend.domain == "xabber.org":
            self.inside_friends_set.add(name)
        else:
            self.external_friends_set.add(name)


class ExternalUser(object):
    def __init__(self, name):
        self.name = name
        s = name.split('@')[1]
        self.domain = s.split('.')[0]

