from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('data/', include("data.urls")),
    path('admin/', admin.site.urls),
]
