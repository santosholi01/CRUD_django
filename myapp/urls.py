from django.urls import path
from .views import home, add, delete,edit

urlpatterns=[
    path('',home.as_view(), name="home" ),
    path('Add/',add.as_view(), name="Add"),
    path('Delete/' , delete.as_view(), name="Delete"),
    path('Edit/<int:id>/', edit.as_view(), name="Edit")
]