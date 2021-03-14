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

# https://djangobrothers.com/blogs/related_name/#related_name%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9
# ↑ 複数のForeign,Manyがある場合のrelated_name ↑
class BoardModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="create_user")
    closed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    favorite = models.ManyToManyField(UserModel,related_name="favorite_user")
    
class CommentModel(models.Model):
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class TradeCommentModel(CommentModel):
    pass

PLACE_CHOICES = ((-1,"sp"),(0,"pcsp"),(1,"pc"))
class TradeBoardModel(BoardModel):
    place = models.IntegerField(choices=PLACE_CHOICES)
    comment = models.ForeignKey(TradeCommentModel,on_delete=models.CASCADE)
