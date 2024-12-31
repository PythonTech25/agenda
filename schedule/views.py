from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Contact
from . import forms


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
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, 'Contato adicionado com sucesso!')
            return redirect('contact_read')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = forms.ContactForm()

    context = {'form': form}
    return render(request, 'pages/contacts/contact_create.html', context)

