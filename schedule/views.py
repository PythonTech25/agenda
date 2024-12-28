from django.shortcuts import render
from .models import Contact


# Create your views here.
def index_login(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }
    return render(request, 'pages/login_logout/login.html', context=context)
