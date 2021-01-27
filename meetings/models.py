from django.db import models
from accounts.models import User


LOCATION_CHOICES = (
    (0, '서울'),
    (1, '대구'),
    (2, '대전'),
    (3, '광주'),
    (4, '인천'),
    (5, '부산'),
    (6, '울산'),
    (7, '세종'),
    (8, '제주'),
    (9, '경기도'),
    (10, '강원도'),
    (11, '충청남도'),
    (12, '충청북도'),
    (13, '전라남도'),
    (14, '전라북도'),
    (15, '경상남도'),
    (16, '경상북도'),
)



class Meeting(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meeting_host')
    location = models.PositiveIntegerField(choices=LOCATION_CHOICES, default=0)
    title = models.CharField(max_length=30, blank=False, null=True)
    find_people = models.PositiveIntegerField()
    body = models.CharField(max_length=500, blank=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, blank=False, related_name='comment_from_meeting')
    content = models.TextField(blank=False, max_length=500) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.nickname