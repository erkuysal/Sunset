from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have an username.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    access_level = models.IntegerField(default=1)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
#   profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    user_followers = models.ManyToManyField('self', symmetrical=False, related_name='follow')

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower_user = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower_user', 'following_user')

    def __str__(self):
        return f'{self.follower_user} follows {self.following_user}'


class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#   balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    coins = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s Wallet'



