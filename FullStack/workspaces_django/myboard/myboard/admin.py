from django.contrib import admin
from .models import MyBoard,MyMember # 현재 내가 있는 위치에서 models.py 찾기

admin.site.register(MyBoard)
admin.site.register(MyMember)