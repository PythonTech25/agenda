from django.shortcuts import render


# Create your views here.
def index_login(request):
    return render(request, 'pages/login_logout/login.html')
