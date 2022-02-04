from django.urls import path
from . import views

# {% url 'index' %} -> name = 'index'
urlpatterns = [
    path('',views.index,name='index'), #경로에 대한 name = 'index' # 특정 앱의 index name
    path('var01/',views.variables01),
    path('var02/',views.variables02),
    path('forloop/',views.for_loop),
    path('if01/',views.if01),
    path('if02/',views.if02),
    path('request/',views.get_post),
]