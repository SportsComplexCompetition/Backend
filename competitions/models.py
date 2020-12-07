from django.db import models
from accounts.models import User

COMPETITION_TYPE = {
    (0, '경쟁'),
    (1, '챌린지')
}

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


class Competition(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='competition_host')
    comp_type = models.PositiveIntegerField(choices=COMPETITION_TYPE)
    location = models.PositiveIntegerField(choices=LOCATION_CHOICES, default=0)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    ended_at = models.DateField()
    max_people = models.PositiveIntegerField()
    joined_people = models.ManyToManyField(User, related_name='competition_join_people',  default=None, blank=True)
    require_money = models.PositiveIntegerField()
    total_money = models.PositiveIntegerField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name='competition_winner')
    
    def __str__(self):
        return self.title