from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signin/', views.CustomLoginView.as_view(), name='signin'),
    path('signup/', views.CustomRegisterView.as_view(), name='signup'),
    path('mycomplist/', views.UserJoinCompetitionView.as_view(), name='joincomplist'),
    path('mymeetlist/', views.UserJoinMeetingView.as_view(), name='joinmeetlist'),
]
