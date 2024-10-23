from django.urls import path
from . import views
from .views import homeListView





urlpatterns = [
    path('' , homeListView.as_view() , name='home' ),
    path('login/' , views.user_login, name='login'),
    path('logout/' , views.user_logout , name='logout'),
    path('register/', views.register_user, name='register'),
]