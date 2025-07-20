from django.urls import path
from . import views


urlpatterns = [

# Authentication URLs
path('login/', views.LoginView.as_view(), name='login'),
path('logout/', views.LogoutView.as_view(), name='logout'),
path('signup/', views.SignupView.as_view(), name='signup'),

# Home URL
path('', views.HomeView.as_view(), name='home'),

# Note URLs
path('create/', views.create_note, name='create_note'),
path('notes/', views.note_list, name='note_list'),

]
