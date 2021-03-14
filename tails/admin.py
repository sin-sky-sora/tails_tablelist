from django.contrib import admin
from .models import UserModel,TradeCommentModel,TradeBoardModel
# Register your models here.

admin.site.register(UserModel)

admin.site.register(TradeBoardModel)
admin.site.register(TradeCommentModel)