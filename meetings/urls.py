from django.urls import path, include
from meetings import views
urlpatterns = [
    # path('list/', views.MeetingListViewSet.as_view(), name='meeting_list'),
    path('comment/<int:meetid>', views.GetEachCommentView.as_view(), name='each_comment_list')
]
