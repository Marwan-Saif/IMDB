

from django.core import serializers

from rest_framework import serializers
from imdbfake_app.models import Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class WatchListSerializer(serializers.ModelSerializer):  # the difference between ModelSerializer and Serializer is that ModelSerializer automatically generates fields based on the model, while Serializer requires you to define each field manually. && ModelSerializer also provides default implementations for create() and update() methods, while Serializer requires you to implement them yourself.
    reviews = ReviewSerializer(many=True, read_only=True)  # nested serializer to show the related reviews for each watchlist item. && the name should match the related_name in the ForeignKey field of the Review model.
    class Meta:
        model = WatchList
        fields = '__all__'  # equals to fields = '__all__'  # equals to exclude = []  # equals to exclude = ['id']  
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)  # nested serializer to show the related watchlist items for each stream platform. && the name should match the related_name in the ForeignKey field of the WatchList model. 
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        


#**** serializer ******
# def describtion_length(value): # Custom validator function  &&& this function will be used in the serializer field as a validator && can be used with more than one field  &&& should be defined outside the serializer class
#     if len(value) < 10:
#         raise serializers.ValidationError("Description must be at least 10 characters long.")
 
# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[describtion_length])
#     active = serializers.BooleanField(default=True)
    
#         return WatchList.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('name', instance.name)
#         instance.story_line = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def vslidate_name(self, value):  #Field-level validation  Fun naming convention: validate_<field_name>
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long.")
#         return value
#     def validate(self, data):    #Object-level validation    
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description must be different.")
#         return data