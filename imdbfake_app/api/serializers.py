

from django.core import serializers

from rest_framework import serializers
from imdbfake_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):  # the difference between ModelSerializer and Serializer is that ModelSerializer automatically generates fields based on the model, while Serializer requires you to define each field manually. && ModelSerializer also provides default implementations for create() and update() methods, while Serializer requires you to implement them yourself.
   
    # custom serializer field ***
    len_name = serializers.SerializerMethodField()  # this field is not in the model, but we can add it to the serializer. && SerializerMethodField is a read-only field that gets its value by calling a method on the serializer class. && The method should be named get_<field_name> and should take the object being serialized as its only argument.
    def get_len_name(self, obj):  # this method is called when the serializer is serializing an object. && obj is the object being serialized. && we can use this method to calculate the value of the field based on the object's attributes.
        return len(obj.name)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'active', 'len_name']  # equals to fields = '__all__'  # equals to exclude = []  # equals to exclude = ['id']  
        
    def validate_name(self, value):  #Field-level validation  Fun naming convention: validate_<field_name>
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value
    def validate(self, data):    #Object-level validation    
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description must be different.")
        return data
#**** serializer ******
# def describtion_length(value): # Custom validator function  &&& this function will be used in the serializer field as a validator && can be used with more than one field  &&& should be defined outside the serializer class
#     if len(value) < 10:
#         raise serializers.ValidationError("Description must be at least 10 characters long.")
 
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[describtion_length])
#     active = serializers.BooleanField(default=True)
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
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