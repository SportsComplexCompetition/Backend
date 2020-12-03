from django.db import models
from accounts.models import User

class Competition(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    join_people = models.ManyToManyField(User, related_name='competition_join_people',  default=None, blank=True)
    created = models.DateField(auto_now_add=True)