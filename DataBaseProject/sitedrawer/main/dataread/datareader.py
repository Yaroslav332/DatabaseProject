from . import User


def get_users():
    service_users = dict()
    f = open("../static/main/txt/data.csv", 'r')
    t = f.readline()
    while t:
        a = t.split(';')
        u = a[0]
        friend = a[1]
        if friend[-1] == "\n":
            friend = friend[0:-1]

        if service_users.keys().__contains__(u):
            (service_users[u]).add_friend(friend)
        else:
            service_users[u] = User.InsideUser(u)

        t = f.readline()
    f.close()
    return service_users.values()