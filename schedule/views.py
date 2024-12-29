from django.shortcuts import render, get_object_or_404
from .models import Contact


def index_login(request):
    login = ''

    context = {'login': login}
    return render(request, 'pages/login_logout/login.html', context=context)


def user_create(request):
    users = ''
    context = {'users': users}
    return render(request, 'pages/users/user_create.html', context=context)


def contact_create(request, contact_id):
    contact = get_object_or_404(Contact.objects, id=contact_id)
    context = {'contacts': contact}
    return render(request, 'pages/contacts/contacts_create.html', context=context)
