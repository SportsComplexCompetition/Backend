from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

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





class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(max_length=10, blank=False, null=True)
    age = models.PositiveIntegerField(blank=True, null=False)
    sex = models.CharField(max_length=10, blank=False, null=True)
    location = models.PositiveIntegerField(choices=LOCATION_CHOICES, default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'age']

    objects = UserManager()

    # def __str__(self):
    #     return self.nickname