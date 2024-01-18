from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('details/<int:id>/',views.detail,name="detail"),
    path('addmovies',views.add_movies,name="add_movies"),
    path('editmovies/<int:id>',views.edit_movies,name="edit_movies"),
    path('delete/<int:id>',views.delete_movies,name="delete_movies"),
]
