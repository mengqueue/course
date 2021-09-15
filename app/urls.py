from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('courselist/', views.course_list, name='course_list'),
    path('search/', views.search, name='search'),
]