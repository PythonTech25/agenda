from django.shortcuts import render, get_object_or_404
from .models import Contact
from . import form

app_name = 'contact'


def index_login(request):
    login = ''

    context = {'login': login}
    return render(request, 'pages/login_logout/login.html', context=context)


def user_create(request):
    users = ''
    context = {'users': users}
    return render(request, 'pages/users/user_create.html', context=context)


def contact_read(request):
    contact = Contact.objects.all()
    context = {'contacts': contact}
    return render(request, 'pages/contacts/contact_read.html', context=context)


def contact_detail(request, contact_id):
    # single_contact = Contact.objects.get(pk=contact_id)
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    context = {'contact': single_contact}
    return render(request, 'pages/contacts/contact_detail.html', context=context)


def contact_create(request):
    if request.method == 'POST':
        create = form.ContactForm(request.POST)
        if create.is_valid():
            create.save(commit=False)
            create.save()

    create = form.ContactForm()
    context = {'form': create}
    return render(request, 'pages/contacts/contact_create.html', context=context)
