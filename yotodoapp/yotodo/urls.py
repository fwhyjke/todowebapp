from django.urls import path
from .views import *

urlpatterns = [
    path('welcome', welcomepage, name='welcome'),
    path('registration', Registration.as_view(), name='registration'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('', MainPage.as_view(), name='main'),
    path('complete_task/<int:pk>/', CompleteTaskView.as_view(), name='complete_task'),
]
