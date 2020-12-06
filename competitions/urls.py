from django.urls import path, include
from competitions import views

urlpatterns = [
    path('join/<int:pk>', views.CompetitionJoinAPIView.as_view(), name='competition_join')

]