from django.urls import path
from .views import CreateUserView, CustomAuthToken

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]
