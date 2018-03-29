from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todolist_view, name="list"),
    url(r'^hello/', views.hello_django, name="hello"),
    url(r'^edit/[0-9]/', views.edit_view, name="edit"),
]
