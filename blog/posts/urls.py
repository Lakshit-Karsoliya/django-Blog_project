from django.urls import path
from . import views
#urls are different paths in website
urlpatterns=[
    path('', views.index,name='index'),
    path('fullblog/<str:s>',views.fullblog,name='fullblog'),
    path('addblog',views.addblog,name='addblog')
]