from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmainpage, name="mainpage"),
    path('introduction/',showintroduction, name="introduction"),
    path('show/',showshow, name="show"),
    path('post/',showpost, name="post"),
    path('<int:id>',detail, name="detail"),
    path('new/', new, name="new"),
    path('create/',create, name="create"),
    path('edit/<int:id>',edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]