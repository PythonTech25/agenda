from django.urls import path
from . import views

urlpatterns = [
    # login / logout
    path("", views.index_login, name='index_login'),

    # user crud
    path('user/create/', views.user_create, name='user_create'),

    # contact crud
    path('contacts/read/', views.contact_read, name='contact_read'),
    path('contacts/<int:contact_id>/detail', views.contact_detail, name='contact_detail'),
    # path('contacts/<int:contact_id>/update', views.contact_update, name='contact_update'),
    # path('contacts/<int:contact_id>/delete', views.contact_delete, name='contact_delete'),
    path('contacts/create', views.contact_create, name='contact_create'),
]