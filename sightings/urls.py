from django.urls import path

from . import views

urlpatterns=[
        path('', views.index, name='squirrel_list'),
        path('add/',views.add, name='add_squirrel'),
        path('<squirrel_ID>/',views.edit, name='edit_squirrel'),
        
]
