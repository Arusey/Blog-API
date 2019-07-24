from django.urls import path

from Blog.posts import views

app_name = "posts"


urlpatterns = [path('posts/', views.PostViewSet.as_view(
    {'get': 'list', "post": "create"}), name='posts-all'),
    path('posts/<pk>/', views.PostViewSet.as_view(
        {"get": "retrieve", "put": "update", "patch": "partial_update",
         "delete": "destroy"}), name='single-post'), ]
