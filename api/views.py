from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, HomeHero
from .serializers import CategorySerializer, ProductSerializer, HomeHeroSerializer, ContactMessageSerializer

class CategoryListAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductListAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class HomeDataAPIView(APIView):
    def get(self, request):
        hero = HomeHero.objects.filter(is_active=True)

        return Response(HomeHeroSerializer(hero, many=True).data)

class ContactMessageCreateAPIView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)