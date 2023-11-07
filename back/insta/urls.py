from django.urls import path, include
from .views import (
    CheckView,
)


urlpatterns = [
    path("api/check/", CheckView.as_view(), name="check_ok"),
]
