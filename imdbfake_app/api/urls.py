
from django.urls import path
# from imdbfake_app.api.views import  movie_list, movie_detail
from imdbfake_app.api.views import  StreamPlatformAV, StreamPlatformDetailAV, WatchListAV, WatchListDetailAV


urlpatterns=[
    path('', WatchListAV.as_view(), name='watchlist_list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='watchlist_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform_list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform_detail'),
] 