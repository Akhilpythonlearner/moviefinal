from django.urls import path
from users import views
app_name='users'
urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('addmovies/',views.AddMovies,name='addmovies'),
    path('update/<int:id>',views.Update,name='update'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('updatedetails/<int:pk>/',views.TodoUpdateView.as_view(),name='updatedetails'),
]