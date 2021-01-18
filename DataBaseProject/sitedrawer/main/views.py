from django.shortcuts import render
from .dataread import User
from .dataread import datareader


# Create your views here.
def main(request):
    u = User.InsideUser('booba@mail.ru')
    u.add_friend('vasya@gmail.com')
    u.add_friend('vasya@yandex.com')
    u.add_friend('vasya@mail.ru')
    u.add_friend('vasya@xabber.org')
    a = {
        'users': [u],
    }
    return render(request, 'main/index.html', a)
