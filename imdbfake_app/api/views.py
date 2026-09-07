from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView, Http404
from imdbfake_app.api.serializers import StreamPlatformSerializer, WatchListSerializer
from imdbfake_app.models import StreamPlatform, WatchList

class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class StreamPlatformDetailAV(APIView):
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(platform, data=request.data, partial=True) #partial means that i want put fun to act as patch &&&& if i didnt pass the platform instance, it will create a new platform instead of updating the existing one
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        platform = self.get_object(pk)
        platform.delete()
        return Response(status=204)
class WatchListAV(APIView):
    def get(self, request):
        WatchList = WatchList.objects.all()
        serializer = WatchListSerializer(WatchList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class WatchListDetailAV(APIView):
    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = WatchListSerializer(movie, data=request.data, partial=True) #partial means that i want put fun to act as patch &&&& if i didnt pass the movie instance, it will create a new movie instead of updating the existing one
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=204)
    
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer=MovieSerializer (movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=404)
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=404)
#         serializer = MovieSerializer(movie, data=request.data) #if i didnt pass the movie instance, it will create a new movie instead of updating the existing one
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=404)
#         movie.delete()
#         return Response(status=204)