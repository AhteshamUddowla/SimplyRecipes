from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('account/', views.account_view, name='account'),
    path('edit-account/<str:pk>/', views.edit_account_view, name='edit-account'),


]