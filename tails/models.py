from django.db import models
from django.utils import timezone
from random import randint
import hashlib

class UserModel(models.Model):
    user_str = models.CharField(max_length=12)
    # シャープ付 例:#ffffff
    user_color = models.CharField(max_length=7)
    user_hash = models.UUIDField()
    finger_print = models.CharField(max_length=32)
    location_hash = models.CharField(max_length=64)
    
    def random_colors(self) -> int:
        r,g,b = randint(0,255),randint(0,255),randint(0,255)
        return "#%02X%02X%02X" % (r,g,b)
    def create_hash(text:str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()

class TradeBoardModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    author = models.ManyToManyField(UserModel)
    closed = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    favorite = models.ManyToManyField(UserModel)

