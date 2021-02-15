from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    #유저모델 생성할 때 사용
    #Manager for user profiles

    def create_user(self, email, name, password=None):
        #Create a new user profile
        if not email:
            raise ValueError('User must have an email address')

        #소문자로 바꿔주는듯
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        #Create and save a new superuser with given details
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    #unique=True를 주면 한 필드에 같은 데이터가 못들어가게 함
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #유저 모델에서 필드의 이름을 설명하는 string, 유니크 식별자, 여기에 해준 설정떄문에 로그인할 때 id가 email로 됨
    USERNAME_FIELD = 'email'
    #createsuperuser 커멘드로 유저를 생성할 때 나타날 필드 이름 목록
    REQUIRED_FIELDS = ['name']
        

    def geet_short_name(self):
        return self.name

    #객체를 출력할 때 __str__메서드를 출력함
    def __str__(self):
        return self.email
    