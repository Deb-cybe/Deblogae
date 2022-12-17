from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('bposts/<int:id>',views.bposts,name="bposts"),
    path('addpost',views.addpost,name="addpost"),
    path('editpost/<int:id>',views.editpost,name="editpost"),
    path('deletepost/<int:id>',views.deletepost,name="deletepost"),
]
