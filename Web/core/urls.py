from django.urls import path
from .views import HomePageView, SamplePageView

core_patterns = ([
    path('home/', HomePageView.as_view(), name="home"),
    path('404/', SamplePageView.as_view(), name="404"),
], 'core')