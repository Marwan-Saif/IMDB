# from django.shortcuts import render
# from django.http import JsonResponse
# from imdbfake_app.models import Movie

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {'movie': {
#                 'id': movie.id,
#                 'title': movie.name,
#                 'description': movie.description,
#                 # 'release_date': movie.release_date,
#             }}
#     return JsonResponse(data)
    