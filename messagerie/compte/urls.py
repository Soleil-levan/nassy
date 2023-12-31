from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CreateUserView.as_view(), name='createUser'),
    path('delete/', DeleteView.as_view(), name='deleteUser'),
]
