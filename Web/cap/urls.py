from django.urls import path
from .views import ListCap


cap_patterns = ([
    path('', ListCap.as_view(), name="ListCap")
], "cap")
