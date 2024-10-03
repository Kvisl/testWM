from rest_framework.viewsets import ModelViewSet
from .serializers import CatSerializer, CatDetailSerializer, BreedSerializer, RatingSerializer, PostRatingSerializer
from .models import Cat, Breed, Rating
from cat.permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CatViewSet(ModelViewSet):
    queryset = Cat.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['breed']


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='breed',
                description='ID породы кота для фильтрации',
                required=False,
                type=int
            )
        ]
    )


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CatDetailSerializer
        return CatSerializer


    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return super().get_permissions()


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return super().get_permissions()


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = PostRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

