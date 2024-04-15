from django.contrib import admin
from django.urls import include, path

urlpatterns=[
    path("comrade/connect/", include("connect.urls")),
    path("comrade/connect/admin/",admin.site.urls),
]