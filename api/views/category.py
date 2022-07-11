from api.models.category import Category
from api.serializers.category_serializer import CategorySerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
