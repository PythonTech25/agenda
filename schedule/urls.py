from django.urls import path
from . import views

urlpatterns = [
    # login / logout
    path("", views.index_login, name='index_login'),

    # user crud
    path('user/create/', views.user_create, name='user_create'),

    # contact crud
    path('contacts/create/<int:contact_id>/', views.contact_create, name='contact_create'),
]
