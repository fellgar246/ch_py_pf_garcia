"""
URL configuration for proyecto_final_garcia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from BlogTecnoWave.views import *

urlpatterns = [
    path("", HomeView, name="Home"),
    path("<int:start>/", HomeView, name="Home_with_start"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="ArticleDetail"),
    path("add-post/", AddPostView.as_view(), name="AddPost"),
    path("add-category/", AddCategoryView.as_view(), name="AddCategory"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="UpdatePost"),
    path("article/delete/<int:pk>", DeletePostView.as_view(), name="DeletePost"),
    path("category/<str:categories>/", CategoryView, name='Category'),
    path("category-list/", CategoryListView, name='CategoryList'),
    path("like/<int:pk>", LikeView, name="LikePost"),
    path("like/<int:pk>", LikeView, name="LikePost"),
    path("article/<int:pk>/comment/", AddCommentView.as_view(), name="AddComment"),
    path('about/', About, name='About'),
]
