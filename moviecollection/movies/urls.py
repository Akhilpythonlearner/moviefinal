from movies import views
from django.urls import path

app_name='movies'

urlpatterns =[
    path('',views.allMoviedetails,name='allMoviedetails'),
    path('<slug:c_slug>/', views.allMoviedetails,name='movie_details_by_category'),
    path('slug:c_slug/<slug:movie_slug>/', views.detailedOfMovie, name="detailedOfMovie"),
]