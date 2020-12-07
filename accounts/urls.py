from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signin/', views.CustomLoginView.as_view(), name='signin'),
    path('signup/', views.CustomRegisterView.as_view(), name='signup'),
]
