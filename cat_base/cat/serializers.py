from rest_framework import serializers
from .models import Cat, Breed, Rating


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['score']


class PostRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['score', 'cat']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CatSerializer(serializers.ModelSerializer):

    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['id', 'author', 'colour', 'age', 'description', 'breed', 'average_rating']


    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            return sum(rating.score for rating in ratings) / ratings.count()
        return 0

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CatDetailSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['colour', 'age', 'description', 'breed', 'average_rating']

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            return sum(rating.score for rating in ratings) / ratings.count()
        return 0


class PostCatSerializer(serializers.ModelSerializer):

    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Cat
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)