from django.db import models
from accounts.models import User

COMPETITION_TYPE = {
    (0, '경쟁'),
    (1, '챌린지')
}

class Competition(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='competition_host')
    comp_type = models.PositiveIntegerField(choices=COMPETITION_TYPE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    ended_at = models.DateField()
    max_people = models.PositiveIntegerField()
    joined_people = models.ManyToManyField(User, related_name='competition_join_people',  default=None, blank=True)
    money = models.PositiveIntegerField(blank=False, null=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name='competition_winner')

    def __str__(self):
        return self.title