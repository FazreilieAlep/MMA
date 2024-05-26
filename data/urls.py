from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("json/", views.host_list, name="host_list"),
    path("<str:host_path>/", views.host_index, name="host detail"),
    path("<str:host_path>/json", views.web_api_list, name="web_api_list"),
    path("<str:host_path>/<str:data_path>", views.data_index, name="data detail"),
    path("<str:host_path>/<str:data_path>/json", views.data_list, name="data detail"),
    path("<str:host_path>/<str:data_path>/table", views.table, name="table"),
    path("<str:host_path>/<str:data_path>/updates", views.updates, name="updates"),
    path("<str:host_path>/<str:data_path>/update-db", views.update_db, name="update db"),
]