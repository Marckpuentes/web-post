from django.urls import path
from .views import CategoriesView, CategoriesDelete, CategoriesUpdate, PostView, DetailPost, PostUpdate, PostCreate, PostDelete, Search
post_patterns = ([
    path('directorio/', PostView.as_view(), name="view"),
    path('search/<str:category>/', Search.as_view(), name="search"),
    path('detail/<str:slug>/', DetailPost.as_view(), name="detail"),
    path('update/post/<slug:slug>/', PostUpdate.as_view(), name="update-post"),
    path('create/', PostCreate.as_view(), name="create-post"),
    path('delete/post/<slug:slug>/', PostDelete.as_view(), name="delete-post"),
    path('add/category/', CategoriesView.as_view(), name="add"),
    path('delete/<int:pk>/', CategoriesDelete.as_view(), name="delete"),
    path('update/<int:pk>/', CategoriesUpdate.as_view(), name="update"),
], "post")
