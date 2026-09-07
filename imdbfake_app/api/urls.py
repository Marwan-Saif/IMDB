
from django.urls import path
# from imdbfake_app.api.views import  movie_list, movie_detail
from imdbfake_app.api.views import MovieDetailAV, MovieListAV


urlpatterns=[
    path('', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_detail'),
]