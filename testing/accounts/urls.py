from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup_view"),
    path('login/', views.login_view, name='login_view')
]
