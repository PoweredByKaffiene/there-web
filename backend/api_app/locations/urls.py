from django.urls import path

from .views import save_location

urlpatterns = [
    path("save", save_location, name="login"),
]
