from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', CreateUserView.as_view(), name='createUser'),
]