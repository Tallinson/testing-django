from django.urls import path
from . import views

# app_name = "articles"

urlpatterns = [
    path('', views.article_list),
    path('', views.article_detail)
]