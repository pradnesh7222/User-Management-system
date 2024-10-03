from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('edit/<int:id>/', views.edit_view, name='edit'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
]
